# Emilia Data-Speech

Data-Speech on Malaysian Emilia.

## how to

### Predict gender

```bash
CUDA_VISIBLE_DEVICES=2 \
python3.10 gender_prediction.py --path 'malaysian-podcast_processed_24k/**/*.mp3' --global-index 1 --local-index 0
```