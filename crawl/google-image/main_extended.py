import warnings
warnings.filterwarnings("ignore")

import os
import logging
import asyncio
import time
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup, SoupStrainer
import pandas as pd
import filelock
import uuid


def setup_logging(file_path):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.FileHandler(file_path),
            logging.StreamHandler()
        ]
    )


TRACKER_PATH = 'tracker.txt'
FAIL_TRACKER_PATH = 'fail.txt'
HEADLESS = True
MAX_EXTRACTION_ERROR = 5


def read_first_number_and_update(filename):
    with filelock.FileLock(filename + '.lock'):
        with open(filename, 'r+') as file:
            first_line = file.readline()
            if not first_line:
                return None
            first_number = int(first_line)
            remaining_numbers = file.readlines()
            file.seek(0)
            file.truncate()
            for num in remaining_numbers:
                file.write(num)
        return first_number


def update_fail(fail_index, filename):
    with filelock.FileLock(filename + '.lock'):
        with open(filename, 'r+') as file:
            existing_indexes = file.readlines()
            file.seek(0)
            file.truncate()
            for num in existing_indexes:
                file.write(num)

            file.write(str(fail_index) + '\n')


async def scroll_and_extract(page):
    '''
    scroll through the page and extract image with alt text
    '''
    try:
        for _ in range(6):
            time.sleep(1)
            await page.keyboard.down('End')
        await page.locator('xpath=//*[@id="islmp"]/div/div/div/div/div[1]/div[2]/div[2]/input').click(timeout=3000)
        for _ in range(10):
            time.sleep(1)
            await page.keyboard.down('End')
    except BaseException:
        pass

    img_elements = await page.query_selector_all('a')
    img_elements = [i for i in img_elements if (await i.get_attribute('jsname')) == 'sTFXNd']
    for i in range(len(img_elements)):
        await img_elements[i].click()

    html = await page.content()
    image_segment = SoupStrainer('div', {'role': 'list'})
    soup = BeautifulSoup(html, 'html.parser', parse_only=image_segment)
    image_list = []
    for image in soup.find_all('img'):
        try:
            if image.attrs['alt'] != '':
                image_metadata = {
                    'alt_text': image.attrs['alt'],
                }
                if image.attrs['src'].startswith('data:image'):
                    image_metadata['image_base64'] = image.attrs['src']
                else:
                    image_metadata['image_url'] = image.attrs['src']

                try:
                    parent_href = image.parent.parent.get('href')
                    image_metadata['parent_href'] = parent_href
                except Exception as e:
                    logging.warning('failed to get parent href')

                image_list.append(image_metadata)
        except Exception as e:
            pass
    return image_list


async def iterate_extract_image(page):
    await page.locator('xpath=//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]').click()
    image_list = []
    error_counter = 0
    while True:
        try:
            next_button = page.locator(
                'xpath=//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[1]/div/div[2]/button[2]')
            if await next_button.get_attribute('aria-disabled', timeout=500) == 'true':
                break
            await next_button.click()
        except BaseException:
            error_counter += 1
            if error_counter > MAX_EXTRACTION_ERROR:
                break

    html = await page.content()
    image_segment = SoupStrainer('div', {'class': 'islrc'})
    soup = BeautifulSoup(html, 'html.parser', parse_only=image_segment)
    for image in soup.find_all('img'):
        try:
            if image.attrs['alt'] != '':
                image_metadata = {
                    'alt_text': image.attrs['alt'],
                }
                if image.attrs['src'].startswith('data:image'):
                    image_metadata['image_base64'] = image.attrs['src']
                else:
                    image_metadata['image_url'] = image.attrs['src']

                try:
                    parent_href = image.parent.parent.get('href')
                    image_metadata['parent_href'] = parent_href
                except Exception as e:
                    logging.warning('failed to get parent href')

                image_list.append(image_metadata)
        except Exception as e:
            pass

    return image_list


async def scrape(keyword_list, scrape_output_path):
    while True:
        keyword_index = read_first_number_and_update(TRACKER_PATH)
        if keyword_index is None:
            logging.info('Done')
            break
        try:
            keyword = keyword_list[keyword_index]
            keyword = keyword.replace('\n', '')
            logging.info(f'Scraping keyword: "{keyword}"')
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
                logging.info(f'[{keyword}] alternate subkeyword {alternate_type_list}')
                logging.info(f'[{keyword}] Scraping base keyword...')
                image_list = await iterate_extract_image(page)
                df = pd.DataFrame(
                    image_list,
                    columns=[
                        'alt_text',
                        'image_url',
                        'parent_href',
                        'image_base64'])
                df.to_json(scrape_output_path, orient='records', mode='a', lines=True)
                logging.info(f'Completed! [{len(df)} rows]')

                for alt_type in alternate_type_list:
                    logging.info(f'[{keyword}] Scraping "{alt_type}" subkeyword...')
                    url = f'https://www.google.com/search?q={keyword}&tbm=isch&chips=q:{keyword},g_1:{alt_type}'
                    await page.goto(url)
                    image_list = await iterate_extract_image(page)
                    df = pd.DataFrame(
                        image_list,
                        columns=[
                            'alt_text',
                            'image_url',
                            'parent_href',
                            'image_base64'])
                    df.to_json(scrape_output_path, orient='records', mode='a', lines=True)
                    logging.info(f'[{keyword}] Completed! [{len(df)} rows]')

        except Exception as e:
            update_fail(fail_index=keyword_index, filename=FAIL_TRACKER_PATH)
            logging.info(f'[{keyword_index}] Failed {e}')

if __name__ == '__main__':
    instance_id = str(uuid.uuid4())

    SCRAPE_OUTPUT_PATH = f'data/generated/extended-[{instance_id}].jsonl'
    LOG_FILE_PATH = f'logs/scraping_[{instance_id}].log'

    setup_logging(LOG_FILE_PATH)
    logging.info(f'instance_id: {instance_id}')
    text_file = open('data/source/malay-words.txt', 'r')
    lines = text_file.readlines()
    keyword_list = list(dict.fromkeys(lines))

    asyncio.run(scrape(keyword_list, SCRAPE_OUTPUT_PATH))
