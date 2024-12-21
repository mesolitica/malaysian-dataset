from glob import glob
from tqdm import tqdm
from multiprocess import Pool
import itertools
import zipfile
import os

def chunks(l, n):
    for i in range(0, len(l), n):
        yield (l[i: i + n], i // n)


def multiprocessing(strings, function, cores=6, returned=True):
    df_split = chunks(strings, len(strings) // cores)
    pool = Pool(cores)
    pooled = pool.map(function, df_split)
    pool.close()
    pool.join()

    if returned:
        return list(itertools.chain(*pooled))

def main():
    files = glob('*.zip')

    def loop(files):
        files, _ = files
        for zip_file_path in tqdm(files):
            destination_folder = './'
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(destination_folder)
            os.remove(zip_file_path)
        
    multiprocessing(files, loop, cores = 40, returned = False)

if __name__ == '__main__':
    main()