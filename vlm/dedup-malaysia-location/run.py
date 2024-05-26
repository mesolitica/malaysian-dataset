from accelerate import Accelerator, InitProcessGroupKwargs
from torch.utils.data import DataLoader, Dataset
from io import BytesIO
from PIL import Image
from datetime import datetime
from dataclasses import dataclass
from glob import glob
import pandas as pd
import numpy as np
import torch
import json
import os
from datetime import timedelta
from tqdm import tqdm
from transformers import (
    HfArgumentParser,
    AutoProcessor,
    AutoModel
)

labels = ["scenery", "not scenery"]


def collactor(rows):
    a, filename, index = [], [], []
    for row in rows:
        a.append(row['array'].pixel_values)
        filename.append(row['filename'])
        index.append(row['chunk_index'])

    return {
        'pixel_values': torch.concat(a, 0),
        'input_ids': rows[0]['array']['input_ids'],
        'filename': filename,
        'index': index,
    }


class Train(Dataset):
    def __init__(self, indices, image_processor, maxlen_cache_df=5):
        self.indices = {}
        for k, v in indices.items():
            for i in range(int(k), v['start'] + v['end'], 1):
                self.indices[i] = v

        self.max_index = len(self.indices)
        self.cache_df = {}
        self.maxlen_cache_df = maxlen_cache_df
        self.image_processor = image_processor

    def __len__(self):
        return self.max_index

    def __getitem__(self, item):
        if item < 0:
            item = self.max_index + item

        v = self.indices[item]
        chunk_index = item - v['start']
        if v['filename'] not in self.cache_df:
            df = pd.read_parquet(v['filename'])
            if len(self.cache_df) >= self.maxlen_cache_df:
                keys = list(self.cache_df.keys())
                self.cache_df.pop(sorted(keys)[0], None)
            self.cache_df[v['filename']] = df
        else:
            df = self.cache_df[v['filename']]

        row = df.iloc[chunk_index]
        stream = BytesIO(row['image']['bytes'])
        image = Image.open(stream)
        i = image.convert('RGB')
        image_output = self.image_processor(
            text=labels,
            images=i, padding="max_length", return_tensors='pt'
        )
        return {
            'array': image_output,
            'filename': v['filename'],
            'chunk_index': chunk_index,
        }


@dataclass
class ModelArguments:
    model_name_or_path: str = 'google/siglip-base-patch16-512'
    indices_filename: 'str' = 'global_indices.json'
    folder_output: str = 'output-malaysia-location'
    folder_output_audio: str = 'output-malaysia-location'
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
    model = AutoModel.from_pretrained(model_args.model_name_or_path, torch_dtype=torch_dtype,)
    image_processor = AutoProcessor.from_pretrained(model_args.model_name_or_path)

    model.eval()
    _ = model.cuda()
    print(global_rank, model.dtype, model.device)

    with open(model_args.indices_filename) as fopen:
        global_indices = json.load(fopen)

    train = Train(global_indices, image_processor)
    dataloader = DataLoader(
        train,
        batch_size=model_args.batch_size,
        collate_fn=collactor,
        num_workers=model_args.dataloader_num_workers,
        pin_memory=True,
    )

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
        filename = batch.pop('filename')
        index = batch.pop('index')
        batch['pixel_values'] = batch['pixel_values'].to(model.device, dtype=torch_dtype)
        batch['input_ids'] = batch['input_ids'].to(model.device)
        with torch.no_grad():
            outputs = model(**batch)

        embedding = outputs.vision_model_output.pooler_output
        embedding = embedding.detach().cpu().type(torch.float32).numpy().tolist()
        logits_per_image = outputs.logits_per_image.argmax(-1).detach().cpu().numpy().tolist()

        data = []
        for k in range(len(filename)):
            data.append(
                {
                    'embedding': embedding[k],
                    'label': labels[logits_per_image[k]],
                    'filename': filename[k],
                    'index': index[k]
                }
            )

        filename = os.path.join(model_args.folder_output, f'{global_rank}-{step}.json')
        with open(filename, 'w') as fopen:
            json.dump(data, fopen)

    accelerator.wait_for_everyone()


if __name__ == "__main__":
    main()
