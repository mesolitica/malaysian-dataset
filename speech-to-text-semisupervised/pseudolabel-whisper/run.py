from accelerate import Accelerator, InitProcessGroupKwargs
from torch.utils.data import DataLoader, Dataset
from datetime import datetime
from datasets import Audio
from dataclasses import dataclass
import pandas as pd
import numpy as np
import torch
import json
import os
import soundfile as sf
from datetime import timedelta
from tqdm import tqdm
from transformers import (
    HfArgumentParser,
    Seq2SeqTrainingArguments,
    WhisperConfig,
    WhisperFeatureExtractor,
    WhisperForConditionalGeneration,
    WhisperProcessor,
    WhisperTokenizerFast,
)

chunks = 30
sr = 16000


def collactor(rows):
    a = []
    for row in rows:
        a.append(row['array'])
    return np.stack(a, axis=0)


class Train(Dataset):
    def __init__(self, indices, maxlen_cache_df=5, maxlen_cache_audio=50):
        self.indices = {}
        for k, v in indices.items():
            for i in range(int(k), v['start'] + v['end'], 1):
                self.indices[i] = v

        self.max_index = len(self.indices)
        self.cache_df = {}
        self.cache_audio = {}
        self.maxlen_cache_df = maxlen_cache_df
        self.maxlen_cache_audio = maxlen_cache_audio
        self.audio = Audio(sampling_rate=16000)

    def __len__(self):
        return self.max_index

    def __getitem__(self, item):
        if item < 0:
            item = self.max_index + item

        v = self.indices[item]

        key_row = f"{v['filename']}-{v['i']}"
        chunk_index = item - v['start']

        if key_row not in self.cache_audio:

            if v['filename'] not in self.cache_df:
                df = pd.read_parquet(v['filename'])
                if len(self.cache_df) >= self.maxlen_cache_df:
                    keys = list(self.cache_df.keys())
                    self.cache_df.pop(sorted(keys)[0], None)
                self.cache_df[v['filename']] = df
            else:
                df = self.cache_df[v['filename']]

            row = df.iloc[int(v['i'])]
            audio = self.audio.decode_example(self.audio.encode_example(row['filename']))
            if len(self.cache_audio) >= self.maxlen_cache_audio:
                keys = list(self.cache_audio.keys())
                self.cache_audio.pop(sorted(keys)[0], None)
            self.cache_audio[key_row] = audio

        else:
            audio = self.cache_audio[key_row]

        return {
            'array': audio['array'][(chunks * sr) * chunk_index: (chunks * sr) * (chunk_index + 1)]
        }


@dataclass
class ModelArguments:
    model_name_or_path: str = 'openai/whisper-large-v3'
    attn_type: str = 'flash_attn_2'
    indices_filename: 'str' = 'indices-crawl-youtube.json'
    folder_output: str = 'output'
    folder_output_audio: str = 'output-audio'
    step_file: str = 'step.json'
    batch_size: int = 8
    dataloader_num_workers: int = 1


def main():
    global_rank = int(os.environ['RANK'])
    parser = HfArgumentParser(ModelArguments)
    model_args = parser.parse_args_into_dataclasses()[0]
    print(global_rank, model_args)

    os.makedirs(model_args.folder_output, exist_ok=True)
    os.makedirs(model_args.folder_output_audio, exist_ok=True)

    torch_dtype = torch.bfloat16
    mixed_precision = 'bf16'
    kwargs = InitProcessGroupKwargs(timeout=timedelta(seconds=7200))
    accelerator = Accelerator(
        mixed_precision=mixed_precision,
        kwargs_handlers=[kwargs],
    )
    config = WhisperConfig.from_pretrained(
        model_args.model_name_or_path
    )
    feature_extractor = WhisperFeatureExtractor.from_pretrained(
        model_args.model_name_or_path
    )
    tokenizer = WhisperTokenizerFast.from_pretrained(
        model_args.model_name_or_path
    )
    processor = WhisperProcessor.from_pretrained(
        model_args.model_name_or_path
    )
    model = WhisperForConditionalGeneration.from_pretrained(
        model_args.model_name_or_path,
        torch_dtype=torch_dtype,
        use_flash_attention_2=model_args.attn_type == 'flash_attn_2',
    )
    model.eval()
    _ = model.cuda()
    print(global_rank, model.dtype, model.device)

    with open(model_args.indices_filename) as fopen:
        global_indices = json.load(fopen)

    train = Train(global_indices)
    dataloader = DataLoader(
        train,
        batch_size=model_args.batch_size,
        collate_fn=collactor,
        num_workers=model_args.dataloader_num_workers,
        pin_memory=True,
    )
    dataloader = accelerator.prepare(dataloader)

    start_step = 0
    try:
        with open(model_args.step_file) as fopen:
            start_step = json.load(fopen) + 1
        print(f'continue from {start_step}')
    except Exception as e:
        print('failed to load last step count, continue from 0', e)

    dataloader = accelerator.skip_first_batches(dataloader, num_batches=start_step)
    batches = tqdm(dataloader, disable=not accelerator.is_local_main_process)

    step_file_temp = f'{model_args.step_file}-temp'

    for step, batch in enumerate(batches):
        step = step + start_step
        p = processor(batch, return_tensors='pt')
        p['input_features'] = p['input_features'].to(model.device, dtype=torch_dtype)
        generate_fn = model.generate
        output_ms = generate_fn(
            p['input_features'],
            output_scores=True,
            return_dict_in_generate=True,
            language='ms',
            return_timestamps=True
        )
        output_en = generate_fn(
            p['input_features'],
            output_scores=True,
            return_dict_in_generate=True,
            language='en',
            return_timestamps=True
        )
        last_logits_ms = torch.stack(output_ms.scores, dim=1)
        m1 = (last_logits_ms.argmax(dim=-1) < processor.tokenizer.vocab_size)
        m2 = (last_logits_ms.argmax(dim=-1) != processor.tokenizer.pad_token_id)
        mask = m1 & m2
        last_logits_ms[~mask] = 0.0
        prob_score_ms = last_logits_ms.max(dim=-1).values.mean(dim=1)
        prob_score_ms = prob_score_ms.detach().cpu().type(torch.float32).numpy().tolist()

        last_logits_en = torch.stack(output_en.scores, dim=1)
        m1 = (last_logits_en.argmax(dim=-1) < processor.tokenizer.vocab_size)
        m2 = (last_logits_en.argmax(dim=-1) != processor.tokenizer.pad_token_id)
        mask = m1 & m2
        last_logits_en[~mask] = 0.0
        prob_score_en = last_logits_en.max(dim=-1).values.mean(dim=1)
        prob_score_en = prob_score_en.detach().cpu().type(torch.float32).numpy().tolist()

        data = []
        for k in range(len(batch)):
            data.append(
                {
                    'predict_ms': processor.tokenizer.decode(output_ms.sequences[k]),
                    'predict_en': processor.tokenizer.decode(output_en.sequences[k]),
                    'score_ms': prob_score_ms[k],
                    'score_en': prob_score_en[k],
                }
            )
            filename = os.path.join(model_args.folder_output_audio, f'{global_rank}-{step}-{k}.mp3')
            sf.write(filename, batch[k], sr)

        filename = os.path.join(model_args.folder_output, f'{global_rank}-{step}.json')
        with open(filename, 'w') as fopen:
            json.dump(data, fopen)

        if accelerator.is_local_main_process:
            with open(step_file_temp, 'w') as fopen:
                json.dump(step, fopen)

            os.replace(step_file_temp, model_args.step_file)

    accelerator.wait_for_everyone()


if __name__ == "__main__":
    main()
