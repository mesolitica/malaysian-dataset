from glob import glob
import yt_dlp as youtube_dl
import os
from tqdm import tqdm
import random
import time
import mp
import re

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '64',
    }],
    'postprocessor_args': [
        '-ar', '22050'  # Set sampling rate to 22050 Hz
    ],
    'quiet': False,
}

from glob import glob

ids = []
files = glob('*.txt')
rejected = [
    'indon',
    'dropout',
    'lifegallerychannel',
    'dwarkeshpatel',
    '60minutes',
    'freethink',
    'boxoffice',
    'freemalaysiatoday',
    'cnbctelevision',
    'smartereveryday',
    'tedx',
]
files = [f for f in files if all([r not in f.lower() for r in rejected])]
for f in files:
    with open(f) as fopen:
        t = fopen.read().split('\n')
        ids.extend(t)
        
print('before', len(ids))
ids = sorted([i for i in ids if len(i) and not os.path.exists(os.path.join('done', i))])[::-1]
print('after', len(ids))
urls = [f'https://www.youtube.com/watch?v={t_}' for t_ in ids]

def contains_chinese(text):
    chinese_pattern = re.compile(r'[\u4e00-\u9fff]')
    return bool(chinese_pattern.search(text))

def contains_russian(text):
    cyrillic_pattern = re.compile(r'[\u0400-\u052F]')
    return bool(cyrillic_pattern.search(text))

def contains_indian(text):
    devanagari_pattern = re.compile(r'[\u0900-\u097F]')
    return bool(devanagari_pattern.search(text))

rejected = [
    'indon',
    'menit',
    '扮',
    '浣',
    '心',
    'arab',
    'hollywood',
    'sepeda',
    'sex',
    'ceo',
    'pake',
    'how close',
    'collegehumor',
    '铠',
    '课',
    'cowok',
    'inggris',
    'nomor',
    '斌',
    '妮',
    'working',
    'social music',
    'kunti',
    'gangguin',
    'umno',
    'pkr',
    'pas',
    'politik',
    'keren',
    'banget',
    'laugh',
    'hewan',
    'busting',
    'bikin',
    'play it by ear',
    'coding',
    'mobil',
    'diumpetin',
    'beverly',
    'music video',
    'zikir',
    'the guy',
    'chinese',
    'bilang',
    'watching',
    'xfloor',
    'senin',
    'porn',
    'dokter',
    'subletting',
    'the dawn',
    'populer'
]

def loop(rows):
    urls, _ = rows
    for url in tqdm(urls):
        i = url.split('?v=')[1]
        filename_done = os.path.join('done', i)
        if os.path.exists(filename_done):
            continue
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                filename = ydl.prepare_filename(info).replace('.m4a', '.mp3').replace('.webm', '.mp3')
                lower = filename.lower()
                if contains_chinese(filename) or contains_russian(filename) or contains_indian(filename):
                    with open(filename_done, 'w') as fopen:
                        fopen.write('DONE')
                    continue
                if any([r in lower for r in rejected]):
                    with open(filename_done, 'w') as fopen:
                        fopen.write('DONE')
                    continue
                if os.path.exists(filename) or os.path.exists(os.path.join('audio', filename)):
                    with open(filename_done, 'w') as fopen:
                        fopen.write('DONE')
                    continue
                ydl.download([url])
                
                with open(filename_done, 'w') as fopen:
                    fopen.write('DONE')
                    
        except Exception as e:
            print('Exceptionnnn', e)

mp.multiprocessing(sorted(urls)[::-1], loop, cores = 20, returned = False)
