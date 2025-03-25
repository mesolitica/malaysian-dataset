from tqdm import tqdm
from multiprocess import Pool
import torch
import torchaudio
import pandas as pd
import click
import os
import json

device = 'cuda'

def chunks(l, devices, language, folder):
    chunk_size = len(l) // len(devices)
    remainder = len(l) % len(devices)
    start = 0
    for i in range(len(devices)):
        extra = 1 if i < remainder else 0
        end = start + chunk_size + extra
        yield (l[start:end], devices[i], language, folder)
        start = end

def loop(rows):
    rows, index, language, folder  = rows
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
        for row in tqdm(rows):
            t = row.get('pronunciation', '')
            if not len(t):
                t = row.get('question')
            f = row['audio_filename']
            new_f = f.replace('/', '_').replace('.mp3', '.json').replace('.wav', '.json')
            filename = os.path.join(folder, new_f)
            if os.path.exists(filename):
                continue
            new_wav, sr = torchaudio.load(f)
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
    
@click.command()
@click.option('--filename')
@click.option('--language', default = 'ms')
@click.option('--replication', default = 1)
@click.option('--folder', default = 'force_alignment')
def main(filename, language, replication, folder):
    os.makedirs(folder, exist_ok = True)
    devices = os.environ.get('CUDA_VISIBLE_DEVICES')
    if devices is None:
        devices = list(range(torch.cuda.device_count()))
    else:
        devices = [d.strip() for d in devices.split(',')]

    devices = replication * devices
    print(devices)

    with open(filename) as fopen:
        rows = json.load(fopen)

    df_split = chunks(rows, devices, language, folder)
    pool = Pool(len(devices))
    pooled = pool.map(loop, df_split)
    pool.close()
    pool.join()

if __name__ == '__main__':
    main()