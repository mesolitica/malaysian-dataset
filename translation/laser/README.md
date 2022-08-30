# LASER for eng_Latn-zsm_Latn

Original dataset at https://github.com/facebookresearch/LASER/tree/main/data/nllb200#data

**Update, AllenNLP released NLLB dataset at https://huggingface.co/datasets/allenai/nllb**.

## how-to

1. Install dependencies,

```
sudo apt-get install libcurl4-openssl-dev
git clone https://github.com/kpuatfb/preprocess.git
cd preprocess
git checkout wet
mkdir build
cd build
git clone https://github.com/Cyan4973/xxHash
mkdir xxHash/build
cd xxHash/build
cmake ../cmake_unofficial
cmake --build .
cd ../..
cmake ..
make -j4
git clone https://github.com/facebookresearch/LASER.git
cd LASER/utils
pip3 install -e . --user
cd ../..
```

2. Download dataset from https://github.com/facebookresearch/LASER/tree/main/data/nllb200#data, i choose [eng_Latn-zsm_Latn](https://dl.fbaipublicfiles.com/nllb/data/eng_Latn-zsm_Latn.meta.v1.xz).

3. Run LASER,

```bash
xzcat eng_Latn-zsm_Latn.meta.v1.xz | egrep ^crawl-data | ~/preprocess/build/bin/wet_lines | python3 ~/preprocess/build/LASER/utils/src/cleaner_splitter.py > eng_Latn-zsm_Latn
```

## how-to distribute

**Required redis**.

1. filter metadata,

```
xzcat eng_Latn-zsm_Latn.meta.v1.xz | egrep ^crawl-data > eng_Latn-zsm_Latn.meta
mkdir splitted
cd splitted
split -l 1000000 -d --additional-suffix=.split ../eng_Latn-zsm_Latn.meta eng_Latn-zsm_Latn.meta
```

2. Groupby sha1 and parapgraphs, [gather-warc.ipynb](gather-warc.ipynb).

3. Split JSONL,

```bash
mkdir splitted-jsonl
cd splitted-jsonl
split -l 200000 -d --additional-suffix=.split ../warcs-eng_Latn-zsm_Latn.jsonl warcs-eng_Latn-zsm_Latn.jsonl
```

4. Run [distribute-laser-nllb200.ipynb](distribute-laser-nllb200.ipynb) for each splitted files.

## Citation

```bibtex
@article{DBLP:journals/corr/abs-1812-10464,
  author    = {Mikel Artetxe and
               Holger Schwenk},
  title     = {Massively Multilingual Sentence Embeddings for Zero-Shot Cross-Lingual
               Transfer and Beyond},
  journal   = {CoRR},
  volume    = {abs/1812.10464},
  year      = {2018},
  url       = {http://arxiv.org/abs/1812.10464},
  eprinttype = {arXiv},
  eprint    = {1812.10464},
  timestamp = {Wed, 02 Jan 2019 14:40:18 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1812-10464.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```