import json
import os
import polars
import mp
from glob import glob
from tqdm import tqdm
from collections import defaultdict


def loop(files):
    files, _ = files
    for f in tqdm(files):
        folder, file = os.path.split(f)[1].split('<>')
        folder = os.path.join('data', folder)
        os.makedirs(folder, exist_ok=True)
        file = file.replace('.jsonl', '')
        file = os.path.join(folder, file)

        if os.path.exists(file):
            continue

        d = defaultdict(list)
        with open(f) as fopen:
            for l in fopen:
                l = json.loads(l)
                for k, v in l.items():
                    d[k].append(v)

        df = polars.DataFrame(d)

        df.write_parquet(file)


def main():
    files = glob('output/*.jsonl')
    files = sorted(files)

    os.makedirs('data', exist_ok=True)

    mp.multiprocessing(files, loop, cores=min(len(files), 200), returned=False)


if __name__ == "__main__":
    main()
