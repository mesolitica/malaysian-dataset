import os

# os.environ["HF_ENDPOINT"] = "http://localhost:5564"
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"

from huggingface_hub import HfFileSystem
from tqdm import tqdm
from glob import glob
import os
import pandas as pd
import re
import polars as pl
import json
import mp
import time


def clean(string):
    string = re.sub('[^a-z ]+', ' ', string.lower())
    string = re.sub(r'[ ]+', ' ', string).strip()
    return string


keywords = {
    'malay', 'malaysia', 'melayu', 'bursa', 'ringgit'
}

os.system('mkdir output')


def loop(files):
    files, _ = files
    fs = HfFileSystem()
    for f in tqdm(files):
        f_only = '<>'.join(f.split('/')[-2:])
        f_only_new = f'output/{f_only}.jsonl'
        f_only_done = f'output/{f_only}.done'
        if os.path.exists(f_only_done):
            continue

        while True:
            try:
                try:
                    if not os.path.exists(f_only):
                        fs.get(f, f_only)
                    df = pl.read_parquet(f_only)
                except Exception as e:
                    print(e)
                    fs.get(f, f_only)
                    df = pl.read_parquet(f_only)
                break
            except Exception as e:
                print(e)
                time.sleep(1.0)

        with open(f_only_new, 'w') as fopen:
            for i in range(len(df)):
                row = df[i].to_dict(as_series=False)
                for k in row.keys():
                    row[k] = row[k][0]

                a = set(clean(row['text']).split()) & keywords
                if len(a):
                    fopen.write(f'{json.dumps(row, default=str)}\n')

        with open(f_only_done, 'w') as fopen:
            fopen.write('done')

        os.remove(f_only)
        del df


def main():
    fs = HfFileSystem()
    filename = 'files.json'
    if not os.path.exists(filename):
        files = fs.glob("datasets/HuggingFaceFW/fineweb/data/*/*")
        with open('files.json', 'w') as fopen:
            json.dump(files, fopen)

    with open(filename) as fopen:
        files = json.load(fopen)

    files = [f for f in files if f.endswith('.parquet')]
    files = sorted(files)

    done = set([os.path.split(f)[1].replace('.done', '') for f in glob('output/*.done')])
    not_yet = [f for f in files if '<>'.join(f.split('/')[-2:]) not in done]

    os.system('rm *.parquet')

    if len(not_yet):
        mp.multiprocessing(not_yet, loop, cores=min(len(not_yet), 120), returned=False)


if __name__ == "__main__":
    main()
