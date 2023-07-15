import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib3
import argparse
import asyncio
import json
import sys
import os
from tqdm import tqdm
from urllib.parse import urlparse
from requests_html import HTMLSession, AsyncHTMLSession
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='url')
args = parser.parse_args()
url = args.url
netloc = urlparse(url).netloc
netloc = netloc.replace('www.', '')
filename = f'url-{netloc}.json'
print('url:', url)
print(filename)

if os.path.exists(filename):
    sys.exit()

rejected = [
    'wa.link',
    'mailto:',
    't.me',
    'tally.so',
    'discord.gg',
    'arxiv.org',
    'javascript:'
]


async def get_html(url):
    session = AsyncHTMLSession(verify=False)
    result = None
    try:

        r = await session.get(url, verify=False, timeout=20)
        await r.html.arender(timeout=20)

        result = r.html.html
    except Exception as e:
        pass

    await session.close()
    return result


def get_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links


visited_pages = set([url])


async def crawl(base_url):
    if base_url.endswith('.pdf'):
        return

    html = await get_html(base_url)

    if html is None:
        return

    visited_pages.add(base_url)
    links = get_links(html)
    for link in links:
        try:
            if any([r in link for r in rejected]):
                continue

            if not link.startswith('http'):
                link = urljoin(base_url, link)

            link = link.split('#')[0]
            link = link.split('?')[0]

            if link not in visited_pages:
                visited_pages.add(link)
        except Exception as e:
            pass


async def run(b):
    await asyncio.gather(*[crawl(url) for url in b])

batch_size = 10

for no in range(3):
    l = list(visited_pages)
    print(no, len(l))
    for i in tqdm(range(0, len(l), batch_size)):
        b = l[i: i + batch_size]
        asyncio.run(run(b))
        if len(visited_pages) >= 5000:
            break

with open(filename, 'w') as fopen:
    json.dump(list(visited_pages), fopen)
