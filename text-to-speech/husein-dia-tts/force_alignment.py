import os
import soundfile as sf
import json
import click
import numpy as np
import pandas as pd
from functools import partial
from multiprocess import Pool
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
    language,
):
    indices, device = indices_device_pair
    os.environ['CUDA_VISIBLE_DEVICES'] = str(device)
    
    import torch

    torch.set_grad_enabled(False)

    import torchaudio
    from ctc_forced_aligner import (
        load_alignment_model,
        generate_emissions,
        preprocess_text,
        get_alignments,
    )
    device = 'cuda'
    alignment_model, alignment_tokenizer = load_alignment_model(
        device,
        dtype=torch.float16 if device == "cuda" else torch.float32,
    )
    tokenizer = alignment_tokenizer
    dictionary = tokenizer.get_vocab()
    dictionary = {k: v for k, v in dictionary.items()}
    dictionary_rev = {v: k for k, v in dictionary.items()}
    dictionary["<star>"] = len(dictionary)

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
        y, sr = sf.read(row['filename_audio'])
        new_wav = torch.from_numpy(y)
        audio_waveform = torchaudio.functional.resample(
            new_wav, orig_freq=44100, new_freq=16000
        ).type(torch.float16).cuda()
        emissions, stride = generate_emissions(
            alignment_model, audio_waveform, batch_size=1
        )
        tokens_starred, text_starred = preprocess_text(
            gen_text,
            romanize=True,
            language=language,
        )
        tokens_starred.append('<star>')
        text_starred.append('<star>')
        tokens = tokens_starred
        token_indices = [
            dictionary[c] for c in " ".join(tokens).split(" ") if c in dictionary
        ]
        alignments, scores = torchaudio.functional.forced_align(emissions[None].cpu(), torch.tensor([token_indices]))
        alignments, scores = alignments[0], scores[0]
        token_spans = torchaudio.functional.merge_tokens(alignments, scores)
        groups = []
        current_group = []

        for span in token_spans:
            current_group.append(span)
            if span.token == 31:
                groups.append(current_group)
                current_group = []

        if len(current_group):
            groups.append(current_group)

        merged = []
        for g in groups:
            temp, score = [], []
            if not isinstance(g, list):
                g = [g]
            if len(g) == 1 and g[0].token == 31:
                continue
            for g_ in g:
                if g_.token == 31:
                    continue
                score.append(g_.score)
                temp.append(dictionary_rev[g_.token])
            if len(temp):
                merged.append({
                    'text': ''.join(temp),
                    'start': g[0].start,
                    'end': g[-1].start + (g[-1].end - g[-1].start) // 2,
                    'score': np.mean(score)
                })

        text_nonstar = [w for w in text_starred if w != '<star>']
        alignment = []
        for i in range(len(merged)):
            alignment.append({
                'text': text_nonstar[i],
                'start': round((merged[i]['start'] * len(y) / emissions.shape[0]) / sr, 3),
                'end': round((merged[i]['end'] * len(y) / emissions.shape[0]) / sr, 3),
                'score': round(float(merged[i]['score']), 3)
            })
        with open(filename, 'w') as fopen:
            json.dump(alignment, fopen)

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
        pool.map(loop_partial, df_split)

if __name__ == '__main__':
    main()

    