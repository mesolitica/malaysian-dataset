import os

# os.environ["HF_ENDPOINT"] = "http://localhost:5564"
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"

from huggingface_hub import HfFileSystem
from tqdm import tqdm
from glob import glob
import os
import re
import polars as pl
import json
import mp


def clean(string):
    string = re.sub('[^a-z ]+', ' ', string.lower())
    string = re.sub(r'[ ]+', ' ', string).strip()
    return string


keywords = {
    'malay', 'malaysia', 'melayu', 'bursa', 'ringgit'
}

os.system('mkdir fineweb-edu-dedup')


def loop(files):
    files, _ = files
    fs = HfFileSystem()
    for f in files:
        f_only = os.path.join('fineweb-edu-dedup', os.path.split(f)[1])
        f_only_new = f'{f_only}.jsonl'
        f_only_done = f'{f_only}.done'
        if os.path.exists(f_only_done):
            continue

        try:
            if not os.path.exists(f_only):
                fs.get(f, f_only)
            df = pl.read_parquet(f_only)
        except BaseException:
            fs.get(f, f_only)
            df = pl.read_parquet(f_only)

        with open(f_only_new, 'w') as fopen:
            for i in tqdm(range(len(df))):
                try:
                    row = df[i, :2].to_dict(as_series=False)
                    for k in row.keys():
                        row[k] = row[k][0]

                    a = set(clean(row['text']).split()) & keywords
                    if len(a):
                        fopen.write(f'{json.dumps(row)}\n')
                        fopen.flush()
                except BaseException:
                    pass

        with open(f_only_done, 'w') as fopen:
            fopen.write('done')

        os.remove(f_only)
        del df


def main():
    fs = HfFileSystem()
    files = fs.ls("datasets/HuggingFaceTB/smollm-corpus/fineweb-edu-dedup", detail=False)
    files = sorted(files)
    mp.multiprocessing(files, loop, cores=50, returned=False)


if __name__ == "__main__":
    main()
