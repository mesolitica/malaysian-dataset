from ctc_forced_aligner import (
    load_audio,
    load_alignment_model,
    generate_emissions,
    preprocess_text,
    get_alignments,
    get_spans,
    postprocess_results,
)
from transformers import AutoTokenizer
from sklearn.feature_extraction.text import CountVectorizer
from glob import glob
from tqdm import tqdm
import torch
import torchaudio
import click
import os
import json

device = "cuda" if torch.cuda.is_available() else "cpu"
batch_size = 16

def new_path(f):
    _, extension = os.path.splitext(f)
    f = f.replace(extension, '.alignment')
    splitted = f.split('/')
    base_folder = splitted[0] + '_alignment'
    splitted = '/'.join([base_folder] + splitted[1:])
    return splitted

@click.command()
@click.option("--file", help="file")
@click.option("--global-index", default=1, help="global index")
@click.option("--local-index", default=0, help="local index")
@click.option("--batch-size", default=16, help="batch size")
def function(file, global_index, local_index, batch_size):

    files = []
    with open(file) as fopen:
        for no, l in enumerate(fopen):
            l = json.loads(l)
            l['index'] = os.path.join(file.replace('.jsonl', ''), f'{no}.mp3')
            files.append(l)
    
    print(len(files), files[0])
    filtered_files = []
    for f in files:
        new_f = new_path(f['index'])
        if os.path.exists(new_f) and os.path.getsize(new_f) > 2:
            continue
        filtered_files.append(f)

    global_size = len(filtered_files) // global_index
    files = filtered_files[global_size * local_index: global_size * (local_index + 1)]
    print(len(files))

    alignment_model, alignment_tokenizer = load_alignment_model(
        device,
        dtype=torch.float16 if device == "cuda" else torch.float32,
    )
    tokenizer = AutoTokenizer.from_pretrained('openai/whisper-large-v3')

    with torch.no_grad():
        for f in tqdm(files):
            splitted = tokenizer.decode(tokenizer(f['new_text'])['input_ids']).split('<|transcribe|>')
            t = splitted[1].split('<|endoftext|>')[0]
            language = splitted[0].split('<|startoftranscript|>')[-1][2:-2]
            
            try:
                new_wav, sr = torchaudio.load(f['audio_filename'])
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
                splitted = new_path(f['index'])
                os.makedirs(os.path.split(splitted)[0], exist_ok = True)
                with open(splitted, 'w') as fopen:
                    json.dump(word_timestamps, fopen)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    function()