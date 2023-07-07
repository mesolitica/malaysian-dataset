import requests
import os
import json
import asyncio
from tqdm import tqdm
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.parse import urlparse
import urllib3
import time
from requests_html import HTMLSession, AsyncHTMLSession
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from tika import parser
from bs4.element import Comment
from bs4 import BeautifulSoup

import logging

logging.basicConfig(level=logging.DEBUG)

TIKA_HOST = 'http://localhost:9998'


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body, is_html=True):
    if is_html:
        soup = BeautifulSoup(body, 'html.parser')
    else:
        soup = body
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return '\n'.join(t.strip() for t in visible_texts).strip()


def parse_tika(string, minlen=2,):
    while True:
        try:
            raw_xml = parser.from_buffer(string, TIKA_HOST, xmlContent=True)
            break
        except BaseException:
            time.sleep(1.0)
    body = BeautifulSoup(raw_xml['content']).find('body')
    t = []
    for b in body:
        try:
            t_ = text_from_html(b, is_html=False)
            if len(t_) > minlen:
                t.append(t_)
        except Exception as e:
            pass

    return t


async def get_html(filename, url):
    #     if os.path.exists(filename) and os.path.getsize(filename) > 100:
    #         return

    if os.path.exists(filename):
        return

    with open(filename, 'w') as fopen:

        result = None
        if url.endswith('.jpg'):
            return
        if url.endswith('.png'):
            return
        if url.endswith('.jpeg'):
            return
        if url.endswith('.pdf'):
            try:
                result = requests.get(url, timeout=10).content
            except BaseException:
                pass
        else:
            session = AsyncHTMLSession(verify=False)

            try:

                r = await session.get(url, verify=False, timeout=10)
                await r.html.arender(timeout=10)

                result = r.html.html
            except Exception as e:
                pass

            await session.close()

#         try:
#             result = requests.get(url, timeout = 20).content
#         except Exception as e:
#             print(e)

        if result is not None:
            try:
                result = '\n'.join(parse_tika(result))
                data = {
                    'url': url,
                    'data': result,
                }

                json.dump(data, fopen)
            except Exception as e:
                print(e)

from glob import glob
files = sorted(glob('url-*.json'))
print(files)
directory = 'page'

batch_size = 10
for f in files:
    t = f.replace('.json', '').replace('url-', '')
    with open(f) as fopen:
        urls = sorted(json.load(fopen))
        urls = [url.strip() for url in urls]
    urls = sorted([u for u in urls if urlparse(u).netloc.endswith('.my')])
    urls = [(os.path.join(directory, f'{t}-{no}.json'), url) for no, url in enumerate(urls)]
    print(f)
    for i in tqdm(range(0, len(urls), batch_size)):
        b = urls[i: i + batch_size]

        async def main():
            tasks = [get_html(url[0], url[1]) for url in b]
            await asyncio.gather(*tasks)

        asyncio.run(main())
