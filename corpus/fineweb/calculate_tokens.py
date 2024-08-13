import json
import os
from transformers import AutoTokenizer
from glob import glob
from tqdm import tqdm
import mp
import tiktoken


def loop(files):
    files, _ = files
    encoding = tiktoken.encoding_for_model("gpt2")
    for f in tqdm(files):
        new_f = os.path.split(f)[-1]
        new_f = os.path.join('count', new_f)

        if os.path.exists(new_f):
            continue

        count = 0
        with open(f) as fopen:
            for l in fopen:
                l = json.loads(l)
                count += len(encoding.encode(l['text']))

        with open(new_f, 'w') as fopen:
            json.dump(count, fopen)


def main():
    files = glob('output/*.jsonl')
    files = sorted(files)

    os.system('mkdir count')

    try:
        if len(files):
            mp.multiprocessing(files, loop, cores=min(len(files), 200), returned=False)
    except BaseException:
        pass

    files = glob('count/*.jsonl')
    total_tokens = 0
    for f in files:
        with open(f) as fopen:
            total_tokens += json.load(fopen)

    print('total tokens', total_tokens)


if __name__ == "__main__":
    main()
