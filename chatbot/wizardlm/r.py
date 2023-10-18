import json
import malaya
import argparse
import os
import pickle
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', help='filename')
parser.add_argument('-k', '--hostname', help='hostname')
args = parser.parse_args()
filename = args.filename

model = malaya.translation.huggingface(
    model='mesolitica/translation-t5-small-standard-bahasa-cased',
    use_ctranslate2=True,
    device='cuda',
    quantization='bfloat16')


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

file = open(f'{filename}.requested', 'a')

with open(filename) as fopen:
    for i, l in tqdm(enumerate(fopen)):
        if i >= pointer.index:
            text = json.loads(l)
            if len(model.tokenizer.tokenize(text)) < 4096:
                r = model.generate(
                    [text],
                    to_lang='ms',
                    max_input_length=4096,
                    max_decoding_length=4096)[0]
                data = {'src': text, 'r': r}

                d = json.dumps(data)
                file.write(f'{d}\n')
                file.flush()

            pointer.index = i
            pointer._save()

file.close()
