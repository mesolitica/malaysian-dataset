from bs4 import BeautifulSoup
from tqdm import tqdm
import json
from selenium import webdriver
import time
urls = [
    "https://masabih.org/mishkat/introduction",
    "https://masabih.org/mishkat/kitab-iman",
    "https://masabih.org/mishkat/kitab-ilmu",
    "https://masabih.org/mishkat/kitab-bersuci",
    "https://masabih.org/mishkat/kitab-solat",
    "https://masabih.org/mishkat/kitab-jenazah",
    "https://masabih.org/mishkat/kitab-zakat",
    "https://masabih.org/mishkat/kitab-puasa",
    "https://masabih.org/mishkat/kitab-fadhilat-quran",
    "https://masabih.org/mishkat/kitab-doa",
    "https://masabih.org/mishkat/kitab-haji-dan-umrah",
    "https://masabih.org/mishkat/kitab-jual-beli",
    "https://masabih.org/mishkat/kitab-faraidh-dan-wasiat",
    "https://masabih.org/mishkat/kitab-nikah",
    "https://masabih.org/mishkat/kitab-merdeka-hamba",
    "https://masabih.org/mishkat/kitab-sumpah-dan-nazar",
    "https://masabih.org/mishkat/kitab-qisas",
    "https://masabih.org/mishkat/kitab-hudud",
    "https://masabih.org/mishkat/kitab-kepimpinan-dan-kehakiman",
    "https://masabih.org/mishkat/kitab-jihad",
    "https://masabih.org/mishkat/kitab-penyembelihan",
    "https://masabih.org/mishkat/kitab-makanan",
    "https://masabih.org/mishkat/kitab-pakaian",
    "https://masabih.org/mishkat/kitab-perubatan-dan-jampian",
    "https://masabih.org/mishkat/kitab-mimpi",
    "https://masabih.org/mishkat/kitab-adab",
    "https://masabih.org/mishkat/kitab-fitan",
    "https://masabih.org/mishkat/kitab-riqaq",
    "https://masabih.org/mishkat/kitab-keadaan-qiamat",
    "https://masabih.org/mishkat/kitab-fadhail-dan-shamail",
    "https://masabih.org/mishkat/kitab-manaqib",
    ]
def get_texts(soup, name, class_):
    divs = soup.find_all(name, class_=class_)
    return [div.get_text(separator='\n').strip() for div in divs]
with open('mishkat_al_masabih.jsonl', 'w') as fopen:
    driver = webdriver.Chrome()
    for url in tqdm(urls):
        print(f"Scraping {url}")
        driver.get("https://masabih.org/") # page redirect if access url directly
        time.sleep(1) # let js run
        driver.get(url)
        time.sleep(4) # let js run
        prev_height = -1
        for i in range(30):
            for j in range(5):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2) # let js run
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == prev_height:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1) # let js run
                break
            prev_height = new_height
        soup = BeautifulSoup(driver.page_source, "lxml")
        if url == "https://masabih.org/mishkat/introduction":
            texts_ar = get_texts(soup, "div", "col-lg-6 pl-lg-5 arabic text-details long_text font22 order-1 order-lg-2")
            texts_bm = get_texts(soup, "div", "col-lg-6 pt-lg-0 pt-3 english text-details long_text font15 order-2 order-lg-1")
            for i, (text_ar, text_bm) in enumerate(zip(texts_ar, texts_bm)):
                fopen.write(f'''{json.dumps({
                    'url': url,
                    'title': soup.find('title').text.replace("Masabih | ", ""),
                    'paragraph_number': str(i+1),
                    'ar': text_ar,
                    'bm': text_bm,
                    'syarh_bm': "",
                    'status': "",
                    'info': "",
                })}\n''')
            print(f"{len(texts_ar)=}, {len(texts_bm)=}")
        else:
            texts_ar = get_texts(soup, "div", "arabic text-details long_text hadith_arab")
            texts_bm = get_texts(soup, "div", "english text-details long_text hadith_trans bm")
            texts_syarh = get_texts(soup, "span", "long_text hadith_syarh bm")
            texts_status = get_texts(soup, "span", "hadith_status")
            texts_info = [t.replace(":\n","") for t in get_texts(soup, "div", "col-9 line-height-1 pl-0")]
            for i, (text_ar, text_bm, text_syarh, text_status, text_info) in enumerate(zip(texts_ar, texts_bm, texts_syarh, texts_status, texts_info)):
                fopen.write(f'''{json.dumps({
                    'url': url,
                    'title': soup.find('title').text.replace("Masabih | ", ""),
                    'paragraph_number': str(i+1),
                    'ar': text_ar,
                    'bm': text_bm,
                    'syarh_bm': text_syarh,
                    'status': text_status,
                    'info': text_info,
                })}\n''')
            print(f"{len(texts_ar)=}, {len(texts_bm)=}, {len(texts_syarh)=}, {len(texts_info)=}")
        
    driver.quit()    