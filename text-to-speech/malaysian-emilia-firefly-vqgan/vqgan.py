from dynamicbatch_ttspipeline.fishspeech.load import load_vqgan
from tqdm import tqdm
from glob import glob
import torch
import torchaudio
import numpy as np
import os
import click
import pandas as pd

@click.command()
@click.option("--file", default='verify-text.parquet', help="file")
@click.option("--global-index", default=1, help="global index")
@click.option("--local-index", default=0, help="local index")
@click.option("--batch-size", default=16, help="batch size")
def function(file, global_index, local_index, batch_size):

    df = pd.read_parquet(file)
    files = df['audio'].tolist()
    global_size = len(files) // global_index
    files = files[global_size * local_index: global_size * (local_index + 1)]
    model = load_vqgan(device = 'cuda')

    for i in tqdm(range(0, len(files), batch_size)):
        batch = files[i: i + batch_size]
        
        wavs = []
        audio_lengths = []
        paths = []
        max_length = 0
        for file in batch:

            f = os.path.split(file)[1]
            new_f = os.path.splitext(f)[0] + '.npy'
            folder = os.path.split(file)[0]
            splitted = folder.split('/')
            base_folder = splitted[0]
            folder = base_folder + '_vqgan'
            folder = '/'.join([folder] + splitted[1:])
            os.makedirs(folder, exist_ok = True)
            
            path = os.path.join(folder, new_f)
            
            if os.path.exists(path) and os.path.getsize(path) > 1000:
                continue
     
            try:
                wav, sr = torchaudio.load(file)
            except Exception as e:
                print(e)
                continue
            
            if wav.shape[0] > 1:
                wav = wav.mean(dim=0, keepdim=True)
            wav = torchaudio.functional.resample(
                wav.cuda(), sr, model.spec_transform.sample_rate
            )[0]
            max_length = max(max_length, len(wav))
            wavs.append(wav)
            audio_lengths.append(len(wav))
            paths.append(path)

        if not len(wavs):
            continue
        
        for i in range(len(wavs)):
            wavs[i] = torch.nn.functional.pad(wavs[i], (0, max_length - len(wavs[i])), "constant")
        
        with torch.no_grad():
            audios = torch.stack(wavs, dim=0)[:, None]
            audio_lengths = torch.tensor(audio_lengths, device=model.device, dtype=torch.long)
            indices, feature_lengths = model.encode(audios, audio_lengths)
            outputs = indices.cpu().numpy()
            features = [feature[:, :feature_lengths[i]].T.flatten() for i, feature in enumerate(outputs)]

        for i in range(len(features)):
            np.save(paths[i], features[i])

if __name__ == '__main__':
    function()