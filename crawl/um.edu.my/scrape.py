import aiohttp
import asyncio
from bs4 import BeautifulSoup
from tqdm.asyncio import tqdm
import json

async def fetch(session, url, retries=3):
    for attempt in range(retries):
        try:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=60)) as response:
                response.raise_for_status()
                return await response.text()
        except aiohttp.ClientError as e:
            print(f"Error fetching {url}, attempt {attempt + 1}/{retries}: {e}")
            await asyncio.sleep(2) 
    return None

async def scrape_content(session, url):
    html_content = await fetch(session, url)
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')

        title_tag = soup.find('h1', class_='kingster-page-title')
        title = title_tag.get_text(strip=True) if title_tag else "No title found"

        about_me_div = soup.find('div', class_='kingster-content-wrap kingster-item-pdlr clearfix')
        body = about_me_div.get_text(strip=True) if about_me_div else "No content found in 'resume-body' div."

        return {'url': url, 'title': title, 'body': body}
    return None

async def main():
    results = []

    with open('links-umnews.txt', 'r') as file:
        urls = [url.strip() for url in file.readlines()]

    async with aiohttp.ClientSession() as session:
        tasks = [scrape_content(session, url) for url in urls]
        for content in tqdm(asyncio.as_completed(tasks), desc='Scraping URLs', total=len(urls)):
            result = await content
            results.append(result)

    with open('umnews-scraped1.json', 'w') as outfile:
        json.dump(results, outfile, indent=2)

if __name__ == '__main__':
    asyncio.run(main())