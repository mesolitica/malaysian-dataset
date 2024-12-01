# Emilia

## Husein server

### GPU 0

```bash
cd /home/husein/ssd2/Amphion/preprocessors/Emilia
LD_LIBRARY_PATH=/home/husein/.local/lib/python3.10/site-packages/nvidia/cudnn/lib \
CUDA_VISIBLE_DEVICES=1 \
python3.10 main.py \
--batch_size 2 \
--compute_type bfloat16 \
--whisper_arch large-v3 \
--global-size 3 --local-index 1

for i in {0..1}; do
  screen -S "run_$i" -X quit 2>/dev/null
  screen -dmS "run_$i" bash -c "cd /home/husein/ssd2/Amphion/preprocessors/Emilia && \
  LD_LIBRARY_PATH=/home/husein/.local/lib/python3.10/site-packages/nvidia/cudnn/lib \
  CUDA_VISIBLE_DEVICES=$i \
  python3.10 main.py \
  --batch_size 2 \
  --compute_type bfloat16 \
  --whisper_arch large-v3 \
  --global-size 3 --local-index $i"
done
```

## PrimeIntellect

Install,

```bash
cd /workspace
pip3 install huggingface-hub
python -c "
from huggingface_hub import snapshot_download
snapshot_download(repo_id='malaysia-ai/crawl-youtube-malaysian-cartoons-filtered-24k', repo_type='dataset', local_dir = './')
"
wget https://www.7-zip.org/a/7z2301-linux-x64.tar.xz
tar -xf 7z2301-linux-x64.tar.xz
/workspace/7zz x filtered-24k.zip -y -mmt40

cd /workspace
pip3 install notebook==6.5.6
apt update
apt install screen unzip ffmpeg vim -y
screen -dmS jupyter_session bash -c "jupyter notebook --NotebookApp.token='' --no-browser --allow-root --notebook-dir='/workspace'"
wget https://github.com/TRvlvr/model_repo/releases/download/all_public_uvr_models/UVR-MDX-NET-Inst_HQ_3.onnx
wget https://github.com/microsoft/DNS-Challenge/raw/refs/heads/master/DNSMOS/DNSMOS/sig_bak_ovr.onnx
wget https://huggingface.co/datasets/huseinzol05/temp-storage/resolve/main/Amphion-main.zip
unzip Amphion-main.zip
cd Amphion-main/preprocessors/Emilia
pip3 install -r requirements.txt
pip3 install onnxruntime-gpu==1.20.0

for i in {0..7}; do
  screen -S "run_$i" -X quit 2>/dev/null
  screen -dmS "run_$i" bash -c "cd /workspace/Amphion-main/preprocessors/Emilia && \
  LD_LIBRARY_PATH=/usr/local/lib/python3.11/dist-packages/nvidia/cudnn/lib \
  CUDA_VISIBLE_DEVICES=$i \
  python3 main.py \
  --batch_size 4 \
  --compute_type bfloat16 \
  --whisper_arch large-v3 \
  --global-size 8 --local-index $i"
done
```

## Post cleaning

### MY Podcast

```bash
cd /workspace
pip3 install git+https://github.com/huseinzolkepli05/resemble-enhance
python3 -c "from resemble_enhance.enhancer.inference import denoise, enhance"
pip3 install huggingface-hub notebook==6.5.6 click
apt update
apt install screen unzip ffmpeg -y
screen -dmS jupyter_session bash -c "jupyter notebook --NotebookApp.token='' --no-browser --allow-root --notebook-dir='/workspace'"
wget https://huggingface.co/datasets/mesolitica/Malaysian-Emilia/resolve/main/malaysian-podcast-processed.zip
unzip malaysian-podcast-processed.zip

for i in {0..7}; do
  screen -S "run_$i" -X quit 2>/dev/null
  screen -dmS "run_$i" bash -c "CUDA_VISIBLE_DEVICES=$i \
  python3 post-cleaning.py \
  --path 'parlimen-24k-chunk_processed/**/*.mp3' \
  --global-index 8 --local-index $i"
done
```