from tqdm import tqdm
import pickle
import json
import malaya
import os
os.environ['CUDA_VISIBLE_DEVICES'] = ''

alxlnet = malaya.entity.transformer_ontonotes5(model='alxlnet')
albert = malaya.entity.transformer_ontonotes5(model='albert')
xlnet = malaya.entity.transformer_ontonotes5(model='xlnet')
true_case = malaya.true_case.transformer()


filename = 'translated-trainset-parliament.json'

with open(filename) as fopen:
    data = json.load(fopen)


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
file = open(f'{filename}.ontonotes5.jsonl', 'a')


for i in tqdm(range(len(data))):
    if index >= pointer.index:
        s = data[i][0]
        t = true_case.greedy_decoder([s])[0]
        r = malaya.stack.voting_stack([xlnet, albert, alxlnet], t)
        d = json.dumps({'string': s, 'true-case': t, 'tagging': r})
        file.write(f'{d}\n')

        file.flush()
        pointer.increment()
    index += 1

file.close()
