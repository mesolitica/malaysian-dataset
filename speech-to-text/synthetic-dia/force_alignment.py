from tqdm import tqdm
from glob import glob
from multiprocess import Pool
import torch
import torchaudio
import pandas as pd
import click
import os
import json
import re

device = 'cuda'

pronunciation = {
    'A': 'ay', 'B': 'bee', 'C': 'see', 'D': 'dee', 'E': 'ee',
    'F': 'eff', 'G': 'ge', 'H': 'aitch', 'I': 'eye', 'J': 'jay',
    'K': 'kay', 'L': 'el', 'M': 'em', 'N': 'en', 'O': 'oh',
    'P': 'pee', 'Q': 'cue', 'R': 'ar', 'S': 'ess', 'T': 'tee',
    'U': 'you', 'V': 'vee', 'W': 'double you', 'X': 'ex', 'Y': 'why', 'Z': 'zee'
}

def replace_uppercase_sequences(text):
    pattern = re.compile(r'\b(?:[A-Z](?:[ \.,-]*[A-Z])*)\b')

    def repl(m):
        chunk = m.group()                   
        letters = re.findall(r'[A-Z]', chunk)
        return ' '.join(pronunciation[l] for l in letters)

    return pattern.sub(repl, text)

def chunks(l, devices, language, folder, column):
    chunk_size = len(l) // len(devices)
    remainder = len(l) % len(devices)
    start = 0
    for i in range(len(devices)):
        extra = 1 if i < remainder else 0
        end = start + chunk_size + extra
        yield (l[start:end], devices[i], language, folder, column)
        start = end
        
def new_f(folder, f):
    new_f = f.replace('/', '_').replace('.mp3', '.json').replace('.wav', '.json')
    filename = os.path.join(folder, new_f)
    return filename

def loop(rows):
    files, index, language, folder, column  = rows
    os.environ['CUDA_VISIBLE_DEVICES'] = str(index)

    from ctc_forced_aligner import (
        load_audio,
        load_alignment_model,
        generate_emissions,
        preprocess_text,
        get_alignments,
        get_spans,
        postprocess_results,
    )
    import torch

    alignment_model, alignment_tokenizer = load_alignment_model(
        device,
        dtype=torch.float16 if device == "cuda" else torch.float32,
    )

    with torch.no_grad():
        for f in tqdm(files):
            try:
                with open(f) as fopen:
                    row = json.load(fopen)
            except:
                continue
            
            if 'filename_audio' not in row:
                continue
                
            t = row.get(column, '')
            t = replace_uppercase_sequences(t)
            
            if len(t) < 2:
                continue
            
            filename_audio = row['filename_audio']
            if not os.path.exists(filename_audio):
                continue
            
            filename = new_f(folder, filename_audio)
            if os.path.exists(filename):
                continue
            
            try:
                new_wav, sr = torchaudio.load(filename_audio)
                audio_waveform = torchaudio.functional.resample(
                    new_wav[0], orig_freq=sr, new_freq=16000
                ).type(torch.float16).cuda()
                emissions, stride = generate_emissions(
                    alignment_model, audio_waveform, batch_size=1
                )
                tokens_starred, text_starred = preprocess_text(
                    t,
                    romanize=True,
                    language=language,
                )
                segments, scores, blank_token = get_alignments(
                    emissions,
                    tokens_starred,
                    alignment_tokenizer,
                )
                spans = get_spans(tokens_starred, segments, blank_token)
                word_timestamps = postprocess_results(text_starred, spans, stride, scores)
                with open(filename, 'w') as fopen:
                    row['word_timestamps'] = word_timestamps
                    json.dump(row, fopen)
            except Exception as e:
                print(e)
    
@click.command()
@click.option('--pattern')
@click.option('--rejected')
@click.option('--language', default = 'ms')
@click.option('--replication', default = 1)
@click.option('--folder', default = 'force_alignment')
@click.option('--column', default = 'normalized_generate_text')
def main(pattern, rejected, language, replication, folder, column):
    os.makedirs(folder, exist_ok = True)
    devices = os.environ.get('CUDA_VISIBLE_DEVICES')
    if devices is None:
        devices = list(range(torch.cuda.device_count()))
    else:
        devices = [d.strip() for d in devices.split(',')]

    devices = replication * devices
    print(devices)
    if rejected is not None:
        rejected = rejected.split(',')

    rows = glob(pattern)
    selected = []
    for f in tqdm(rows):
        if rejected is not None and any([r in f for r in rejected]):
            continue
        try:
            with open(f) as fopen:
                row = json.load(fopen)
        except:
            continue
            
        if 'filename_audio' not in row:
            continue
            
        t = row.get(column, '')
        
        filename_audio = row['filename_audio']
        if not os.path.exists(filename_audio):
            continue
        
        filename = new_f(folder, filename_audio)
        if os.path.exists(filename):
            continue
            
        selected.append(f)

    print(len(selected))
    df_split = chunks(selected, devices, language, folder, column)
    pool = Pool(len(devices))
    pooled = pool.map(loop, df_split)
    pool.close()
    pool.join()

if __name__ == '__main__':
    main()