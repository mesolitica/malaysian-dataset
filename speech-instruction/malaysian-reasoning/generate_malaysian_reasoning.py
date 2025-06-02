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

rejected = {'eh', 'erm'}
good_ratio = 7 / len('Untuk bertanyakan jumlah atau bilangan. . Aee . apa . Bee . siapa . See . bila . Dee . berapa .')

def clean(string):
    string = re.sub('[^A-Za-z ]+', ' ', string)
    string = re.sub(r'[ ]+', ' ', string.lower()).strip()
    return string

def chunks(l, devices):
    chunk_size = len(l) // len(devices)
    remainder = len(l) % len(devices)
    start = 0
    for i in range(len(devices)):
        extra = 1 if i < remainder else 0
        end = start + chunk_size + extra
        yield (l[start:end], devices[i])
        start = end

replace = {
    'Aee .': 'A.',
    'Bee .': 'B.',
    'See .': 'C.',
    'Dee .': 'D.',
    'Eee .': 'E.',
    ' .': '.',
    '(': '',
    ')': '',
}

rejected = ['frac{', '\math', 'sqrt', '+']

replace_pronunciation = {
    'A.': 'Eay .',
    'B.': 'Bee .',
    'C.': 'See .',
    'D.': 'Dee .',
    'E.': 'Eee .',
}

def loop(
    indices_device_pair,
    file,
    folder,
    model,
    temperature,
    cfg_scale,
    threshold,
    repeat,
    language,
):
    indices, device = indices_device_pair
    os.environ['CUDA_VISIBLE_DEVICES'] = str(device)
    
    import torch

    torch.set_grad_enabled(False)

    import torchaudio
    import malaya
    from dia.model import Dia
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
    
    model = Dia.from_pretrained(model, compute_dtype="float16")
    
    rows = pd.read_parquet(file).to_dict(orient = 'records')
    for i in tqdm(indices):
        filename = os.path.join(folder, f'{i}.json')

        speaker = rows[i]['new_audio_filename']
        t = rows[i]['speaker']['transcription']
        clone_from_text = f"[S1] {t}"
        clone_from_audio = speaker
        t_ = rows[i]['question'][1]['pronunciation']

        if any([r in t_ for r in rejected]):
            d = {
                'error': 'rejected',
            }
            with open(filename, 'w') as fopen:
                json.dump(d, fopen)
            continue

        for k, v in replace.items():
            t_ = t_.replace(k, v)
        text = clone_from_text + '[S1] ' + t_.strip()
        texts = [text]
        clone_from_audios = [clone_from_audio] * len(texts)
        ratio = len(rows[i]['question'][1]['pronunciation']) * good_ratio

        gen_text = rows[i]['question'][1]['pronunciation']
        for k, v in replace_pronunciation.items():
            gen_text = gen_text.replace(k, v)

        success = False
        for _ in range(repeat):
        
            try:
                output = model.generate(
                    texts, 
                    audio_prompt=clone_from_audios, 
                    use_torch_compile=True, 
                    verbose=True, 
                    max_tokens=3000, 
                    temperature=temperature,
                    cfg_scale=cfg_scale,
                )
            except Exception as e:
                print('EXCEPTION', e)
                with open(filename, 'w') as fopen:
                    d = {'error': str(e)}
                    json.dump(d, fopen)
                lower = str(e).lower()
                if 'compile' in lower or 'memory' in lower:
                    raise Exception(e)
                else:
                    continue

            len_audio = len(output) / 44100
            print(len_audio, ratio)
            if len_audio > (ratio + 5):
                continue
            
            if len_audio < (ratio - 5):
                continue
                
            try:
                new_wav = torch.tensor(output)
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
                segments, scores, blank_token = get_alignments(
                    emissions,
                    tokens_starred,
                    alignment_tokenizer,
                )
                spans = get_spans(tokens_starred, segments, blank_token)
                word_timestamps = postprocess_results(text_starred, spans, stride, scores)
                print(word_timestamps)
                scores = [w['score'] for w in word_timestamps if w['score'] <= threshold]

                if len(scores):
                    continue
            except Exception as e:
                print(e)
                continue

            filename_audio = filename.replace('.json', '.mp3')
            sf.write(filename_audio, output, 44100)

            d = {
                'filename_audio': filename_audio,
            }
            with open(filename, 'w') as fopen:
                json.dump(d, fopen)
            success = True
            break
        
        if not success:
            d = {
                'error': 'fail',
            }
            with open(filename, 'w') as fopen:
                json.dump(d, fopen)
    
    raise Exception('done')

@click.command()
@click.option('--file')
@click.option('--folder')
@click.option('--model', default = 'mesolitica/Malaysian-Dia-1.6B')
@click.option('--temperature', default = 1.0)
@click.option('--cfg_scale', default = 1.0)
@click.option('--replication', default = 1)
@click.option('--threshold', default = -14.5)
@click.option('--repeat', default = 5)
@click.option('--language', default = 'ms')
def main(
    file, 
    folder,
    model, 
    temperature, 
    cfg_scale,
    replication,
    threshold,
    repeat,
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
    rows = pd.read_parquet(file)
    indices = list(range(0, len(rows), 1))
    indices = [i for i in indices if not os.path.exists(os.path.join(folder, f'{i}.json'))]
    print(len(indices))

    df_split = list(chunks(indices, devices))

    loop_partial = partial(
        loop,
        file=file,
        folder=folder,
        model=model,
        temperature=temperature,
        cfg_scale=cfg_scale,
        threshold=threshold,
        repeat=repeat,
        language=language,
    )

    with Pool(len(devices)) as pool:
        pooled = pool.map(loop_partial, df_split)

if __name__ == '__main__':
    main()

    