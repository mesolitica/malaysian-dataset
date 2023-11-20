import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import re
import time
import fitz  # PyMuPDF
import os
import json

def get_download_links(url):
    # Send a GET request to the page
    response = requests.get(url)
    # If the request was successful, proceed to parse the content
    if response.status_code == 200:
        # Create a BeautifulSoup object and specify the parser
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all table rows in the table
        rows = soup.find_all('tr')
        # Iterate over each row to find the `a` tags and extract the `href`
        links = []
        subjects = []
        pattern = r'[^a-zA-Z]'
        for row in rows:
            subject = row.find('td').get_text().strip().strip()
            if bool(re.search(r'\d\.', subject)):
                # Find all `a` tags in the row
                a_tags = row.find_all('a')
                for a in a_tags:
                    # Check if the `a` tag has an `href` attribute and add it to the list
                    if a.has_attr('href'):
                        if 'drive.google.com' in a['href']:
                            links.append(a['href'])
                            subjects.append(re.sub(pattern, '', subject))
    else:
        print(f"Failed to retrieve the webpage, status code: {response.status_code}")
    return links, subjects

def download_file_from_google_drive(id, destination):
    time.sleep(30)
    URL = "https://drive.google.com/uc?export=download"
    session = requests.Session()

    response = session.get(URL, params={'id': id})
    
    if 'content-disposition' in response.headers:
        save_response_content(response, destination)
    else:
        form_data = extract_form_data(response.text, id)
        if form_data:
            response = session.post(URL, data=form_data, stream=True)
            save_response_content(response, destination)
        else:
            print(f"Failed to download {id}: Unable to extract form data.")

def extract_form_data(html_content, file_id):
    soup = BeautifulSoup(html_content, 'lxml')
    form = soup.find('form')
    if form:
        action = form.get('action')
        uuid_match = re.search(r'uuid=([^&]+)', action)
        uuid = uuid_match.group(1) if uuid_match else None

        # Assuming 'confirm' parameter is always 't'
        return {'id': file_id, 'confirm': 't', 'uuid': uuid}
    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

def download_kssr(url, destination):
    links, subjects = get_download_links(url)
    for i, link in tqdm(enumerate(links), total=len(links)):
        file_id = link.split('/')[-2]
        try:
            download_file_from_google_drive(file_id, f'{destination}/kssr_{subjects[i]}_{file_id}.pdf')
        except Exception as e:
            print(f"Failed to download {file_id}: {e}")

def download_kssm(url, destination):
    links, subjects = get_download_links(url)
    for i, link in tqdm(enumerate(links), total=len(links)):
        if 'id=' in link:
            file_id = link.split('id=')[-1]
        elif 'file/d/' in link:
            file_id = link.split('/')[-2]
        elif 'folders' in link:
            continue
        try:
            download_file_from_google_drive(file_id, f'{destination}/kssm_{subjects[i]}_{file_id}.pdf')
        except Exception as e:
            print(f"Failed to download {file_id}: {e}")

def retrive_text(folder):
    texts = []
    for file in tqdm(os.listdir(folder), total=len(os.listdir(folder))):
        if file.endswith(".pdf"):
            try:
                doc = fitz.open(f"{folder}/{file}")
                # Extract text from each page
                pages = []
                for page in doc:
                    pages.append(page.get_text())
                all_text = " ".join(pages)
                book_name = file.split.split('.')[0]
                texts.append({'book': file, 'content': all_text})
            except Exception as e:
                print(f"Failed to extract text from {file}: {e}")
    return texts

def save_json(posts):
    with open('malaysia_textbook.jsonl', 'a') as f:
        json.dump(posts, f)

if __name__ == "__main__":
    url = 'https://www.ipendidikan.my/buku-teks-digital-kssr-tahun-1-hingga-6.html'
    url2 = 'https://www.ipendidikan.my/koleksi-buku-teks-digital-asas-kssm.html'
    destination = f'pdfs'
    download_kssr(url, destination)
    download_kssm(url2, destination)
    data = retrive_text(destination)
    save_json(data)
