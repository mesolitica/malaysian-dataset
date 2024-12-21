import os
import zipfile
import mp
from datetime import datetime
from glob import glob
from tqdm import tqdm
from huggingface_hub import HfApi
from huggingface_hub import HfFileSystem
import time

partition_size = 5e+9

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size

def loop(files):
    files, index = files
    current_index = 0
    api = HfApi()
    fs = HfFileSystem()
    total = 0
    temp = []
    for i in tqdm(range(len(files))):
        s = get_size(files[i])
        if s + total >= partition_size:
            part_name = f"dialects-processed-{index}-{current_index}.zip"
                
            with zipfile.ZipFile(part_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for folder in temp:
                    for root, dirs, files in os.walk(folder):
                        for f in files:
                            f = os.path.join(root, f)
                            zipf.write(f, arcname=f)

            while True:
                try:
                    api.upload_file(
                        path_or_fileobj=part_name,
                        path_in_repo=part_name,
                        repo_id="mesolitica/Malaysian-Emilia",
                        repo_type="dataset",
                    )
                    break
                except:
                    time.sleep(60)

            os.remove(part_name)
            
            current_index += 1
            temp = [files[i]]
            total = s
        else:
            temp.append(files[i])
            total += s
        
    if len(temp):
        part_name = f"dialects-processed-{index}-{current_index}.zip"

        with zipfile.ZipFile(part_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for folder in temp:
                for root, dirs, files in os.walk(folder):
                    for f in files:
                        f = os.path.join(root, f)
                        zipf.write(f, arcname=f)

        while True:
            try:
                api.upload_file(
                    path_or_fileobj=part_name,
                    path_in_repo=part_name,
                    repo_id="mesolitica/Malaysian-Emilia",
                    repo_type="dataset",
                )
                break
            except:
                time.sleep(60)

        os.remove(part_name)

while True:
    try:
        folders = sorted(glob('dialects_processed/*'))
        print(datetime.now(), len(folders))
        mp.multiprocessing(folders, loop, cores = 10, returned = False)
    except Exception as e:
        print(e)

    time.sleep(10800)