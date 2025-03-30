# Emilia

## Husein server

```bash
cd /home/husein/ssd2/Amphion/preprocessors/Emilia
LD_LIBRARY_PATH=/home/husein/.local/lib/python3.10/site-packages/nvidia/cudnn/lib \
CUDA_VISIBLE_DEVICES=0 \
python3.10 main.py \
--batch_size 2 \
--compute_type bfloat16 \
--whisper_arch large-v3 \
--global-size 1 --local-index 0

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
wget https://www.7-zip.org/a/7z2301-linux-x64.tar.xz
tar -xf 7z2301-linux-x64.tar.xz
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
pip3 uninstall whisperx -y
pip3 install git+https://github.com/m-bain/whisperX.git@9e3a9e0e38fcec1304e1784381059a0e2c670be5
pip3 install ctranslate2==4.5.0
pip3 install numpy==1.26.4
pip3 install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1

cd /workspace
python -c "
from huggingface_hub import snapshot_download
snapshot_download(repo_id='malaysia-ai/crawl-youtube-malaysian-cartoons-filtered-24k', repo_type='dataset', local_dir = './')
"
/workspace/7zz x filtered-24k.zip -y -mmt40

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

### Malaysian Youtube dialects

```bash
python -c "
from huggingface_hub import snapshot_download
snapshot_download(repo_id='malaysia-ai/filtered-malaysian-dialects-youtube', repo_type='dataset', local_dir = './',
max_workers = 40)
"
python -c "
from huggingface_hub import snapshot_download
snapshot_download(repo_id='mesolitica/Malaysian-Emilia', repo_type='dataset', local_dir = './',
allow_patterns = 'dialects-processed-*.zip')
"
python3 unzip.py
rm *.zip

for i in {0..3}; do
  screen -S "run_$i" -X quit 2>/dev/null
  screen -dmS "run_$i" bash -c "cd /workspace/Amphion-main/preprocessors/Emilia && \
  LD_LIBRARY_PATH=/usr/local/lib/python3.11/dist-packages/nvidia/cudnn/lib \
  CUDA_VISIBLE_DEVICES=$i \
  python3 main.py \
  --batch_size 4 \
  --compute_type bfloat16 \
  --whisper_arch large-v3 \
  --global-size 4 --local-index $i || echo 'Error encountered! Press Ctrl+D to exit.'; exec bash"
done
```