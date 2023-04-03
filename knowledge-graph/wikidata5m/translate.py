# !pip3 install ujson

from tqdm import tqdm
import malaya
import re
import pickle
import ujson as json
import os
import sys
import re
from unidecode import unidecode
from collections import defaultdict
import numpy as np

filename = sys.argv[1]
try:
    device = sys.argv[2]
except:
    device = ''

os.environ['CUDA_VISIBLE_DEVICES'] = device

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


pointer = Pointer(f'{filename}.pickle')
pointer.load()
index = 0

file = open(f'{filename}.translated', 'a')


def cleaning(string):
    string = re.sub('[^A-Za-z ]+', ' ', unidecode(string).lower())
    return re.sub(r'[ ]+', ' ', string).strip()


def get_uniques(string):
    uniques = defaultdict(list)
    splitted = string.split('\t')
    for s in splitted[1:]:
        uniques[cleaning(s)].append(unidecode(s))

    r = []
    for k, v in uniques.items():
        vals = [sum([ord(c) for c in v_]) for v_ in v]
        r.append(v[np.argmin(vals)])
    return splitted[0], r


with open(filename) as fopen:
    dataset = json.load(fopen)

for l in tqdm(dataset):
    if index >= pointer.index:
        id, uniques = get_uniques(l)
        uniques = sorted(uniques, key=len, reverse=True)
        uniques = uniques[:32]
        ms = transformer.greedy_decoder(uniques)
        d = json.dumps({'id': id, 'uniques': uniques, 'original': l, 'uniques_ms': ms})
        file.write(f'{d}\n')
        file.flush()

        pointer.increment()
    index += 1

file.close()
