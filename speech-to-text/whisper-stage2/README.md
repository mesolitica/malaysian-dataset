# STT Whisper Stage 2

1. We provide segment and word level timestamps on,
- [Malaysian Emilia Dialects](https://huggingface.co/datasets/mesolitica/Malaysian-Emilia#malaysian-dialect).
- [Speech Instructions](https://huggingface.co/datasets/mesolitica/Speech-Instructions).
2. Synthetic merging different context, [synthetic-context-switching-word-timestamp.ipynb](synthetic-context-switching-word-timestamp.ipynb).

## Sliding Audionet

```bash
CUDA_VISIBLE_DEVICES=0 \
python3 audioset_sliding.py --file 'prepared-pseudolabel.jsonl' --global-index 4 --local-index 0
CUDA_VISIBLE_DEVICES=1 \
python3 audioset_sliding.py --file 'prepared-pseudolabel.jsonl' --global-index 4 --local-index 1
CUDA_VISIBLE_DEVICES=2 \
python3 audioset_sliding.py --file 'prepared-pseudolabel.jsonl' --global-index 4 --local-index 2
CUDA_VISIBLE_DEVICES=3 \
python3 audioset_sliding.py --file 'prepared-pseudolabel.jsonl' --global-index 4 --local-index 3
```

## Speech Instructions

1. Run force alignment,

```bash
CUDA_VISIBLE_DEVICES=2 \
python3.10 force_alignment.py \
--filename 'prepare-force-alignment.json' \
--language 'ms' \
--replication 3
```

2. Prepare dataset,

- Segment level, [speech-instructions-segment-timestamps.ipynb](speech-instructions-segment-timestamps.ipynb).
- Word level, [speech-instructions-word-timestamps.ipynb](speech-instructions-word-timestamps.ipynb).

## Malaysian Emilia Dialects

1. Prepare dataset,

Because force alignment already calculated at [mesolitica/Malaysian-Emilia-annotated/dialects_processed_alignment.zip](https://huggingface.co/datasets/mesolitica/Malaysian-Emilia-annotated/blob/main/dialects_processed_alignment.zip).

- Segment level, [dialects-segment-timestamps.ipynb](dialects-segment-timestamps.ipynb).
- Word level, [dialects-word-timestamps.ipynb](dialects-word-timestamps.ipynb).