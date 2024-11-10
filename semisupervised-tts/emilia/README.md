# Emilia

## Husein server

### GPU 0

```bash
LD_LIBRARY_PATH=/home/husein/.local/lib/python3.10/site-packages/nvidia/cudnn/lib \
CUDA_VISIBLE_DEVICES=0 \
python3.10 main.py \
--batch_size 2 \
--compute_type bfloat16 \
--whisper_arch large-v3 \
--global-size 2 --local-index 0
```

## PrimeIntellect

Install,

```bash
cd /workspace
pip3 install notebook==6.5.6 huggingface-hub
apt update
apt install screen unzip ffmpeg -y
screen -dmS jupyter_session bash -c "jupyter notebook --NotebookApp.token='' --no-browser --allow-root --notebook-dir='/workspace'"
wget https://www.7-zip.org/a/7z2301-linux-x64.tar.xz
tar -xf 7z2301-linux-x64.tar.xz
wget https://github.com/TRvlvr/model_repo/releases/download/all_public_uvr_models/UVR-MDX-NET-Inst_HQ_3.onnx
wget https://github.com/microsoft/DNS-Challenge/raw/refs/heads/master/DNSMOS/DNSMOS/sig_bak_ovr.onnx
wget https://huggingface.co/datasets/huseinzol05/temp-storage/resolve/main/Amphion-main.zip
unzip Amphion-main.zip
cd Amphion-main/preprocessors/Emilia
pip3 install -r requirements.txt
pip3 install onnxruntime-gpu
python -c "
from huggingface_hub import snapshot_download
snapshot_download(repo_id='malaysia-ai/crawl-youtube-malaysian-podcast', repo_type='dataset', local_dir = './')
"
/workspace/7zz x malaysian-podcast.zip -y -mmt40
```

```bash
cd /workspace/Amphion-main/preprocessors/Emilia
LD_LIBRARY_PATH=/usr/local/lib/python3.11/dist-packages/nvidia/cudnn/lib \
CUDA_VISIBLE_DEVICES=0 \
python3 main.py \
--batch_size 2 \
--compute_type bfloat16 \
--whisper_arch large-v3 \
--global-size 2 --local-index 0
```