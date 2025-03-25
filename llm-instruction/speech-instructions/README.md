# Speech Instructions

## how to prepare

### 1. Speaker dedup

1. Prepare dataset to dedup,

- [prepare-malaysia-parliament.ipynb](prepare-malaysia-parliament.ipynb).
- [prepare-malaysian-podcast.ipynb](prepare-malaysian-podcast.ipynb).
- [prepare-malaysian-others.ipynb](prepare-malaysian-others.ipynb).

2. Convert to embedding,

We use speaker embedding from https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/titanet_large

```bash
CUDA_VISIBLE_DEVICES=1,2 \
python3.10 embedding.py \
--filename filtered-politicians.parquet \
--replication 3

CUDA_VISIBLE_DEVICES=1,2 \
python3.10 embedding.py \
--filename filtered-podcast.parquet \
--replication 3 --folder embedding-podcast

CUDA_VISIBLE_DEVICES=0,2 \
python3.10 embedding.py \
--filename filtered-others.parquet \
--replication 3 --folder embedding-others
```

2. Merge and dedup,

- [dedup-parliament.ipynb](dedup-parliament.ipynb).
- [dedup-podcasts.ipynb](dedup-podcasts.ipynb).

### 2. Populate instructions

All datasets from https://huggingface.co/collections/mesolitica/malaysian-synthetic-dataset-656c2673fe7fe0b1e9e25fe2, and follow [filter-instructions.ipynb](filter-instructions.ipynb).

### 3. Generate synthetic voice

```bash
bash generate.sh
```

**Modify it appropriately based on your local GPUs**.