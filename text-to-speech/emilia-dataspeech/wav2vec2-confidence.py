from transformers import AutoModelForCTC
import torch
import pandas as pd
from dataclasses import dataclass, asdict
from malaya_speech.utils.char import HF_CTC_VOCAB, HF_CTC_VOCAB_IDX
from malaya_speech.torch_model.huggingface import batching
from malaya_speech.utils.aligner import (
    merge_repeats,
    merge_words,
)
from datasets import Audio
import re
from tqdm import tqdm
from glob import glob
import torchaudio
import numpy as np
import click
import os

sr = 16000
audio = Audio(sampling_rate=sr)

def new_path(f):
    f = f.replace('.mp3', '.force')
    splitted = f.split('/')
    base_folder = splitted[0] + '_force'
    splitted = '/'.join([base_folder] + splitted[1:])
    return splitted

def get_trellis(emission, tokens, blank_id=0):
    num_frame = emission.size(0)
    num_tokens = len(tokens)

    # Trellis has extra diemsions for both time axis and tokens.
    # The extra dim for tokens represents <SoS> (start-of-sentence)
    # The extra dim for time axis is for simplification of the code.
    trellis = torch.empty((num_frame + 1, num_tokens + 1))
    trellis[0, 0] = 0
    trellis[1:, 0] = torch.cumsum(emission[:, 0], 0)
    trellis[0, -num_tokens:] = -float("inf")
    trellis[-num_tokens:, 0] = float("inf")

    for t in range(num_frame):
        trellis[t + 1, 1:] = torch.maximum(
            # Score for staying at the same token
            trellis[t, 1:] + emission[t, blank_id],
            # Score for changing to the next token
            trellis[t, :-1] + emission[t, tokens],
        )
    return trellis


@dataclass
class Point:
    token_index: int
    time_index: int
    score: float


def backtrack(trellis, emission, tokens, blank_id=0):
    # Note:
    # j and t are indices for trellis, which has extra dimensions
    # for time and tokens at the beginning.
    # When referring to time frame index `T` in trellis,
    # the corresponding index in emission is `T-1`.
    # Similarly, when referring to token index `J` in trellis,
    # the corresponding index in transcript is `J-1`.
    j = trellis.size(1) - 1
    t_start = torch.argmax(trellis[:, j]).item()

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
        prob = emission[t - 1, tokens[j - 1] if changed > stayed else 0].exp().item()
        # Return token index and time index in non-trellis coordinate.
        path.append(Point(j - 1, t - 1, prob))

        # 3. Update the token
        if changed > stayed:
            j -= 1
            if j == 0:
                break
    else:
        raise ValueError("Failed to align")
    return path[::-1]


@click.command()
@click.option("--path", help="files path in glob pattern")
@click.option("--global-index", default=1, help="global index")
@click.option("--local-index", default=0, help="local index")
def function(path, global_index, local_index):
    
    model = AutoModelForCTC.from_pretrained(
        'mesolitica/wav2vec2-xls-r-300m-mixed-v2',
        torch_dtype = torch.bfloat16)
    _ = model.cuda()

    df = pd.read_parquet(path).to_dict(orient = 'records')

    files = glob(path)
    filtered_files = []
    for f in df:
        new_f = new_path(f['audio_filename'])
        if os.path.exists(new_f) and os.path.getsize(new_f) > 2:
            continue
        filtered_files.append(f)

    global_size = len(filtered_files) // global_index
    filtered_files = filtered_files[global_size * local_index: global_size * (local_index + 1)]
    df = filtered_files

    with torch.no_grad():
        for i in tqdm(range(len(df))):
            transcription = ''.join([c for c in df[i]['transcription'].lower() if c in HF_CTC_VOCAB_IDX])
            transcription = re.sub(r'[ ]+', ' ', transcription).strip()
            tokens = [HF_CTC_VOCAB_IDX[c] for c in transcription]
            y = audio.decode_example(audio.encode_example(df[i]['audio_filename']))['array']
            normed_input_values, attentions = batching([y])
            normed_input_values = torch.tensor(normed_input_values).type(torch.bfloat16).cuda()
            attentions = torch.tensor(attentions).cuda()

            out = model(normed_input_values, attention_mask=attentions)
            logits = torch.nn.functional.log_softmax(out.logits, -1)
            o = logits[0].cpu()
            trellis = get_trellis(o, tokens, blank_id=len(HF_CTC_VOCAB))
            path = backtrack(trellis, o, tokens, blank_id=len(HF_CTC_VOCAB))
            segments = merge_repeats(path, transcription)
            word_segments = merge_words(segments)
            segments = [asdict(s) for s in segments]
            scores = [s['score'] for s in segments]
            
            df[i]['segments'] = segments
            df[i]['average_score'] = np.mean(scores)
            df[i]['logits_length'] = logits.shape[1]

            splitted = new_path(f)
                
            os.makedirs(os.path.split(splitted)[0], exist_ok = True)
            with open(splitted, 'w') as fopen:
                fopen.write(labels[no])

if __name__ == '__main__':
    function()