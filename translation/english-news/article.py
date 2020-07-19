import os
import time

os.environ['LD_LIBRARY_PATH'] = '/home/husein/phantomjs-2.1.1-linux-x86_64/bin'
os.environ[
    'PATH'
] = '/home/husein/.local/bin:/home/husein/bin:/home/husein/anaconda3/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/husein/phantomjs-2.1.1-linux-x86_64/bin'

import translate_new

import json

files = ['dataset-0.json', 'dataset-100000.json', 'dataset-200000.json']

for f in files:

    with open(f) as fopen:
        data = json.load(fopen)

    translators = translate_new.Translate_Concurrent(
        batch_size = 20, from_lang = 'en', to_lang = 'ms'
    )

    t = translators.translate_batch(data)

    with open(f'{f}.translate', 'w') as fopen:
        json.dump(t, fopen)

    del translators
    time.sleep(60)
