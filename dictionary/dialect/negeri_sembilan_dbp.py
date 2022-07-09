import time
from selenium import webdriver
import json

count = 2
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery");
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome('../chromedriver', chrome_options=chrome_options)
driver.delete_all_cookies()

driver.get('http://prpm.dbp.gov.my/Cari1.aspx?keyword=%3d&d=259120&#LIHATSINI')

results = []

def get_page():
    while True:

        try:
            t = driver.find_element_by_xpath('//*[@id="MainContent_GridView1"]')
            print(t)
            return t.get_attribute('innerHTML')
        except Exception as e:
            print(e)
            time.sleep(3)


while True:
    results.append(get_page())
    p = '//*[@id="MainContent_GridView1"]/tbody/tr[12]/td/table/tbody/tr/td[%d]/a'%(count)
    print(p)
    if count < 11:
        count += 1
    try:
        e = driver.find_element_by_xpath(p)
        driver.execute_script("arguments[0].click();", e)
    except:
        break

with open('negeri_sembilan.json', 'w') as fopen:
    json.dump(results, fopen)