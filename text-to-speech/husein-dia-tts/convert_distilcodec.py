import os
import soundfile as sf
import json
import click
import re
import pandas as pd
import librosa
from glob import glob
from functools import partial
from multiprocess import Pool
from huggingface_hub import hf_hub_download
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
    
    from distilcodec import DistilCodec, demo_for_generate_audio_codes
    import torchaudio
    import torch

    codec_model_config_path = hf_hub_download(repo_id="IDEA-Emdoor/DistilCodec-v1.0", filename='model_config.json')
    codec_ckpt_path = hf_hub_download(repo_id="IDEA-Emdoor/DistilCodec-v1.0", filename='g_00204000')

    codec = DistilCodec.from_pretrained(
        config_path=codec_model_config_path,
        model_path=codec_ckpt_path,
        use_generator=True,
        is_debug=False).eval()

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
            tokens = demo_for_generate_audio_codes(
                codec, 
                row['filename_audio'], 
                target_sr=24000, 
                plus_llm_offset=False
            )
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
    filtered = []
    for i in tqdm(indices):
        filename = os.path.join(folder, f'{i}.json')
        if os.path.exists(filename):
            try:
                with open(filename) as fopen:
                    json.load(fopen)
                continue
            except:
                pass
        filtered.append(i)

    df_split = list(chunks(filtered, devices))

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

    