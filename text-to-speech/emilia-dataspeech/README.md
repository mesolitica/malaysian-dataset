# Emilia Data-Speech

Data-Speech on Malaysian Emilia.

## how to

### Predict gender

```bash
CUDA_VISIBLE_DEVICES=0 \
python3.10 gender_prediction.py --path 'malaysian-podcast_processed_24k/**/*.mp3' --global-index 1 --local-index 0
```

### Data-Speech

```bash
git clone https://github.com/huggingface/dataspeech
cd dataspeech
```