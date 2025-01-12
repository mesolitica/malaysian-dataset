## how to force alignment

```bash
for i in {0..3}; do
  screen -S "run2_$i" -X quit 2>/dev/null
  screen -dmS "run2_$i" bash -c "cd /home/husein/ssd4 && \
  CUDA_VISIBLE_DEVICES=2 \
  python3.10 force_alignment_stt.py \
  --file 'prepared-pseudolabel.jsonl' \
  --global-index 4 \
  --local-index $i"
done

for i in {0..3}; do
  screen -S "run3_$i" -X quit 2>/dev/null
  screen -dmS "run3_$i" bash -c "cd /home/husein/ssd4/youtube && \
  CUDA_VISIBLE_DEVICES=2 \
  python3.10 force_alignment_stt.py \
  --file 'dataset-podcast.jsonl' \
  --global-index 4 \
  --local-index $i"
done

for i in {0..3}; do
  screen -S "run3_$i" -X quit 2>/dev/null
  screen -dmS "run3_$i" bash -c "cd /home/husein/ssd4 && \
  CUDA_VISIBLE_DEVICES=2 \
  python3.10 force_alignment_stt.py \
  --file 'prepared-imda.jsonl' \
  --global-index 4 \
  --local-index $i"
done

for i in {0..3}; do
  screen -S "run3_$i" -X quit 2>/dev/null
  screen -dmS "run3_$i" bash -c "cd /home/husein/ssd4/pseudolabel-science-large-v3-timestamp && \
  CUDA_VISIBLE_DEVICES=2 \
  python3.10 force_alignment_stt.py \
  --file 'science-en-stt.jsonl' \
  --global-index 4 \
  --local-index $i"
done
```