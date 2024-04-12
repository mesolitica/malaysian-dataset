from accelerate import Accelerator, InitProcessGroupKwargs
from torch.utils.data import DataLoader, Dataset
from datetime import datetime
from datasets import Audio
from dataclasses import dataclass
from glob import glob
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

sr = 16000
chunks = 30
stride = chunks // 6


def sequence_1d(
    seq, maxlen=None, padding: str = 'post', pad_int=0.0, return_len=False
):
    if padding not in ['post', 'pre']:
        raise ValueError('padding only supported [`post`, `pre`]')

    if not maxlen:
        maxlen = max([len(s) for s in seq])

    padded_seqs, length = [], []
    for s in seq:
        if isinstance(s, np.ndarray):
            s = s.tolist()
        if padding == 'post':
            padded_seqs.append(s + [pad_int] * (maxlen - len(s)))
        if padding == 'pre':
            padded_seqs.append([pad_int] * (maxlen - len(s)) + s)
        length.append(len(s))
    if return_len:
        return np.array(padded_seqs), length
    return np.array(padded_seqs)


def collactor(rows):
    a, filename = [], []
    for row in rows:
        if row is None:
            continue
        a.append(row['array'])
        filename.append(row['filename'])
    return sequence_1d(a), filename


class Train(Dataset):
    def __init__(self):
        self.files = sorted(glob('split-nusantara/*.mp3'))
        self.audio = Audio(sampling_rate=16000)

    def __len__(self):
        return len(self.files)

    def __getitem__(self, item):
        try:
            y = self.audio.decode_example(self.audio.encode_example(self.files[item]))['array']
            return {'array': y, 'filename': self.files[item]}
        except Exception as e:
            print(e)


@dataclass
class ModelArguments:
    model_name_or_path: str = 'openai/whisper-large-v3'
    attn_type: str = 'flash_attn_2'
    folder_output: str = 'output-nusantara'
    batch_size: int = 8
    dataloader_num_workers: int = 1


def main():
    global_rank = int(os.environ['RANK'])
    parser = HfArgumentParser(ModelArguments)
    model_args = parser.parse_args_into_dataclasses()[0]
    print(global_rank, model_args)

    os.makedirs(model_args.folder_output, exist_ok=True)

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

    train = Train()
    dataloader = DataLoader(
        train,
        batch_size=model_args.batch_size,
        collate_fn=collactor,
        num_workers=model_args.dataloader_num_workers,
        pin_memory=True,
    )
    dataloader = accelerator.prepare(dataloader)

    start_step = 0
    steps = glob(os.path.join(model_args.folder_output, f'{global_rank}-*.json'))
    steps = [int(f.split('-')[1].replace('.json', '')) for f in steps]
    if len(steps):
        start_step = max(steps) + 1
        print(f'{global_rank}, continue from {start_step}')
    else:
        print(f'{global_rank}, failed to load last step count, continue from 0')

    dataloader = accelerator.skip_first_batches(dataloader, num_batches=start_step)
    batches = tqdm(dataloader, disable=not accelerator.is_local_main_process)

    for step, batch in enumerate(batches):
        step = step + start_step
        batch, filenames = batch
        p = processor(batch, return_tensors='pt', sampling_rate=sr, return_attention_mask=True)
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
                    'predict_ms': output_ms.sequences[k].tolist(),
                    'predict_en': output_en.sequences[k].tolist(),
                    'score_ms': prob_score_ms[k],
                    'score_en': prob_score_en[k],
                    'filename': filenames[k],
                }
            )

        filename = os.path.join(model_args.folder_output, f'{global_rank}-{step}.json')
        with open(filename, 'w') as fopen:
            json.dump(data, fopen)

    accelerator.wait_for_everyone()


if __name__ == "__main__":
    main()
