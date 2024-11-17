from speechbrain.inference.classifiers import EncoderClassifier
from torch.utils.data import DataLoader
from torch.nn import functional as F
from tqdm import tqdm
from glob import glob
import torch
import torchaudio
import numpy as np
import click
import os

def new_path(f):
    f = f.replace('.mp3', '.lang')
    splitted = f.split('/')
    base_folder = splitted[0] + '_lang'
    splitted = '/'.join([base_folder] + splitted[1:])
    return splitted

class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, dataset, sampling_rate=16000, max_audio_len=5):
        self.dataset = dataset
        self.sampling_rate = sampling_rate
        self.max_audio_len = max_audio_len

    def __len__(self):
        return len(self.dataset)

    def _cutorpad(self, audio):
        effective_length = self.sampling_rate * self.max_audio_len
        len_audio = len(audio)

        if len_audio > effective_length:
            audio = audio[:effective_length]

        return audio

    def __getitem__(self, index):
        filepath = self.dataset[index]

        return {'file': filepath}

class CollateFunc:
    def __init__(self):
        pass

    def __call__(self, batch):
        files = []

        for audio in batch:
            files.append(audio['file'])

        return files


@click.command()
@click.option("--path", help="files path in glob pattern")
@click.option("--global-index", default=1, help="global index")
@click.option("--local-index", default=0, help="local index")
def function(path, global_index, local_index):

    language_id = EncoderClassifier.from_hparams(
        source="speechbrain/lang-id-voxlingua107-ecapa", 
        savedir="tmp",
        run_opts={"device":"cuda"},
    )

    files = glob(path)
    filtered_files = []
    for f in files:
        new_f = new_path(f)
        if os.path.exists(new_f) and os.path.getsize(new_f) > 2:
            continue
        filtered_files.append(f)

    global_size = len(filtered_files) // global_index
    filtered_files = filtered_files[global_size * local_index: global_size * (local_index + 1)]
        
    dataset = CustomDataset(filtered_files)
    data_collator = CollateFunc()

    dataloader = DataLoader(
        dataset=dataset,
        batch_size=16,
        collate_fn=data_collator,
        shuffle=False,
        num_workers=10
    )

    with torch.no_grad():
        for batch in tqdm(dataloader):
            files_ = batch
            signals = [language_id.load_audio(f) for f in b[-1]]
            max_length = max(tensor.size(0) for tensor in signals)
            padded_tensors = [
                F.pad(tensor, (0, max_length - tensor.size(0)), mode='constant', value=0)
                for tensor in signals
            ]
            result = torch.stack(padded_tensors)
            prediction = language_id.classify_batch(result)
            
            for no, f in enumerate(files_):
                splitted = new_path(f)
                
                os.makedirs(os.path.split(splitted)[0], exist_ok = True)
                with open(splitted, 'w') as fopen:
                    fopen.write(prediction[3][no])

if __name__ == '__main__':
    function()