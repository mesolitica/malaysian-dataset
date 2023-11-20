import requests
from bs4 import BeautifulSoup
import logging
import json
from tqdm import tqdm
import time

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the base URL of the site to scrape
base_url = 'https://www.cypherhackz.net/'
filename = 'cypherhackz'

def get_articles(url):
    time.sleep(5)
    posts = []
    links = []
    titles = []

    # Get total number of pages from headers by sending a HEAD request to the URL
    response = requests.head(f"{base_url}/wp-json/wp/v2/posts")
    total_pages = response.headers.get('X-WP-TotalPages', 'Unknown')
    total_posts = response.headers.get('X-WP-Total', 'Unknown')
    for page in tqdm(range(1, int(total_pages) + 1)):
        logging.debug(f"Retrieve page no {page}")
        response = requests.get(f'{url}/wp-json/wp/v2/posts?page={page}&per_page=100')
        if response.ok:
            links = links + [d['link'] for d in response.json() if 'link' in d]
            titles = titles + [d['title']['rendered'] for d in response.json() if 'title' in d]
            posts = posts + [BeautifulSoup(d['content']['rendered'] , 'html.parser').get_text(strip=True) for d in response.json() if ('content' in d and 'rendered' in d['content'])]
            logging.debug(f"{len(posts)} articles retrieve after querying page {page}")
            if len(posts) == int(total_posts):
                break
        else:
            logging.error(f"Failed to retrieve the page no: {page}. Status code: {response.status_code}")
    return posts, links, titles

def combine_data(posts, links, titles):
    combined_list = [{'url': link, 'title': title, 'body': post}
                 for link, title, post in zip(links, titles, posts)]
    return combined_list

def save_json(posts):
    with open(f'{filename}.jsonl', 'a') as f:
        json.dump(posts, f)

get_articles(base_url)
articles, urls, titles = get_articles(base_url)
data = combine_data(articles, urls, titles)
save_json(data)
logging.info(f"Retrieved {len(data)} articles from {base_url}")
