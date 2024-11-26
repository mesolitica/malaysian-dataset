from glob import glob
import yt_dlp as youtube_dl
import os
from tqdm import tqdm
import random
import time
import mp
import json

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '128',
    }],
    'quiet': False,
}

with open('PARLIMENMALAYSIA1.parlimen') as fopen:
    d = fopen.read().split('\n')
    
d = [d_ for d_ in d if len(d_)]

urls = [f'https://www.youtube.com/watch?v={t_}' for t_ in d]
filtered = urls
filtered = [s for s in filtered if len(s.split('?v=')[1]) > 0]

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
                if os.path.exists(filename) or os.path.exists(os.path.join('audio', filename)):
                    with open(filename_done, 'w') as fopen:
                        fopen.write('DONE')
                    continue
                ydl.download([url])
                
                with open(filename_done, 'w') as fopen:
                    fopen.write('DONE')
                    
        except Exception as e:
            print(e)

mp.multiprocessing(filtered, loop, cores = 3, returned = False)