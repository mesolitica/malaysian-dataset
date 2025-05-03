# Pseudolabel Whisper Non-verbal

## how to

```bash
CUDA_VISIBLE_DEVICES='0,1,2' \
python3.10 pseudolabel_nonverbal.py \
--file 'verify-text.parquet' \
--folder 'pseudolabel_nonverbal' \
--replication 3
```