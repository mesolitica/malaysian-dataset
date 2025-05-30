apt update
apt install unzip ffmpeg -y
apt update && apt install -y locales
locale-gen en_US.UTF-8
cd /workspace
wget https://www.7-zip.org/a/7z2301-linux-x64.tar.xz
tar -xf 7z2301-linux-x64.tar.xz
pip3 install huggingface-hub

python3 -c "
from huggingface_hub import snapshot_download
snapshot_download(repo_id='malaysia-ai/dedup-Malaysian-Emilia', repo_type='dataset', 
                  allow_patterns = '*.z*', local_dir = './')
"
/workspace/7zz x dedup-parliament.zip -y -mmt40
/workspace/7zz x dedup-podcasts.zip -y -mmt40

wget https://github.com/mesolitica/malaysian-dataset/raw/refs/heads/master/text-to-speech/husein/requirements.txt
pip3 install -r requirements.txt
pip3 install click vocos torchdiffeq==0.2.4 x-transformers==1.42.11 jieba==0.42.1 pypinyin==0.53.0

wget https://huggingface.co/datasets/malaysia-ai/Speech-Instructions/resolve/main/text/partition-instructions-part-3.json
wget https://huggingface.co/datasets/malaysia-ai/Speech-Instructions/resolve/main/text/partition-instructions-part-4.json
wget https://huggingface.co/datasets/malaysia-ai/Speech-Instructions/resolve/main/text/partition-instructions-part-5.json
wget https://huggingface.co/datasets/malaysia-ai/Speech-Instructions/resolve/main/text/partition-instructions-part-6.json
wget https://raw.githubusercontent.com/malaysia-ai/dataset/refs/heads/main/speech-instructions/generate.py

for i in {0..3}; do
  screen -S "partition-instructions-part-3_$i" -X quit 2>/dev/null
  screen -dmS "partition-instructions-part-3_$i" bash -c "cd /workspace && \
  CUDA_VISIBLE_DEVICES=0 \
  python3 generate.py \
    --input_file \"partition-instructions-part-3.json\" \
    --folder \"partition-instructions-part-3\" \
    --global_index 4 \
    --index $i"
done

for i in {0..3}; do
  screen -S "partition-instructions-part-4_$i" -X quit 2>/dev/null
  screen -dmS "partition-instructions-part-4_$i" bash -c "cd /workspace && \
  CUDA_VISIBLE_DEVICES=1 \
  python3 generate.py \
    --input_file \"partition-instructions-part-4.json\" \
    --folder \"partition-instructions-part-4\" \
    --global_index 4 \
    --index $i"
done

for i in {0..3}; do
  screen -S "partition-instructions-part-5_$i" -X quit 2>/dev/null
  screen -dmS "partition-instructions-part-5_$i" bash -c "cd /workspace && \
  CUDA_VISIBLE_DEVICES=2 \
  python3 generate.py \
    --input_file \"partition-instructions-part-5.json\" \
    --folder \"partition-instructions-part-5\" \
    --global_index 4 \
    --index $i"
done

for i in {0..3}; do
  screen -S "partition-instructions-part-6_$i" -X quit 2>/dev/null
  screen -dmS "partition-instructions-part-6_$i" bash -c "cd /workspace && \
  CUDA_VISIBLE_DEVICES=3 \
  python3 generate.py \
    --input_file \"partition-instructions-part-6.json\" \
    --folder \"partition-instructions-part-6\" \
    --global_index 4 \
    --index $i"
done