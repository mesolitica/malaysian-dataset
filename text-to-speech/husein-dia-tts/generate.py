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

def chunks(l, devices):
    chunk_size = len(l) // len(devices)
    remainder = len(l) % len(devices)
    start = 0
    for i in range(len(devices)):
        extra = 1 if i < remainder else 0
        end = start + chunk_size + extra
        yield (l[start:end], devices[i])
        start = end

def fix_spacing(text):
    
    quote_pattern = r'"([^"]*)"'
    def fix_quotes(match):
        content = match.group(1).strip()
        return f'"{content}"'
    
    text = re.sub(quote_pattern, fix_quotes, text)
    paren_pattern = r'\(([^)]*)\)'
    
    def fix_parens(match):
        content = match.group(1).strip()
        return f'({content})'
    text = re.sub(paren_pattern, fix_parens, text)
    
    punct_pattern = r'\s+([,.?])'
    text = re.sub(punct_pattern, r'\1', text)
    
    return text

def loop(
    indices_device_pair,
    file,
    folder,
    reference_audio,
    reference_text,
    model,
    temperature,
    repeat,
):
    indices, device = indices_device_pair
    os.environ['CUDA_VISIBLE_DEVICES'] = str(device)
    
    import torch
    import malaya
    from dia.model import Dia
    
    normalizer = malaya.normalize.normalizer()
    model = Dia.from_pretrained("mesolitica/Malaysian-Podcast-Dia-1.6B", compute_dtype="float16")

    df = pd.read_parquet(file)
    for i in tqdm(indices):
        filename = os.path.join(folder, f'{i}.json')
        try:
            with open(filename) as fopen:
                json.load(fopen)
            continue
        except:
            pass

        t = df['text'].iloc[i]
        t = t.strip().replace('...', ', ')
        t = re.sub(r'(?<=\S)/(?=\S)', ' ', t).strip()
        string = normalizer.normalize(t, normalize_hingga = False, normalize_text = True, normalize_word_rules = False, normalize_time = True, normalize_cardinal = True)
        t_ = string['normalize']
        if '--' in t_:
            continue
        if '~' in t_:
            continue
        
        t_ = fix_spacing(t_)
        text = '[S1] ' + reference_text + '[S1] ' + t_.strip() + '. '
        texts = [text] * repeat
        clone_from_audios = [reference_audio] * len(texts)

        output = model.generate(
            texts, 
            audio_prompt=clone_from_audios, 
            use_torch_compile=True, verbose=False, 
            max_tokens=2000, temperature = temperature
        )

        filename_audios = []
        for k in range(repeat):
            try:
                filename_audio = os.path.join(folder, f'{i}-{k}.mp3')
                sf.write(filename_audio, output[k], 44100)
                filename_audios.append(filename_audio)
            except Exception as e:
                print('exception', e)
        
        if len(filename_audios):
            d = {
                'reference_text': reference_text,
                'generate_text': t,
                'normalized_generate_text': t_,
                'reference_audio': reference_audio,
                'filename_audios': filename_audios,
            }
            with open(filename, 'w') as fopen:
                json.dump(d, fopen)

@click.command()
@click.option('--file')
@click.option('--folder')
@click.option('--reference_audio')
@click.option('--reference_text')
@click.option('--model', default = 'mesolitica/Malaysian-Podcast-Dia-1.6B')
@click.option('--temperature', default = 0.8)
@click.option('--repeat', default = 5)
@click.option('--replication', default = 1)
def main(
    file, 
    folder,
    reference_audio,
    reference_text,
    model, 
    temperature, 
    repeat,
    replication,
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

    df_split = list(chunks(indices, devices))

    """
    def loop(
        indices_device_pair,
        file,
        folder,
        reference_audio,
        reference_text,
        model,
        temperature,
        repeat,
    ):
    """

    loop_partial = partial(
        loop,
        file=file,
        folder=folder,
        reference_audio=reference_audio,
        reference_text=reference_text,
        model=model,
        temperature=temperature,
        repeat=repeat,
    )

    with Pool(len(devices)) as pool:
        pooled = pool.map(loop_partial, df_split)

if __name__ == '__main__':
    main()

    