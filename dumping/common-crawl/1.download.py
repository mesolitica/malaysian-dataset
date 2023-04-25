import gzip
import urllib.request
import collections
import os
from tqdm import tqdm

# !wget https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2022-49/cc-index.paths.gz
# !gzip -d cc-index.paths.gz

storage_folder = 'data/'
file_prefix = 'https://data.commoncrawl.org/'

os.makedirs(storage_folder, exist_ok=True)


def save(url, filename):
    urllib.request.urlretrieve(url, filename)


def read_every_line(fname,
                    max_lines=-1):
    lines = []
    with open(fname, encoding='utf-8') as f:
        for i, l in enumerate(f):
            lines.append(l)
            if i > max_lines and max_lines > 0:
                break
    return lines


cc_indexes = read_every_line('cc-index.paths')
cc_indexes = cc_indexes[:-2]
cc_indexes = [_.replace('\n', '') for _ in cc_indexes]
cc_indexes[:5]

file_dict = collections.OrderedDict()

for i, cc_index in enumerate(cc_indexes):
    if i > 75:
        cc_index_file = cc_index.split('/')[-1]
        file_dict[os.path.join(storage_folder, cc_index_file)] = file_prefix + cc_index
    else:
        pass

for i, (file_name, url) in enumerate(tqdm(file_dict.items())):
    print('PROCESSING INDEX FILE [{}]/[{}] ...'.format(i, len(file_dict)))
    print('Downloading an index file {} ...'.format(file_name))
    if os.path.exists(file_name):
        continue
    save(url, file_name)
