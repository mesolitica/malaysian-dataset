# distributed multi-GPUs pseudolabel using Whisper on Malaysian Youtube videos

This pseudolabel included fast hashing load audio files and continue last step decoded.

## download

All data uploaded at https://huggingface.co/datasets/mesolitica/pseudolabel-malaysian-youtube-whisper-large-v3

## how-to

1. Prepare chunks hash map, [prepare-indices-chunks.ipynb](prepare-indices-chunks.ipynb).

2. Generate chunks hash map, [generate-global-indices.ipynb](generate-global-indices.ipynb).

### Use accelerate

1. Configure accelerate,

```bash
accelerate config
```

2. Run accelerate,

```bash
~/my-env/bin/accelerate launch run.py --indices_filename=global-indices.json --batch_size=4
```

### Use torchrun

```bash
NCCL_P2P_DISABLE=1 NCCL_IB_DISABLE=1 ~/my-env/bin/torchrun --nproc_per_node 2 \
-m run \
--indices_filename=global-indices.json --batch_size=4
```

NCCL is not required.

#### Run in 4x A100

We use batch size of 52,

```bash
NCCL_P2P_DISABLE=1 NCCL_IB_DISABLE=1 torchrun --nproc_per_node 4 \
-m run \
--indices_filename=crawl-youtube-global-indices.json --batch_size=52
```

### Predict language using Speechbrain

```bash
NCCL_P2P_DISABLE=1 NCCL_IB_DISABLE=1 torchrun --nproc_per_node 4 \
-m run-predict-lang \
--batch_size=32
```