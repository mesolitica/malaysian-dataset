# distributed multi-GPUs pseudolabel using Whisper

This pseudolabel included fast hashing load audio files and continue last step decoded.

## download

All data uploaded at https://huggingface.co/datasets/mesolitica/pseudolabel-malaysian-youtube-whisper-large-v3

## how-to

1. Generate chunks hash map, [generate-global-indices.ipynb](generate-global-indices.ipynb).

### Use torchrun

```bash
NCCL_P2P_DISABLE=1 NCCL_IB_DISABLE=1 ~/.local/bin/torchrun --nproc_per_node 2 \
-m run \
--indices_filename=indices-crawl-malaya-speech.json --batch_size=16
```

NCCL is not required.