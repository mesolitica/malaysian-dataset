from tqdm import tqdm
import os

with open('list.txt') as fopen:
    urls = fopen.read().split('\n')

urls = sorted(list(filter(None, urls)))
for url in tqdm(urls):
    print(url)
    command = f'python3 get-url.py --url="{url}"'
    os.system(command)
