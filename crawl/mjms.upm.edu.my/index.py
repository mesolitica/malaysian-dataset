import requests
from bs4 import BeautifulSoup
import json
import os
import re
from urllib.parse import urlparse
import fitz

BASE_URL = "https://mjms.upm.edu.my/"
SCRAPE_URL = "https://mjms.upm.edu.my/archives.php?page={}"
PDF_DIR = 'pdf'

if not os.path.exists(PDF_DIR):
    os.makedirs(PDF_DIR)

def get_all_links():
    """Get all archive links from the volume pages."""
    all_urls = []
    page = 1

    while True:
        url = SCRAPE_URL.format(page)
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.select("tbody a")

            if not links:
                break

            all_urls.extend(BASE_URL + link.get('href') for link in links)
        else:
            print(f"Failed to fetch page {url}. Status code: {response.status_code}")
            break

        page += 1

    return all_urls

def get_abstract_urls(archives_urls):
    """Get abstract links from archive URLs."""
    all_abstract_urls = []

    for archive_url in archives_urls:
        full_url = archive_url
        response = requests.get(full_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            valid_links = [
                BASE_URL + link.get('href')
                for link in soup.select("p a")
                if link.get('href') and "lihatmakalah.php?kod=" in link.get('href')
            ]
            all_abstract_urls.extend(valid_links)
        else:
            print(f"Failed to fetch page {full_url}. Status code: {response.status_code}")

    return all_abstract_urls

def get_fullpaper_urls(abstract_urls):
    """Get fullpaper links from abstract URLs."""
    all_fullpaper_urls = []

    for abstract_url in abstract_urls:
        full_url = abstract_url
        response = requests.get(full_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            valid_links = [
                BASE_URL + link.get('href').replace(" ", "%20")
                for link in soup.select("p a")
                if link.get('href') and "fullpaper" in link.get('href')
            ]
            all_fullpaper_urls.extend(valid_links)
        else:
            print(f"Failed to fetch page {full_url}. Status code: {response.status_code}")

    return all_fullpaper_urls

def extract_pdf_text(pdf_url):
    """Extract text from the PDF."""
    response = requests.get(pdf_url)

    if response.status_code == 200:
        pdf_filename = os.path.join(PDF_DIR, os.path.basename(urlparse(pdf_url).path))
        with open(pdf_filename, 'wb') as pdf_file:
            pdf_file.write(response.content)

        doc = fitz.open(pdf_filename)
        text = ""
        for page in doc:
            page_text = page.get_text()
            text += page_text

        clean_text = re.sub(r'\s+', ' ', text.replace('\n', ' ')).strip()
        
        return clean_text

    else:
        print(f"Failed to download PDF from {pdf_url}, status code: {response.status_code}")
        return ""

def extract_abstract_details(abstract_urls):
    """Extract the details from each abstract URL."""
    abstract_details = []

    for abstract_url in abstract_urls:
        response = requests.get(abstract_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            try:
                title = soup.select_one("p:nth-of-type(1)").text.strip().replace("Abstract:", "") if soup.select_one("p:nth-of-type(1)") else None
                authors = soup.select_one("p:nth-of-type(2)").text.strip() if soup.select_one("p:nth-of-type(2)") else None
                abstract = soup.select_one("p:nth-of-type(5)").text.strip() if soup.select_one("p:nth-of-type(5)") else None
                keywords = soup.select_one("p:nth-of-type(6)").text.strip().replace("Keywords:", "").strip() if soup.select_one("p:nth-of-type(6)") else None
                fullpaper_link = soup.select_one("p:nth-of-type(7) a")
                fullpaper_url = BASE_URL + fullpaper_link.get('href').replace(" ", "%20") if fullpaper_link and fullpaper_link.get('href') else None

                abstract_details.append({
                    "url": abstract_url,
                    "title": title,
                    "authors": authors,
                    "abstract": abstract,
                    "keywords": keywords,
                    "fullpaper_url": fullpaper_url
                })
            except Exception as e:
                print(f"Error processing {abstract_url}: {e}")
        else:
            print(f"Failed to fetch {abstract_url}. Status code: {response.status_code}")

    return abstract_details

def get_fullpaper_details(abstract_details):
    """Extract full text from PDF and save details into fullpaper_details.json."""
    fullpaper_details = []

    for detail in abstract_details:
        fullpaper_url = detail.get("fullpaper_url", "")
        if fullpaper_url:
            full_text = extract_pdf_text(fullpaper_url)
            fullpaper_details.append({
                "url": detail.get("url"),
                "title": detail.get("title"),
                "authors": detail.get("authors"),
                "full_text": full_text,
                "keywords": detail.get("keywords")
            })
        else:
            print(f"No fullpaper URL found for {detail.get('title')}")

    return fullpaper_details

def main():
    """Main function to execute the entire scraping process."""
    # Part 1: Get all archive links
    all_urls = get_all_links()
    with open('archives_url.json', 'w') as f:
        json.dump(all_urls, f, indent=4)

    # Part 2: Get all abstract URLs
    all_abstract_urls = get_abstract_urls(all_urls)
    with open('abstracts_url.json', 'w') as f:
        json.dump(all_abstract_urls, f, indent=4)

    # Part 3: Get full paper URLs
    all_fullpaper_urls = get_fullpaper_urls(all_abstract_urls)
    with open('fullpaper_url.json', 'w') as f:
        json.dump(all_fullpaper_urls, f, indent=4)

    # Part 4: Get abstract details
    abstract_details = extract_abstract_details(all_abstract_urls)
    with open('abstract_details.json', 'w') as f:
        json.dump(abstract_details, f, indent=4)

    # Part 5: Get fullpaper details
    fullpaper_details = get_fullpaper_details(abstract_details)
    with open('fullpaper_details.json', 'w') as f:
        json.dump(fullpaper_details, f, indent=4)

    print("Scraping and extraction complete.")

if __name__ == "__main__":
    main()
