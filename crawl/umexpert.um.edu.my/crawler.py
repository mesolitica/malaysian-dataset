import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
import tqdm from tqdm

base_url = 'https://umexpert.um.edu.my/'

urls = []
visited_url = []
failed_url = []

urls.append(base_url)
while len(urls)>0:
    current = urls.pop()
    try:
        response = requests.get(current)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        visited_url.append(current)
        for link in soup.find_all('a', href=True):
            # Resolve relative links to absolute URLs
            full_url = urljoin(base_url, link['href'])
            if full_url not in visited_url and full_url not in urls and full_url.startswith(base_url) and full_url not in failed_url:
                urls.append(full_url)
        
    except requests.RequestException as e:
        failed_url.append(current)
        print(f"Error fetching or processing the page: {e}")


with open('links-umexpert.txt', 'w') as file:
    for item in visited_url:
        file.write(f"{item}\n")

def categorize_links(links):

    webpages = []
    for link in links:
        if link.endswith(''):
            webpages.append(link)
    return webpages