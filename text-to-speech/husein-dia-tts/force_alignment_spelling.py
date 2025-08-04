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
import time

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
    language,
):
    indices, device = indices_device_pair
    os.environ['CUDA_VISIBLE_DEVICES'] = str(device)
    
    import torch

    torch.set_grad_enabled(False)

    import torchaudio
    from ctc_forced_aligner import (
        load_audio,
        load_alignment_model,
        generate_emissions,
        preprocess_text,
        get_alignments,
        get_spans,
        postprocess_results,
    )
    device = 'cuda'
    alignment_model, alignment_tokenizer = load_alignment_model(
        device,
        dtype=torch.float16 if device == "cuda" else torch.float32,
    )

    df = pd.read_parquet(file)

    for i in tqdm(indices):
        filename = os.path.join(folder, f'{i}.json')

        try:
            with open(filename) as fopen:
                json.load(fopen)
            continue
        except:
            pass

        row = df.iloc[i]
        gen_text = row['normalized_generate_text']
        without_replace = re.sub(r'\b([A-Z])\s+([A-Z])\b', r'\1\2', gen_text)
        replace = replace_uppercase_sequences(without_replace)
        texts = [without_replace]
        if replace != without_replace:
            texts.append(replace)

        y, sr = sf.read(row['filename_audio'])
        new_wav = torch.from_numpy(y)
        audio_waveform = torchaudio.functional.resample(
            new_wav, orig_freq=44100, new_freq=16000
        ).type(torch.float16).cuda()
        emissions, stride = generate_emissions(
            alignment_model, audio_waveform, batch_size=1
        )

        word_timestamps = []
        for t in texts:
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
            word_timestamps.append(postprocess_results(text_starred, spans, stride, scores))

        if len(word_timestamps):
            with open(filename, 'w') as fopen:
                json.dump(word_timestamps, fopen)

@click.command()
@click.option('--file')
@click.option('--folder')
@click.option('--replication', default = 1)
@click.option('--language', default = 'ms')
def main(
    file, 
    folder,
    replication,
    language,
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

    loop_partial = partial(
        loop,
        file=file,
        folder=folder,
        language=language,
    )

    with Pool(len(devices)) as pool:
        pooled = pool.map(loop_partial, df_split)

if __name__ == '__main__':
    main()

    