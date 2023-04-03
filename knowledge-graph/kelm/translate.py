import os

os.environ['CUDA_VISIBLE_DEVICES'] = '0'
os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'

"""
split -l 200000 -d --additional-suffix=.splitted quadruples-validation.tsv quadruples-validation
"""

import json
import pickle
import os
import torch
import transformers
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', help='filename')
parser.add_argument('-b', '--batch_size', help='batch size')
args = parser.parse_args()

filename = args.filename
batch_size = int(args.batch_size)


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


file = open(f'{filename}.translated', 'a')

pointer = Pointer(f'{filename}.pickle')
pointer.load()
index = 0

target = 'zsm_Latn'
source = 'eng_Latn'

real_name = 'facebook/nllb-200-3.3B'
model = AutoModelForSeq2SeqLM.from_pretrained(real_name)
tokenizer = AutoTokenizer.from_pretrained(real_name)
_ = model.cuda()

data = []
with open(filename) as fopen:
    for line in fopen:
        if len(line):
            data.append(line)

print(len(data))

for i in tqdm(range(0, len(data), batch_size)):
    if i >= pointer.index:
        batch = data[i: i + batch_size]
        batch = [json.loads(b) for b in batch]
        batch = [b for b in batch if len(b['sentence'].split()) <= 100]

        if len(batch):
            t = [b['sentence'] for b in batch]
            inputs = tokenizer(t, return_tensors="pt", padding=True)
            for k in inputs.keys():
                inputs[k] = inputs[k].cuda()

            translated_tokens = model.generate(
                **inputs, forced_bos_token_id=tokenizer.lang_code_to_id[target], max_length=500
            )
            decoded = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)
            for k in range(len(batch)):
                batch[k]['translate'] = decoded[k]

            d = json.dumps(batch)
            file.write(f'{d}\n')
            file.flush()

        pointer.index = i
        pointer._save()


file.close()
