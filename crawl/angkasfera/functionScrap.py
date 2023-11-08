"""
Angkasfera
https://angkasfera.com/

231108
"""
# Import Libraries and Packages
import pandas as pd

from bs4 import BeautifulSoup 
import requests  

pd.set_option("display.max_colwidth", None)

# Set Headers
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Cache-Control": "max-age=0",
    }

# Creare empty list
data = []

# Scraping loop
for page_num in range(1, 16):
    print(f"Scraping Page {page_num}")
    web_url = f"https://angkasfera.com/page{page_num}/"
    response = requests.get(web_url, headers=HEADERS)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        article_list = soup.find("div", class_='posts-wrap clearfix')
        title_tags = article_list.find_all('h2')

        for title_tag in title_tags:
            link = title_tag.find('a')
            if link:
                link_text = link.get('href')
                title_text = link.get_text()

                page_url = link_text
                page_response = requests.get(page_url, headers=HEADERS)
                page_soup = BeautifulSoup(page_response.content, 'html.parser')
                article_para = page_soup.find("div", class_='post-content')
                cleaned_text = article_para.text.replace('\n', '').replace('\t', '')

                data.append({'link': link_text, 'title': title_text, 'text': cleaned_text})
    else:
        print(f"Failed to fetch data from page {page_num}")

# Convert into Pandas dataframe
df = pd.DataFrame(data)

# Save as CSV
df.to_csv('scraped2.csv')