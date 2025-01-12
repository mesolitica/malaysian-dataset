from transformers import (
    AutoProcessor,
    AutoModelForSpeechSeq2Seq
)
from torch.utils.data import DataLoader
from torch.nn import functional as F
from tqdm import tqdm
from glob import glob
import torch
import torchaudio
import numpy as np
import click
import os
import json
from datasets import Audio

sr = 16000
audio = Audio(sampling_rate=sr)
dtype = torch.bfloat16
device = 'cuda'

def new_path(f):
    f = f.replace('.mp3', '.language')
    splitted = f.split('/')
    base_folder = splitted[0] + '_language'
    splitted = '/'.join([base_folder] + splitted[1:])
    return splitted

def get_language(model, inputs, rev_vocab):
    labels = torch.tensor([[rev_vocab['<|startoftranscript|>']]], device=device)
    labels = labels.repeat((inputs.shape[0], 1))
    with torch.no_grad():
        out_encoder = model.model.encoder(inputs)
        out_decoder = model.model.decoder(labels, encoder_hidden_states=out_encoder[0], use_cache = False, past_key_values = None)
        proj = model.proj_out(out_decoder.last_hidden_state[:, -1:])
        proj = proj[:,-1]
        return torch.nn.functional.softmax(proj, dim = -1)

@click.command()
@click.option("--path", help="files path in glob pattern")
@click.option("--global-index", default=1, help="global index")
@click.option("--local-index", default=0, help="local index")
@click.option("--batch-size", default=16, help="batch size")
def function(path, global_index, local_index, batch_size):

    files = glob(path)
    print(len(files))
    filtered_files = []
    for f in files:
        new_f = new_path(f)
        if os.path.exists(new_f) and os.path.getsize(new_f) > 2:
            continue
        filtered_files.append(f)

    global_size = len(filtered_files) // global_index
    files = filtered_files[global_size * local_index: global_size * (local_index + 1)]
    print(len(files))
    
    processor = AutoProcessor.from_pretrained('openai/whisper-large-v3')
    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        'openai/whisper-large-v3',
        torch_dtype=dtype,
    ).to(device)

    rev_vocab = processor.tokenizer.get_vocab()
    vocab = {v: k for k, v in rev_vocab.items()}
    
    with torch.no_grad():
        for i in tqdm(range(0, len(files), batch_size)):
            batch_files = files[i: i + batch_size]
            y = [audio.decode_example(audio.encode_example(f))['array'] for f in batch_files]
            batch = processor(
                y,
                return_tensors='pt',
                sampling_rate=processor.feature_extractor.sampling_rate,
                device = 'cuda',
            ).to('cuda')
            batch['input_features'] = batch['input_features'].type(dtype)
            proj = get_language(model, batch['input_features'], rev_vocab)
            probs = proj.amax(-1).tolist()
            argmax = proj.argmax(-1)
            langs = [vocab[a.tolist()][2:-2] for a in argmax]
            
            for no, f in enumerate(batch_files):
                splitted = new_path(f)
                os.makedirs(os.path.split(splitted)[0], exist_ok = True)
                with open(splitted, 'w') as fopen:
                    json.dump({'label': langs[no], 'prob': probs[no]}, fopen)

if __name__ == '__main__':
    function()