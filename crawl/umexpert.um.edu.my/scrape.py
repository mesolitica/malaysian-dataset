
from bs4 import BeautifulSoup
from tqdm.asyncio import tqdm
import json
import requests
import time

def scrape_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')

        title_tag = soup.find('h1', class_='name mt-1 mb-1 text-uppercase text-uppercase')
        title = title_tag.get_text(strip=True) if title_tag else "No title found"

        about_me_div = soup.find('div', class_='resume-body pl-3 pr-4 pb-4 ml-4 pt-5')
        body = about_me_div.get_text(strip=True) if about_me_div else "No content found in 'resume-body' div."

        return {'url': url, 'title': title, 'body': body}

    except requests.RequestException as e:
        return {'url': url, 'title': 'Error', 'body': f"Error fetching or processing the page: {e}"}

def save_results(results):
    with open('umexpert-scraped1.json', 'w') as outfile:
        json.dump(results, outfile, indent=2)

def main():
    current = time.time()
    results = []
    with open('links-umexpert-modified.txt', 'r') as file:
        urls = file.readlines()
        i = 0
        for url in tqdm(urls): 
            url = url.strip()
            content = scrape_content(url)
            results.append((content))
            i += 1
            if i % 10 == 0:
                save_results(results)


    

    print(f"Time taken: {time.time() - current:.2f} seconds")

if __name__ == '__main__':
    main()
