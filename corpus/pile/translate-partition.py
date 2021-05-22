# !wget https://the-eye.eu/public/AI/pile/train/00.jsonl.zst
# !/home/husein/pure-text/zstd/build/cmake/programs/zstd -d 00.jsonl.zst

# !pip3 install zstandard ujson

import os
import sys

os.environ['CUDA_VISIBLE_DEVICES'] = ''
filename = sys.argv[1]

import ujson as json
import pickle
import re
import malaya
from tqdm import tqdm

split_sentences = malaya.text.function.split_into_sentences
transformer = malaya.translation.en_ms.transformer()


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
            splitted = split_sentences(l['text'], minimum_length = 2)
            splitted = [cleaning(s) for s in splitted]
            splitted = [s for s in splitted if len(s.split()) < 150]
            words = ('. '.join(splitted)).split()
            translated = []
            if meta not in ['Github']:
                for i in range(0, len(splitted), batch_size):
                    translated.extend(
                        transformer.greedy_decoder(splitted[i : i + batch_size])
                    )
            d = json.dumps(
                {'en': splitted, 'ms': translated, 'meta': l['meta']}
            )
            file.write(f'{d}\n')
            file.flush()

        pointer.increment()
    index += 1

file.close()
