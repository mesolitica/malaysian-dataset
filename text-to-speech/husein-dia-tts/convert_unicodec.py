import os
import soundfile as sf
import json
import click
import re
import pandas as pd
from glob import glob
from functools import partial
from multiprocess import Pool
from tqdm import tqdm

def chunks(l, devices):
    chunk_size = len(l) // len(devices)
    remainder = len(l) % len(devices)
    start = 0
    for i in range(len(devices)):
        extra = 1 if i < remainder else 0
        end = start + chunk_size + extra
        yield (l[start:end], devices[i])
        start = end

def loop(
    indices_device_pair,
    file,
    folder,
):
    indices, device = indices_device_pair
    os.environ['CUDA_VISIBLE_DEVICES'] = str(device)
    
    from encodec.utils import convert_audio
    from unicodec.decoder.pretrained import Unicodec
    import torchaudio
    import torch

    config = 'unicodec_frame75_10s_nq1_code16384_dim512_finetune.yaml'
    checkpoint = 'unicode.ckpt'
    model = Unicodec.from_pretrained0802(config, checkpoint).cuda()
    bandwidth_id = torch.tensor([0]).cuda()

    df = pd.read_parquet(file)
    for i in tqdm(indices):
        filename = os.path.join(folder, f'{i}.json')
        if os.path.exists(filename):
            try:
                with open(filename) as fopen:
                    json.load(fopen)
                continue
            except:
                pass

        try:
            row = df.iloc[i]
            wav, sr = torchaudio.load(row['filename_audio'])
            wav = convert_audio(wav, sr, 24000, 1).cuda()
            with torch.no_grad():
                _, discrete_code = model.encode_infer(wav, '2', bandwidth_id=bandwidth_id)
            tokens = discrete_code[0, 0].tolist()
            with open(filename, 'w') as fopen:
                json.dump(tokens, fopen)
        except Exception as e:
            print(e)

@click.command()
@click.option('--file')
@click.option('--folder')
@click.option('--replication', default = 1)
def main(
    file, 
    folder,
    replication,
):
    devices = os.environ.get('CUDA_VISIBLE_DEVICES')
    if devices is None:
        
        import torch
        devices = list(range(torch.cuda.device_count()))
    else:
        devices = [d.strip() for d in devices.split(',')]

    devices = replication * devices
    print(devices)

    os.makedirs(folder, exist_ok = True)
    transcription = pd.read_parquet(file)
    indices = list(range(0, len(transcription), 1))

    df_split = list(chunks(indices, devices))

    """
    def loop(
        indices_device_pair,
        file,
        folder,
    ):
    """

    loop_partial = partial(
        loop,
        file=file,
        folder=folder,
    )

    with Pool(len(devices)) as pool:
        pooled = pool.map(loop_partial, df_split)

if __name__ == '__main__':
    main()

    