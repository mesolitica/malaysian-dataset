import os
import json
import torch
import pickle
from tqdm import tqdm
from unidecode import unidecode
from malaya.text.rouge import postprocess_summary
from transformers import T5Tokenizer, T5ForConditionalGeneration
import malaya
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', help='filename')
parser.add_argument('-d', '--device', help='device')
args = parser.parse_args()
filename = args.filename
device = args.device or '0'
print('device', device)

maxlen = 128

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

            article = data['keyword']

            input_ids = tokenizer.encode(f'terjemah Inggeris ke Melayu: {article}', return_tensors='pt').cuda()
            outputs = model.generate(input_ids, max_length=1000)
            t_highlights = tokenizer.decode(outputs[0], skip_special_tokens=True)

            data['translated-keyword'] = t_highlights

            d = json.dumps(data)
            file.write(f'{d}\n')
            file.flush()

            pointer.index = i
            pointer._save()

file.close()
