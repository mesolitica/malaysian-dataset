# !wget https://the-eye.eu/public/AI/pile/train/00.jsonl.zst
# !/home/husein/pure-text/zstd/build/cmake/programs/zstd -d 00.jsonl.zst

# !pip3 install zstandard ujson

from langdetect import detect
from tqdm import tqdm
import string
import malaya
import re
import pickle
import ujson as json
import os
import sys

filename = sys.argv[1]
try:
    device = sys.argv[2]
except:
    device = ''

os.environ['CUDA_VISIBLE_DEVICES'] = device


chars = string.ascii_lowercase + ' '

split_sentences = malaya.text.function.split_into_sentences
transformer = malaya.translation.en_ms.transformer(check_gpu=False)


def cleaning(string):
    return re.sub(r'[ ]+', ' ', string).strip()


class Pointer:
    def __init__(self, filename):
        self.filename = filename
        self.index = 0

    def _save(self):
        with open(self.filename, 'wb') as fopen:
            pickle.dump(self.index, fopen)

    def increment(self):
        self.index += 1
        self._save()

    def load(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, 'rb') as fopen:
            self.index = pickle.load(fopen)


batch_size = 16

pointer = Pointer(f'{filename}.pickle')
pointer.load()
index = 0

file = open(f'{filename}.translated', 'a')

with open(filename) as fopen:
    dataset = json.load(fopen)

for l in tqdm(dataset):
    if index >= pointer.index:
        meta = l['meta']['pile_set_name']
        if meta not in ['Pile-CC', 'Wikipedia (en)']:
            print(meta)
            splitted = split_sentences(l['text'], minimum_length=2)
            translated = []

            if meta not in ['Github']:
                splitted = [cleaning(s) for s in splitted]
                splitted = [s for s in splitted if 1 < len(s.split()) < 150]
                splitted = [s for s in splitted if len(
                    [c for c in s.lower() if c in chars]) / len(s) >= 0.9]
                splitted = [s for s in splitted if detect(s) == 'en']
                print(splitted)
                for i in tqdm(range(0, len(splitted), batch_size)):
                    translated.extend(
                        transformer.greedy_decoder(splitted[i: i + batch_size])
                    )
            d = json.dumps(
                {'en': splitted, 'ms': translated, 'meta': l['meta']}
            )
            file.write(f'{d}\n')
            file.flush()

        pointer.increment()
    index += 1

file.close()
