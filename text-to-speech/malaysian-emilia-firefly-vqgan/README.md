# VQGAN

Convert speech to semantic token.

## how to

```bash
CUDA_VISIBLE_DEVICES=0 \
python3.10 vqgan-parquet.py \
--file /home/husein/ssd3/F5-TTS/gathered.parquet \
--output_folder output-vqgan \
--global-index 3 --local-index 0

CUDA_VISIBLE_DEVICES=1 \
python3.10 vqgan-parquet.py \
--file /home/husein/ssd3/F5-TTS/gathered.parquet \
--output_folder output-vqgan \
--global-index 3 --local-index 1

CUDA_VISIBLE_DEVICES=2 \
python3.10 vqgan-parquet.py \
--file /home/husein/ssd3/F5-TTS/gathered.parquet \
--output_folder output-vqgan \
--global-index 3 --local-index 2
```