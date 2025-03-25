from transformers import AutoFeatureExtractor, AutoModelForAudioClassification
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
    f = f.replace('.mp3', '.emotion')
    splitted = f.split('/')
    base_folder = splitted[0] + '_emotion'
    splitted = '/'.join([base_folder] + splitted[1:])
    return splitted

def preprocess_audio(audio_path, feature_extractor, max_duration=30.0):
    audio_array, sampling_rate = librosa.load(audio_path, sr=feature_extractor.sampling_rate)
    
    max_length = int(feature_extractor.sampling_rate * max_duration)
    if len(audio_array) > max_length:
        audio_array = audio_array[:max_length]
    else:
        audio_array = np.pad(audio_array, (0, max_length - len(audio_array)))

    inputs = feature_extractor(
        audio_array,
        sampling_rate=feature_extractor.sampling_rate,
        max_length=max_length,
        truncation=True,
        return_attention_mask=True,
        return_tensors="pt",
    )
    return inputs


@click.command()
@click.option("--path", help="files path in glob pattern")
@click.option("--global-index", default=1, help="global index")
@click.option("--local-index", default=0, help="local index")
def function(path, global_index, local_index):
    
    model = 'firdhokk/speech-emotion-recognition-with-facebook-wav2vec2-large-xlsr-53'
    
    feature_extractor = AutoFeatureExtractor.from_pretrained(model, do_normalize=True, return_attention_mask=True)
    model = AutoModelForAudioClassification.from_pretrained(model).eval().cuda()
    id2label = model.config.id2label

    files = glob(path)
    filtered_files = []
    for f in files:
        new_f = new_path(f)
        if os.path.exists(new_f) and os.path.getsize(new_f) > 2:
            continue
        filtered_files.append(f)

    global_size = len(filtered_files) // global_index
    filtered_files = filtered_files[global_size * local_index: global_size * (local_index + 1)]

    with torch.no_grad():
        for i in tqdm(range(0, len(files), batch_size)):
            batch_files = files[i: i + batch_size]
            
        for batch in tqdm(dataloader):
            batch, files_ = batch
            input_values = batch['input_values'].type(dtype).to(device)

            logits = model(input_values).logits
            scores = F.softmax(logits, dim=-1)
            
            labels = [label_mapping[i] for i in torch.argmax(scores, dim=1).cpu().detach().numpy()]
            
            for no, f in enumerate(files_):
                splitted = new_path(f)
                
                os.makedirs(os.path.split(splitted)[0], exist_ok = True)
                with open(splitted, 'w') as fopen:
                    fopen.write(labels[no])

if __name__ == '__main__':
    function()