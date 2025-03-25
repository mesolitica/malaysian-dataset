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
@click.option("--output_folder", default='output', help="output folder")
@click.option("--global-index", default=1, help="global index")
@click.option("--local-index", default=0, help="local index")
@click.option("--batch-size", default=16, help="batch size")
def function(file, output_folder, global_index, local_index, batch_size):

    os.makedirs(output_folder, exist_ok = True)
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

            new_f = file.replace('/', '_') + '.npy'
            path = os.path.join(output_folder, new_f)
            
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