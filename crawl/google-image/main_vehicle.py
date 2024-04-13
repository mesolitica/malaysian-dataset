import warnings
warnings.filterwarnings("ignore")

import os
import logging
import asyncio
import time
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup, SoupStrainer
from tqdm import tqdm
import pandas as pd


HEADLESS = True
MAX_EXTRACTION_ERROR = 5


async def scroll_and_extract(keyword, page):
    '''
    scroll through the page and extract image with alt text
    '''
    last_height = await page.evaluate("""
        () => document.documentElement.scrollHeight
    """)
    try:
        i = 0
        while True:
            await page.mouse.wheel(0, 15000)
            await asyncio.sleep(1)

            last_height_ = await page.evaluate("""
                () => document.documentElement.scrollHeight
            """)
            if last_height_ > last_height:
                last_height = last_height_
                print(keyword, f'scrolling {i} {last_height_} {last_height}')
            else:
                print(keyword, f'break scrolling {i}')
                break

            i += 1
    except BaseException:
        pass

    print(keyword, 'clicking h3')
    img_elements = await page.query_selector_all('h3')
    for i in tqdm(range(len(img_elements))):
        try:
            await img_elements[i].click(timeout=2000)
        except BaseException:
            pass

    html = await page.content()
    soup = BeautifulSoup(html, 'html.parser')
    image_list = []
    for image in soup.find_all('h3'):
        img = image.find('img')
        if img is not None:
            href = image.find('a').get('href')
            if href is None:
                continue
            alt_text = img.attrs['alt']
            d = {
                'alt_text': alt_text,
                'parent_href': href,
            }
            if img.attrs['src'].startswith('data:image'):
                d['image_base64'] = img.attrs['src']
            else:
                d['image_url'] = img.attrs['src']
            image_list.append(d)
    return image_list


async def scrape(keyword, scrape_output_path):
    filename_done = f'{scrape_output_path}_done'
    if os.path.exists(filename_done):
        return

    keyword = keyword.replace('\n', '')
    print(f'Scraping keyword: "{keyword}"')
    alternate_type_list = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=HEADLESS)
        page = await browser.new_page(
            geolocation={'latitude': 3.1447325, 'longitude': 101.664989},
            permissions=['geolocation']
        )
        url = f'https://www.google.com/search?q={keyword}&tbm=isch'
        await page.goto(url)
        # get list of alternate images type
        html = await page.content()
        image_segment = SoupStrainer('span', {'role': 'list'})
        soup = BeautifulSoup(html, 'html.parser', parse_only=image_segment)
        for index, span in enumerate(soup.find_all('span')):
            if index == 0:
                continue
            alternate_type_list.append(span.get_text())
        print(f'[{keyword}] alternate subkeyword {alternate_type_list}')
        print(f'[{keyword}] Scraping base keyword...')
        image_list = await scroll_and_extract(keyword, page)
        df = pd.DataFrame(
            image_list,
            columns=[
                'alt_text',
                'parent_href',
                'image_base64'])
        df.to_json(scrape_output_path, orient='records', mode='a', lines=True)
        print(f'Completed! [{len(df)} rows]')

        for alt_type in alternate_type_list:
            print(f'[{keyword}] Scraping "{alt_type}" subkeyword...')
            url = f'https://www.google.com/search?q={keyword}&tbm=isch&chips=q:{keyword},g_1:{alt_type}'
            await page.goto(url)
            image_list = await scroll_and_extract(keyword, page)
            df = pd.DataFrame(
                image_list,
                columns=[
                    'alt_text',
                    'parent_href',
                    'image_base64']
            )
            df.to_json(scrape_output_path, orient='records', mode='a', lines=True)
            print(f'[{keyword}] Completed! [{len(df)} rows]')

        with open(filename_done, 'w') as fopen:
            fopen.write('done')


async def run():
    BATCH_SIZE = 100

    text_file = open('vehicles.txt', 'r')
    lines = text_file.readlines()
    keyword_list = list(dict.fromkeys(lines))
    functions = []
    for no, keyword in enumerate(keyword_list):
        filename = f'data/generated-vehicle/{no}.jsonl'
        functions.append(scrape(keyword, filename))

    for i in range(0, len(functions), BATCH_SIZE):
        await asyncio.gather(*functions[i: i + BATCH_SIZE])

if __name__ == '__main__':

    asyncio.run(run())
