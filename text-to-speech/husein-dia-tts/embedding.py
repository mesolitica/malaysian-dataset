import click
import json
import pandas as pd
import torch
import numpy as np
from tqdm import tqdm
from multiprocess import Pool
import os

def chunks(l, devices, folder):
    chunk_size = len(l) // len(devices)
    remainder = len(l) % len(devices)
    start = 0
    for i in range(len(devices)):
        extra = 1 if i < remainder else 0
        end = start + chunk_size + extra
        yield (l[start:end], devices[i], folder)
        start = end

def loop(rows):
    rows, index, folder = rows
    os.environ['CUDA_VISIBLE_DEVICES'] = str(index)

    import torch
    import torchaudio
    import malaya_speech

    model = malaya_speech.speaker_vector.nemo('huseinzol05/nemo-titanet_large').cuda()
    _ = model.eval()
    with torch.no_grad():
        for row in tqdm(rows, desc = f'loop {index}'):
            no, row = row
            new_f = os.path.join(folder, f'{no}.npy')
            if os.path.exists(new_f):
                continue
            e = model([malaya_speech.load(row['audio'])[0]])
            np.save(new_f, e[0], allow_pickle=True)

@click.command()
@click.option('--filename')
@click.option('--replication', default = 1)
@click.option('--folder', default = 'embedding')
def main(filename, replication, folder):
    os.makedirs(folder, exist_ok = True)
    devices = os.environ.get('CUDA_VISIBLE_DEVICES')
    if devices is None:
        devices = list(range(torch.cuda.device_count()))
    else:
        devices = [d.strip() for d in devices.split(',')]

    devices = replication * devices
    print(devices)

    rows = pd.read_parquet(filename).to_dict(orient = 'records')
    rows = [(i, rows[i]) for i in range(len(rows))]
    df_split = chunks(rows, devices, folder)
    pool = Pool(len(devices))
    pooled = pool.map(loop, df_split)
    pool.close()
    pool.join()

if __name__ == '__main__':
    main()


