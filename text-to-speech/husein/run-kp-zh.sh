apt update
apt install screen ffmpeg -y

cd /workspace
wget https://github.com/mesolitica/malaysian-dataset/raw/refs/heads/master/text-to-speech/husein/requirements.txt
pip3 install -r requirements.txt
pip3 install vocos torchdiffeq==0.2.4 x-transformers==1.42.11 jieba==0.42.1 pypinyin==0.53.0

wget https://github.com/mesolitica/malaysian-dataset/raw/refs/heads/master/text-to-speech/husein/generate_zh.py
wget https://huggingface.co/datasets/mesolitica/TTS/resolve/main/kp-rtm-enhanced-v2.wav
wget https://huggingface.co/datasets/mesolitica/TTS/resolve/main/texts/alpaca-chinese.json
wget https://huggingface.co/datasets/mesolitica/TTS/resolve/main/texts/chinese-texts-part2.json
wget https://huggingface.co/datasets/mesolitica/TTS/resolve/main/texts/chinese-texts-part3.json
wget https://huggingface.co/datasets/mesolitica/TTS/resolve/main/texts/chinese-texts-part4.json

for i in {0..3}; do
  screen -S "run_alpaca-chinese_$i" -X quit 2>/dev/null
  screen -dmS "run_alpaca-chinese_$i" bash -c "cd /workspace && \
  CUDA_VISIBLE_DEVICES=0 \
  python3 generate_zh.py \
    --voice \"kp-rtm-enhanced-v2.wav\" \
    --original_text \"Selalunya kalau kita pergi berjumpa media kan, kalau kita pergi buat produk launch ke dan sebagainya, selalunya, dia siapkan barang itu dulu, atau apa yang kita nak jual kepada dunia,\" \
    --text_file \"alpaca-chinese.json\" \
    --folder \"kp-alpaca-chinese\" \
    --global_index 4 \
    --index $i --threshold -12"
done

for i in {0..3}; do
  screen -S "run_kp-chinese-texts-part2_$i" -X quit 2>/dev/null
  screen -dmS "run_kp-chinese-texts-part2_$i" bash -c "cd /workspace && \
  CUDA_VISIBLE_DEVICES=1 \
  python3 generate_zh.py \
    --voice \"kp-rtm-enhanced-v2.wav\" \
    --original_text \"Selalunya kalau kita pergi berjumpa media kan, kalau kita pergi buat produk launch ke dan sebagainya, selalunya, dia siapkan barang itu dulu, atau apa yang kita nak jual kepada dunia,\" \
    --text_file \"chinese-texts-part2.json\" \
    --folder \"kp-chinese-texts-part2\" \
    --global_index 4 \
    --index $i --threshold -12"
done