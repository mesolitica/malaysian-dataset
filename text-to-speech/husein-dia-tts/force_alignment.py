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
import numpy as np

import librosa
import numpy as np
from dataclasses import dataclass

@dataclass
class Point:
    token_index: int
    time_index: int
    score: float


@dataclass
class Segment:
    label: str
    start: int
    end: int
    score: float

    def __repr__(self):
        return f"{self.label}\t({self.score:4.2f}): [{self.start:5d}, {self.end:5d})"

    @property
    def length(self):
        return self.end - self.start


def get_trellis(emission, tokens, blank_id=0):
    num_frame = emission.shape[0]
    num_tokens = len(tokens)

    trellis = np.full((num_frame + 1, num_tokens + 1), -float('inf'))
    trellis[:, 0] = 0
    for t in range(num_frame):
        trellis[t + 1, 1:] = np.maximum(
            trellis[t, 1:] + emission[t, blank_id],
            trellis[t, :-1] + emission[t, tokens],
        )
    return trellis


def backtrack(trellis, emission, tokens, blank_id=0):
    # Note:
    # j and t are indices for trellis, which has extra dimensions
    # for time and tokens at the beginning.
    # When referring to time frame index `T` in trellis,
    # the corresponding index in emission is `T-1`.
    # Similarly, when referring to token index `J` in trellis,
    # the corresponding index in transcript is `J-1`.
    j = trellis.shape[1] - 1
    t_start = np.argmax(trellis[:, j]).item()

    path = []
    for t in range(t_start, 0, -1):
        # 1. Figure out if the current position was stay or change
        # Note (again):
        # `emission[J-1]` is the emission at time frame `J` of trellis dimension.
        # Score for token staying the same from time frame J-1 to T.
        stayed = trellis[t - 1, j] + emission[t - 1, blank_id]
        # Score for token changing from C-1 at T-1 to J at T.
        changed = trellis[t - 1, j - 1] + emission[t - 1, tokens[j - 1]]

        # 2. Store the path with frame-wise probability.
        prob = np.exp(emission[t - 1, tokens[j - 1] if changed > stayed else 0]).item()
        # Return token index and time index in non-trellis coordinate.
        path.append(Point(j - 1, t - 1, prob))

        # 3. Update the token
        if changed > stayed:
            j -= 1
            if j == 0:
                break
    else:
        raise ValueError('Failed to align')
    return path[::-1]

def merge_repeats(path, transcript):
    i1, i2 = 0, 0
    segments = []
    while i1 < len(path):
        while i2 < len(path) and path[i1].token_index == path[i2].token_index:
            i2 += 1
        score = sum(path[k].score for k in range(i1, i2)) / (i2 - i1)
        segments.append(
            Segment(
                transcript[path[i1].token_index],
                path[i1].time_index,
                path[i2 - 1].time_index + 1,
                score,
            )
        )
        i1 = i2
    return segments

def merge_words(segments, separator='<star>'):
    words = []
    i1, i2 = 0, 0
    while i1 < len(segments):
        if i2 >= len(segments) or segments[i2].label == separator:
            if i1 != i2:
                segs = segments[i1:i2]
                word = "".join([seg.label for seg in segs])
                score = sum(seg.score * seg.length for seg in segs) / sum(seg.length for seg in segs)
                words.append(Segment(word, segments[i1].start, segments[i2].start, score))
            i1 = i2 + 1
            i2 = i1
        else:
            i2 += 1
    return words

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
        index = df.iloc[i]['index']
        filename = os.path.join(folder, f'{index}.json')

        try:
            with open(filename) as fopen:
                json.load(fopen)
            continue
        except:
            pass

        row = df.iloc[i]
        t = row['normalized_generate_text']
        
        new_wav, sr = librosa.load(row['filename_audio'], sr = 16000)
        audio_waveform = torch.tensor(new_wav).cuda()
        emissions, stride = generate_emissions(
            alignment_model, audio_waveform.to(torch.float16), batch_size=1
        )
        tokens_starred, text_starred = preprocess_text(
            t,
            romanize=True,
            language=language,
        )
        tokens_starred.append('<star>')
        text_starred.append('<star>')
        tokens = tokens_starred
        token_indices = [
            dictionary[c] for c in " ".join(tokens).split(" ") if c in dictionary
        ]
        o = emissions.cpu().numpy()
        trellis = get_trellis(o, token_indices)
        path = backtrack(trellis, o, token_indices)
        segments = merge_repeats(path, " ".join(tokens).split(" "))
        word_segments = merge_words(segments)
        text_starred_filtered = [t for t in text_starred if t != '<star>']
        words_alignment = []
        t = (len(new_wav) / sr) / o.shape[0]
        for no, s in enumerate(word_segments):
            words_alignment.append(
                {'text': text_starred_filtered[no],
                    'start': round(s.start * t, 3),
                    'end': round(s.end * t, 3),
                    'start_t': s.start,
                    'end_t': s.end,
                    'score': round(s.score, 3)}
            )

        with open(filename, 'w') as fopen:
            json.dump({'words_alignment': words_alignment, 'length': new_wav.shape[0] / sr}, fopen)

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

    