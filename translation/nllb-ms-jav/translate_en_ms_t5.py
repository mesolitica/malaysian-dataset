import os
import json
import torch
import pickle
from tqdm import tqdm
from unidecode import unidecode
from transformers import T5Tokenizer, T5ForConditionalGeneration
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', help='filename')
parser.add_argument('-d', '--device', help='device')
parser.add_argument('-d', '--index', help='index')
args = parser.parse_args()
filename = args.filename
device = args.device or '0'
index = int(args.index or 0)
print('device', device)
print('index', index)

os.environ['CUDA_VISIBLE_DEVICES'] = device
tokenizer = T5Tokenizer.from_pretrained('mesolitica/finetune-translation-t5-small-standard-bahasa-cased')
model = T5ForConditionalGeneration.from_pretrained('mesolitica/finetune-translation-t5-small-standard-bahasa-cased')

_ = model.cuda()


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

file = open(f'{filename}.translated', 'a')

with open(filename) as fopen:
    for i, l in tqdm(enumerate(fopen)):
        if i >= pointer.index:
            data = json.loads(l)
            text = data[index]

            input_ids = tokenizer.encode(f'terjemah Inggeris ke Melayu: {text}', return_tensors='pt').cuda()
            outputs = model.generate(input_ids, max_length=10000)
            t = tokenizer.decode(outputs[0], skip_special_tokens=True)

            d = {
                'data': data,
                'translated': t,
            }

            d = json.dumps(d)
            file.write(f'{d}\n')
            file.flush()

            pointer.index = i
            pointer._save()

file.close()
