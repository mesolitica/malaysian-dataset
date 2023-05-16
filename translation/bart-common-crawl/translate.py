import json
import argparse
import pickle
import os
import time
import random
from tqdm import tqdm
from Bard import Chatbot

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', help='filename')
parser.add_argument('-t', '--token', help='token')
args = parser.parse_args()
filename = args.filename
token = args.token

chatbot = Chatbot(token)


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


def translate(text, retry=10):
    key = '{`malay`, `english`}'
    for k in range(retry):
        try:
            t = f"""
            text `{text}`, translate to standard english and malay, return as JSON structure {key}
            """
            return chatbot.ask(t)
        except Exception as e:
            print(k, e)

        time.sleep(2)


pointer = Pointer(f'{filename}.pickle')
pointer.load()

file = open(f'{filename}.requested', 'a')

with open(filename) as fopen:
    for i, l in tqdm(enumerate(fopen)):
        if i >= pointer.index:
            data = json.loads(l)

            data = {'src': data, 'r': translate(data['original'])}

            d = json.dumps(data)
            file.write(f'{d}\n')
            file.flush()

            pointer.index = i
            pointer._save()

            time.sleep(random.uniform(1.0, 2.0))

file.close()
