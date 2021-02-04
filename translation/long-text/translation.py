import os
import time

os.environ['LD_LIBRARY_PATH'] = '/home/husein/phantomjs-2.1.1-linux-x86_64/bin'
os.environ[
    'PATH'
] = '/home/husein/.local/bin:/home/husein/bin:/home/husein/anaconda3/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/husein/phantomjs-2.1.1-linux-x86_64/bin'

import translate_new

import json

files = ['long-text-0.json', 'long-text-100000.json', 'long-text-1000000.json']

for f in files:
    print(f)
    translators = translate_new.Translate_Concurrent(
        batch_size = 20, from_lang = 'ms', to_lang = 'en'
    )
    with open(f) as fopen:
        data = json.load(fopen)

    t = translators.translate_batch(data)
    with open(f'{f}.translated.json', 'w') as fopen:
        json.dump(t, fopen)

    del translators
    time.sleep(10)
