from io import BytesIO
from PIL import Image
import mp
from glob import glob
import pandas as pd
from streaming import MDSWriter
from streaming.base.format.mds.encodings import Encoding, _encodings
from streaming import LocalDataset
import streaming
import numpy as np
import json
import os
from tqdm import tqdm
from huggingface_hub import snapshot_download
from sklearn.metrics.pairwise import cosine_similarity


class Float32(Encoding):
    def encode(self, obj) -> bytes:
        return obj.tobytes()

    def decode(self, data: bytes):
        return np.frombuffer(data, np.float32)


def deduplicate(similarity_matrix, threshold=0.5):
    unique_indices = []
    for i, vector in enumerate(similarity_matrix):
        is_duplicate = False
        for j in unique_indices:
            if similarity_matrix[i, j] >= threshold:
                is_duplicate = True
                break
        if not is_duplicate:
            unique_indices.append(i)
    return unique_indices


def loop(files):
    files, index = files
    dataset = LocalDataset('combine')
    for f in tqdm(files):
        f_ = os.path.split(f)[1]
        r = []
        df = pd.read_parquet(f)
        keywords = df['keyword'].unique().tolist()
        for no, k in enumerate(keywords):

            filename = os.path.join('output', f'{f_}-{no}.json')
            if os.path.exists(filename):
                continue

            small_df = df[df['keyword'] == k]
            indices = small_df.index
            selected_indices, embedding = [], []
            for i in indices:
                key = f'{os.path.split(f)[1]}-{i}'
                if key not in mapping:
                    continue
                row = dataset[mapping[key]]
                if row['label'] == 'scenery':
                    selected_indices.append(i)
                    embedding.append(row['embedding'])

            if not len(embedding):
                selected_indices = []
            else:
                similarity = cosine_similarity(embedding)
                dedup = deduplicate(similarity)
                selected_indices = [selected_indices[i] for i in dedup]

            with open(filename, 'w') as fopen:
                json.dump({'filename': f_, 'keyword': k, 'no': no,
                          'selected_indices': selected_indices}, fopen)


_encodings['float32'] = Float32

with open('mapping-index.json') as fopen:
    mapping = json.load(fopen)


folder = snapshot_download(
    repo_id="malaysia-ai/crawl-google-image-malaysia-location",
    repo_type='dataset')
files = glob(f'{folder}/data/*.parquet')
files = sorted(files, key=lambda x: int(x.split('/')[-1].split('-')[1]))
results = mp.multiprocessing(files, loop, cores=20, returned=False)
