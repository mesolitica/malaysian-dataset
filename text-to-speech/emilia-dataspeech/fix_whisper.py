import pandas as pd
import json
import torch
import torchaudio
from tqdm import tqdm
from torchaudio.functional import resample
from transformers import pipeline
import click
import os
import json

torch_dtype = torch.bfloat16
device = 'cuda'

def new_path(f):
    f = f.replace('.mp3', '.whisper')
    splitted = f.split('/')
    base_folder = splitted[0] + '_whisper'
    splitted = '/'.join([base_folder] + splitted[1:])
    return splitted


@click.command()
@click.option("--file", help="file")
@click.option("--global-index", default=1, help="global index")
@click.option("--local-index", default=0, help="local index")
@click.option("--batch-size", default=8, help="batch size")
def function(file, global_index, local_index, batch_size):

    files = pd.read_parquet(file).to_dict(orient = 'records')
    for i in range(len(files)):
        files[i]['index'] = os.path.join(file.replace('.jsonl', ''), f'{i}.mp3')
    
    print(len(files), files[0])
    filtered_files = []
    for f in files:
        new_f = new_path(f['index'])
        if os.path.exists(new_f) and os.path.getsize(new_f) > 2:
            continue
        filtered_files.append(f)
    
    print(len(files), len(filtered_files))
    global_size = len(filtered_files) // global_index
    files = filtered_files[global_size * local_index: global_size * (local_index + 1)]
    print(len(files))

    asr_pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-large-v3-turbo",
        torch_dtype=torch.bfloat16,
        device=device,
    )

    with torch.no_grad():
        for i in tqdm(range(0, len(files), batch_size)):
            batch = files[i: i + batch_size]
            ys = []
            for f in batch:
                y, sr = torchaudio.load(f['audio'])
                y = y.mean(dim=0)
                y = resample(y, orig_freq=sr, new_freq=16000).numpy()
                ys.extend([y, y])
            
            languages = ['en', 'ms'] * len(batch)
            r_asr = asr_pipe(
                ys,
                chunk_length_s=30,
                batch_size=len(ys),
                generate_kwargs={"task": "transcribe", "language": languages},
                return_timestamps=False,
            )

            for no, f in enumerate(batch):
                splitted = new_path(f['index'])
                os.makedirs(os.path.split(splitted)[0], exist_ok = True)
                labels = r_asr[no * 2:(no + 1) * 2]
                with open(splitted, 'w') as fopen:
                    json.dump({'labels': labels, 'languages': ['en', 'ms']}, fopen)

if __name__ == '__main__':
    function()