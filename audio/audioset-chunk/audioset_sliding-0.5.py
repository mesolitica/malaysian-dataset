from transformers import AutoFeatureExtractor, AutoModelForAudioClassification
from collections import defaultdict
from tqdm import tqdm
from glob import glob
from datasets import Audio
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
import torch
import torchaudio
import numpy as np
import click
import os
import json
import numpy as np

def new_path(f):
    f = f.replace('.mp3', '.audioset-0.5')
    splitted = f.split('/')
    base_folder = splitted[0] + '_audioset-0.5'
    splitted = '/'.join([base_folder] + splitted[1:])
    return splitted


@click.command()
@click.option("--path", help="files path in glob pattern")
@click.option("--global-index", default=1, help="global index")
@click.option("--local-index", default=0, help="local index")
@click.option("--stride", default=0.5)
@click.option("--sliding", default=0.5)
@click.option("--model", default='MIT/ast-finetuned-audioset-10-10-0.4593')
def function(path, global_index, local_index, stride, sliding, model):

    feature_extractor = AutoFeatureExtractor.from_pretrained(model, return_attention_mask = True)
    model = AutoModelForAudioClassification.from_pretrained(model, torch_dtype = torch.float16).eval().cuda()
    id2label = model.config.id2label
    sr = feature_extractor.sampling_rate
    actual_stride = stride
    stride = int(stride * sr)
    sliding = int(sliding * sr)
    audio = Audio(sampling_rate = sr)

    files = glob(path)
    filtered_files = []
    for f in files:
        if '_audioset' in f:
            continue
        if os.path.getsize(f) < 10000:
            continue
        new_f = new_path(f)
        if os.path.exists(new_f) and os.path.getsize(new_f) > 2:
            continue
        filtered_files.append(f)

    global_size = len(filtered_files) // global_index
    filtered_files = filtered_files[global_size * local_index: global_size * (local_index + 1)]
    files = filtered_files

    class CustomDataset(Dataset):
        def __init__(self, files):
            self.files = files

        def __len__(self):
            return len(self.files)
        
        def __getitem__(self, index):
            f = self.files[index]
            try:
                y = audio.decode_example(audio.encode_example(f))['array']
            except Exception as e:
                print(e, f)
                os.remove(f)
                return None
            timestamps = []
            slided = []
            last_end = 0
            for i in range(0, len(y) - sliding + 1, stride):
                end = i + sliding
                slided.append(y[i: end])
                timestamps.append((i / sr, end / sr))
                last_end = end

            if last_end < len(y):
                y_ = y[last_end:]
                if len(y_) >= 2000:
                    slided.append(y_)
                    timestamps.append((last_end / sr, len(y) / sr))
            
            try:
                inputs = feature_extractor(slided, sampling_rate=sr, 
                                return_tensors="pt", return_attention_mask = True)
                return inputs, f, timestamps
            except Exception as e:
                print(e, f)

    dataset = CustomDataset(files)
    dataloader = DataLoader(dataset, batch_size = 1, shuffle = False, prefetch_factor=10, num_workers=5)

    with torch.no_grad():
        for row in tqdm(iter(dataloader)):
            try:
                inputs, f, timestamps_ = row
            except Exception as e:
                print(e)
                continue
            f = f[0]
            timestamps = []
            for t in timestamps_:
                timestamps.append((float(t[0]), float(t[1])))

            inputs['input_values'] = inputs['input_values'][0].to(torch.float16).cuda()
            logits = model(inputs['input_values']).logits.cpu().numpy()
            
            logits_per_timestamp = {str(t): logits[no] for no, (t, _) in enumerate(timestamps)}
            logits_accumulator = defaultdict(lambda: np.zeros(logits.shape[1]))
            count_accumulator = defaultdict(int)

            for (start, end) in timestamps:
                for t in np.arange(start, end, actual_stride):
                    t = str(round(t, 2))
                    logits_accumulator[t] += logits_per_timestamp[str(start)]
                    count_accumulator[t] += 1

            averaged_logits = {t: logits_accumulator[t] / count_accumulator[t] for t in logits_accumulator}
            for k in averaged_logits.keys():
                averaged_logits[k] = [round(v_, 5) for v_ in averaged_logits[k]]

            combined = []
            for k, v in averaged_logits.items():
                topk = np.array(v).argsort()[-5:][::-1]
                scores = [float(v[i]) for i in topk]
                topk = [id2label[i] for i in topk]
                combined.append({'timestamp': k, 'topk': topk, 'scores': scores})

            splitted = new_path(f)
            os.makedirs(os.path.split(splitted)[0], exist_ok = True)
            with open(splitted, 'w') as fopen:
                json.dump(combined, fopen)
            
if __name__ == '__main__':
    function()