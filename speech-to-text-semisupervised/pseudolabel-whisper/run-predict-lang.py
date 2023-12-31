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
from speechbrain.pretrained import EncoderClassifier
from transformers import HfArgumentParser


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
    a = []
    files = []
    for row in rows:
        a.append(row['array'])
        files.append(row['path'])
    return {
        'array': sequence_1d(a),
        'files': files,
    }


class Train(Dataset):
    def __init__(self, files):
        self.files = files
        self.audio = Audio(sampling_rate=16000)

    def __len__(self):
        return len(self.files)

    def __getitem__(self, item):
        f = self.files[item]
        return self.audio.decode_example(self.audio.encode_example(f))


@dataclass
class ModelArguments:
    folder_output: str = 'output-predict-lang'
    batch_size: int = 8
    dataloader_num_workers: int = 1


def main():
    global_rank = int(os.environ['RANK'])
    parser = HfArgumentParser(ModelArguments)
    model_args = parser.parse_args_into_dataclasses()[0]
    print(global_rank, model_args)

    os.makedirs(model_args.folder_output, exist_ok=True)

    kwargs = InitProcessGroupKwargs(timeout=timedelta(seconds=7200))
    accelerator = Accelerator(
        kwargs_handlers=[kwargs],
    )

    model = EncoderClassifier.from_hparams(
        "speechbrain/lang-id-voxlingua107-ecapa", run_opts={"device": "cuda"})

    files = sorted(glob('output-audio/*.mp3'))
    train = Train(files)

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
    steps = [int(f.split('-')[-1].replace('.json', '')) for f in steps]
    if len(steps):
        start_step = max(steps) + 1
        print(f'{global_rank}, continue from {start_step}')
    else:
        print(f'{global_rank}, failed to load last step count, continue from 0')

    dataloader = accelerator.skip_first_batches(dataloader, num_batches=start_step)
    batches = tqdm(dataloader, disable=not accelerator.is_local_main_process)

    for step, batch in enumerate(batches):
        step = step + start_step

        padded = batch['array']
        padded_pt = torch.tensor(padded)
        padded_pt = padded_pt.to(model.device)
        predicted = model.classify_batch(padded_pt)[3]

        files = {}
        for no, f in enumerate(batch['files']):
            files[f] = predicted[no]

        filename = os.path.join(model_args.folder_output, f'{global_rank}-{step}.json')
        with open(filename, 'w') as fopen:
            json.dump(files, fopen)

    accelerator.wait_for_everyone()


if __name__ == "__main__":
    main()
