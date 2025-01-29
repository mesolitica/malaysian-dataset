apt update
apt install screen ffmpeg -y

cd /workspace
wget https://github.com/mesolitica/malaysian-dataset/raw/refs/heads/master/text-to-speech/husein/requirements.txt
pip3 install -r requirements.txt
pip3 install vocos torchdiffeq==0.2.4 x-transformers==1.42.11 jieba==0.42.1 pypinyin==0.53.0

wget https://github.com/mesolitica/malaysian-dataset/raw/refs/heads/master/text-to-speech/husein/generate.py
wget https://huggingface.co/datasets/mesolitica/TTS/resolve/main/kp-rtm-enhanced-v2.wav
wget https://huggingface.co/datasets/mesolitica/TTS/resolve/main/texts/news-berita-politik.json
wget https://huggingface.co/datasets/mesolitica/TTS/resolve/main/texts/chatbot-conversation-politics.json
wget https://huggingface.co/datasets/mesolitica/TTS/resolve/main/texts/chatbot-conversation.json
wget https://huggingface.co/datasets/mesolitica/TTS/resolve/main/texts/news-berita-bisnes.json
wget https://huggingface.co/datasets/mesolitica/TTS/resolve/main/texts/news-gaya-hidup.json
wget https://huggingface.co/datasets/mesolitica/TTS/resolve/main/texts/news-berita-sukan.json
wget https://huggingface.co/datasets/mesolitica/TTS/resolve/main/texts/news-berita-malaysia.json

for i in {0..3}; do
  screen -S "run_politik_$i" -X quit 2>/dev/null
  screen -dmS "run_politik_$i" bash -c "cd /workspace && \
  CUDA_VISIBLE_DEVICES=0 \
  python3 generate.py \
    --voice \"kp-rtm-enhanced-v2.wav\" \
    --original_text \"Selalunya kalau kita pergi berjumpa media kan, kalau kita pergi buat produk launch ke dan sebagainya, selalunya, dia siapkan barang itu dulu, atau apa yang kita nak jual kepada dunia,\" \
    --text_file \"news-berita-politik.json\" \
    --folder \"kp-berita-politik\" \
    --global_index 4 \
    --index $i --threshold -9"
done

for i in {0..3}; do
  screen -S "run_bisnes_$i" -X quit 2>/dev/null
  screen -dmS "run_bisnes_$i" bash -c "cd /workspace && \
  CUDA_VISIBLE_DEVICES=1 \
  python3 generate.py \
    --voice \"kp-rtm-enhanced-v2.wav\" \
    --original_text \"Selalunya kalau kita pergi berjumpa media kan, kalau kita pergi buat produk launch ke dan sebagainya, selalunya, dia siapkan barang itu dulu, atau apa yang kita nak jual kepada dunia,\" \
    --text_file \"news-berita-bisnes.json\" \
    --folder \"kp-berita-bisnes\" \
    --global_index 4 \
    --index $i --threshold -9"
done

for i in {0..3}; do
  screen -S "run_gaya_$i" -X quit 2>/dev/null
  screen -dmS "run_gaya_$i" bash -c "cd /workspace && \
  CUDA_VISIBLE_DEVICES=2 \
  python3 generate.py \
    --voice \"kp-rtm-enhanced-v2.wav\" \
    --original_text \"Selalunya kalau kita pergi berjumpa media kan, kalau kita pergi buat produk launch ke dan sebagainya, selalunya, dia siapkan barang itu dulu, atau apa yang kita nak jual kepada dunia,\" \
    --text_file \"news-gaya-hidup.json\" \
    --folder \"kp-gaya-hidup\" \
    --global_index 4 \
    --index $i --threshold -9"
done

for i in {0..3}; do
  screen -S "run_malaysia_$i" -X quit 2>/dev/null
  screen -dmS "run_malaysia_$i" bash -c "cd /workspace && \
  CUDA_VISIBLE_DEVICES=3 \
  python3 generate.py \
    --voice \"kp-rtm-enhanced-v2.wav\" \
    --original_text \"Selalunya kalau kita pergi berjumpa media kan, kalau kita pergi buat produk launch ke dan sebagainya, selalunya, dia siapkan barang itu dulu, atau apa yang kita nak jual kepada dunia,\" \
    --text_file \"news-berita-sukan.json\" \
    --folder \"kp-berita-sukan\" \
    --global_index 4 \
    --index $i --threshold -9"
done