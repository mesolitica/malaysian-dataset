from selenium import webdriver
import threading
from queue import Queue
from tqdm import tqdm
import warnings
import time
import urllib.parse

warnings.filterwarnings('ignore')

# er8xn
span = '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span'


class Translate:
    def __init__(self, from_lang, to_lang):
        self.driver = webdriver.PhantomJS()
        self.driver.set_page_load_timeout(120)
        self.url = f'https://translate.google.com/?sl={from_lang}&tl={to_lang}&op=translate'
        self.driver.get(self.url)

    def translate(self, string):
        s = urllib.parse.quote(string)
        self.driver.get(f'{self.url}&text={s}')
        time.sleep(5.5)
        text = [elem.text for elem in self.driver.find_elements_by_xpath(span)]
        if len(text):
            return (string, ' '.join(text))
        else:
            return None


def task_translate(translator, string):
    return translator.translate(string)


def run_parallel_in_threads(args_list, target = task_translate):
    globalparas = [None] * len(args_list)
    result = Queue()

    def task_wrapper(*args):
        result.put((target(*args), args_list.index(args)))

    threads = [
        threading.Thread(target = task_wrapper, args = args)
        for args in args_list
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    while not result.empty():
        res = result.get()
        globalparas.insert(res[1], res[0])
    globalparas = list(filter(None, globalparas))
    return globalparas


class Translate_Concurrent:
    def __init__(self, batch_size, from_lang = 'en', to_lang = 'ms'):
        self._batch_size = batch_size
        self._translators = [
            Translate(from_lang, to_lang) for _ in range(self._batch_size)
        ]

    def translate_batch(self, strings):
        translated = []
        for no in tqdm(range(0, len(strings), self._batch_size), ncols = 70):
            data = strings[no : no + self._batch_size]
            combined = [
                (self._translators[i], data[i]) for i in range(len(data))
            ]
            translated.extend(run_parallel_in_threads(combined))
        return translated
