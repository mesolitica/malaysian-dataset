for i in {0..3}; do
  screen -S "partition-instructions-part-7_$i" -X quit 2>/dev/null
  screen -dmS "partition-instructions-part-7_$i" bash -c "cd /home/husein/ssd3/dataset/speech-instructions && \
  CUDA_VISIBLE_DEVICES=0 \
  python3.10 generate.py \
    --input_file \"partition-instructions-part-7.json\" \
    --folder \"partition-instructions-part-7\" \
    --global_index 4 \
    --index $i"
done

for i in {0..3}; do
  screen -S "partition-instructions-part-15_$i" -X quit 2>/dev/null
  screen -dmS "partition-instructions-part-15_$i" bash -c "cd /home/husein/ssd3/dataset/speech-instructions && \
  CUDA_VISIBLE_DEVICES=2 \
  python3.10 generate.py \
    --input_file \"partition-instructions-part-15.json\" \
    --folder \"partition-instructions-part-15\" \
    --global_index 4 \
    --index $i"
done

for i in {0..3}; do
  screen -S "tatabahasa_$i" -X quit 2>/dev/null
  screen -dmS "tatabahasa_$i" bash -c "cd /home/husein/ssd3/dataset/speech-instructions && \
  CUDA_VISIBLE_DEVICES=2 \
  python3.10 generate.py \
    --input_file \"tatabahasa.json\" \
    --folder \"tatabahasa-v2\" \
    --global_index 4 \
    --index $i --threshold -9 --maxlen 300 --retry 10"
done

for i in {0..3}; do
  screen -S "malaymmlu_$i" -X quit 2>/dev/null
  screen -dmS "malaymmlu_$i" bash -c "cd /home/husein/ssd3/dataset/speech-instructions && \
  CUDA_VISIBLE_DEVICES=2 \
  python3.10 generate.py \
    --input_file \"malaymmlu.json\" \
    --folder \"malaymmlu\" \
    --global_index 4 \
    --index $i --threshold -9 --maxlen 300 --retry 10"
done