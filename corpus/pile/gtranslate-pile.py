# !wget https://the-eye.eu/public/AI/pile/train/00.jsonl.zst
# !/home/husein/pure-text/zstd/build/cmake/programs/zstd -d 00.jsonl.zst

# !pip3 install zstandard ujson

import os

os.environ['CUDA_VISIBLE_DEVICES'] = ''

import ujson as json
import pickle
import re
import malaya
import dask.bag as db
from tqdm import tqdm
from collections import defaultdict
from googletrans import Translator
import time

translator = Translator()
split_sentences = malaya.text.function.split_into_sentences


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


def translate(batch):
    index, meta, texts = batch
    en, ms = [], []
    translations = translator.translate(texts, dest = 'ms')
    for translation in translations:
        en.append(translation.origin)
        ms.append(translation.text)
    time.sleep(1.2)
    return index, meta, en, ms


filename = '00.jsonl'
batch_size = 4
max_thread_size = 5

pointer = Pointer('p.pickle')
pointer.load()
index = 0
en, ms, metas, batches = defaultdict(list), defaultdict(list), {}, []

file = open(f'{filename}.translated', 'a')
with open(filename) as fopen:
    for line in fopen:
        if index >= pointer.index:
            l = json.loads(line)
            meta = l['meta']['pile_set_name']
            if meta not in ['Pile-CC', 'Wikipedia (en)', 'Github']:
                splitted = split_sentences(l['text'], minimum_length = 2)
                splitted = [cleaning(s) for s in splitted]
                splitted = [s for s in splitted if len(s.split()) < 150]
                words = ('. '.join(splitted)).split()
                print(
                    f'{index}: {meta}: total words: {len(words)}, total sentences: {len(splitted)}'
                )
                for i in range(0, len(splitted), batch_size):
                    batches.append((index, meta, splitted[i : i + batch_size]))

            if len(batches) >= max_thread_size:
                bags = db.from_sequence(batches)
                mapped = bags.map(translate)
                computed = mapped.compute(
                    scheduler = 'threads', num_workers = max_thread_size
                )
                for c in computed:
                    en[c[0]].extend(c[2])
                    ms[c[0]].extend(c[3])
                    metas[c[0]] = c[1]

                for key in en.keys():
                    print(key, metas[key])
                    d = json.dumps(
                        {'en': en[key], 'ms': ms[key], 'meta': metas[key]}
                    )

                    file.write(f'{d}\n')
                    file.flush()
                    pointer.increment()

                en, ms, metas, batches = (
                    defaultdict(list),
                    defaultdict(list),
                    {},
                    [],
                )

        index += 1

file.close()
