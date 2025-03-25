from resemble_enhance.enhancer.inference import denoise, enhance
from tqdm import tqdm
from glob import glob
import torch
import torchaudio
import librosa
import soundfile as sf
import os
import click

@click.command()
@click.option("--path", help="files path in glob pattern")
@click.option("--global-index", default=1, help="global index")
@click.option("--local-index", default=0, help="local index")
def function(path, global_index, local_index):

    files = glob(path, recursive = True)
    global_size = len(files) // global_index
    files = files[global_size * local_index: global_size * (local_index + 1)]

    if torch.cuda.is_available():
        device = "cuda"
    else:
        device = "cpu"
        
    solver = 'Midpoint'.lower()
    nfe = int(64)
    lambd = 0.9
    tau = 0.5

    def process(path):
        f = os.path.split(path)[1]
        folder = os.path.split(path)[0]
        splitted = folder.split('/')
        base_folder = splitted[0]
        folder_44k = base_folder + '_44k'
        folder_24k = base_folder + '_24k'
        folder_44k = '/'.join([folder_44k] + splitted[1:])
        folder_24k = '/'.join([folder_24k] + splitted[1:])
        os.makedirs(folder_44k, exist_ok = True)
        os.makedirs(folder_24k, exist_ok = True)
        
        path_44k = os.path.join(folder_44k, f)
        path_24k = os.path.join(folder_24k, f)
        
        if os.path.exists(path_44k) and os.path.exists(path_24k) and os.path.getsize(path_44k) > 1000 and os.path.getsize(path_24k) > 1000:
            return
        
        with torch.no_grad():
            dwav, sr = torchaudio.load(path)
            dwav = dwav.mean(dim=0)

            wav2, new_sr = enhance(dwav, sr, device, nfe=nfe, solver=solver, lambd=lambd, tau=tau)

            wav2 = wav2.cpu().numpy()
            
        down = librosa.resample(y = wav2, orig_sr = new_sr, target_sr = 24000)
        
        sf.write(path_44k, wav2, new_sr)
        sf.write(path_24k, down, 24000)
        
        return path_44k, path_24k

    for f in tqdm(files):
        try:
            process(f)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    function()