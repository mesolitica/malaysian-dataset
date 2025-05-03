from multiprocess import Pool
from tqdm import tqdm
from functools import partial
from multiprocess import Pool
from datasets import Audio
import click
import os
import json
import pandas as pd

def chunks(l, devices):
    chunk_size = len(l) // len(devices)
    remainder = len(l) % len(devices)
    start = 0
    for i in range(len(devices)):
        extra = 1 if i < remainder else 0
        end = start + chunk_size + extra
        yield (l[start:end], devices[i])
        start = end

def new_path(f, folder):
    f_only = os.path.split(f)[1]
    new_f = os.path.join(folder, f_only)
    return new_f.replace('.mp3', '.json')

def loop(
    files_device_pair, 
    folder,
    model_name,
):
    files, device = files_device_pair

    os.environ['CUDA_VISIBLE_DEVICES'] = str(device)

    import torch
    from transformers.models.whisper import tokenization_whisper

    tokenization_whisper.TASK_IDS = ["translate", "transcribe", 'transcribeprecise', 'transcribenonverbal']

    from datasets import Audio
    from transformers import WhisperForConditionalGeneration, WhisperFeatureExtractor, WhisperProcessor

    torch.set_grad_enabled(False)

    audio = Audio(sampling_rate=16000)

    model = WhisperForConditionalGeneration.from_pretrained(
    model_name, torch_dtype=torch.float16)
    model.eval()
    _ = model.cuda()
    processor = WhisperProcessor.from_pretrained(model_name)
    tokenizer = processor.tokenizer

    for f in tqdm(files):
        y = audio.decode_example(audio.encode_example(f))['array']
        p = processor([y], return_tensors='pt')
        p['input_features'] = p['input_features'].to(torch.float16)
        r = model.generate(
            p['input_features'].cuda(),
            repetition_penalty = 1.05,
            output_scores=True,
            return_dict_in_generate=True,
            return_timestamps=True, task = 'transcribenonverbal')
        t = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(r['sequences'][0]))
        new_f = new_path(f, folder)
        with open(new_f, 'w') as fopen:
            json.dump(t, fopen)

@click.command()
@click.option('--file')
@click.option('--folder')
@click.option('--model_name', default ='mesolitica/malaysian-whisper-large-v3-turbo-v3-nonverbal')
@click.option('--replication', default = 1)
def main(
    file,
    folder,
    model_name,
    replication,
):
    devices = os.environ.get('CUDA_VISIBLE_DEVICES')
    if devices is None:
        devices = list(range(torch.cuda.device_count()))
    else:
        devices = [d.strip() for d in devices.split(',')]

    devices = replication * devices
    print(devices)

    os.makedirs(folder, exist_ok = True)

    audio_filename = pd.read_parquet(file)['audio'].tolist()
    print('before', len(audio_filename))
    audio_filename = [f for f in audio_filename if not os.path.exists(new_path(f, folder))]
    print('after', len(audio_filename))

    files_device_pair = list(chunks(audio_filename, devices))
    loop_partial = partial(
        loop,
        folder=folder,
        model_name=model_name,
    )

    with Pool(len(devices)) as pool:
        pooled = pool.map(loop_partial, files_device_pair)

if __name__ == '__main__':
    main()
