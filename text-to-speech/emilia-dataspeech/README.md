# Emilia Data-Speech

Data-Speech on Malaysian Emilia.

## how to

### Predict gender

```bash
CUDA_VISIBLE_DEVICES=0 \
python3.10 gender_prediction.py --path 'malaysian-podcast_processed_24k/**/*.mp3' --global-index 1 --local-index 0
```

### Predict language

```bash
CUDA_VISIBLE_DEVICES=0 \
python3.10 language_prediction.py --path 'sg-podcast_processed/**/*.mp3' --global-index 1 --local-index 0
CUDA_VISIBLE_DEVICES=1 \
python3.10 language_prediction.py --path 'parlimen-24k-chunk_processed/**/*.mp3' --global-index 1 --local-index 0
CUDA_VISIBLE_DEVICES=2 \
python3.10 language_prediction.py --path 'filtered-24k_processed/**/*.mp3' --global-index 1 --local-index 0
CUDA_VISIBLE_DEVICES=2 \
python3.10 language_prediction.py --path 'dialects_processed/**/*.mp3' --global-index 1 --local-index 0
```

### Data-Speech

```bash
git clone https://github.com/huggingface/dataspeech
cd dataspeech
```

### Force alignment

```bash
for i in {0..3}; do
  screen -S "run0_$i" -X quit 2>/dev/null
  screen -dmS "run0_$i" bash -c "cd /home/husein/ssd4 && \
  CUDA_VISIBLE_DEVICES=0 \
  python3.10 force_alignment.py \
  --path 'parlimen-24k-chunk_processed/**/*.mp3' \
  --global-index 4 \
  --local-index $i"
done

for i in {0..3}; do
  screen -S "run1_$i" -X quit 2>/dev/null
  screen -dmS "run1_$i" bash -c "cd /home/husein/ssd4 && \
  CUDA_VISIBLE_DEVICES=1 \
  python3.10 force_alignment.py \
  --path 'filtered-24k_processed/**/*.mp3' \
  --global-index 4 \
  --local-index $i"
done

for i in {0..5}; do
  screen -S "run2_$i" -X quit 2>/dev/null
  screen -dmS "run2_$i" bash -c "cd /home/husein/ssd3 && \
  CUDA_VISIBLE_DEVICES=2 \
  python3.10 force_alignment.py \
  --path 'dialects_processed/**/*.mp3' \
  --global-index 6 \
  --local-index $i"
done
```