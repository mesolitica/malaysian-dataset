### Data Preparation for Malaysian Local Speech (Loghat) to Direct Text Transcription to Proper Text Transcription

**Environment Preparation (Python 3.11.9):**

```
pip install -r requirements.txt
pip install --upgrade --force-reinstall "git+https://github.com/ytdl-org/youtube-dl.git" sudo yum install epel-release sudo yum localinstall --nogpgcheck https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm sudo yum install ffmpeg ffmpeg-devel pip install ffmpeg-python
```
conda install -c conda-forge ffmpeg  #if use conda 

**List of Dialets :**
- [x] Penang
- [x] Kelantan
- [ ] Sarawak
- [ ] Sabah
- [ ] ..
- 

**Process Flow :**

    1. Identify video in Youtube that use almost 100% Malaysia local dialects
    2. Create list of URL of these Youtube video.
    3. Download audio from these Youtube video
    4. Combine these audio and save in mp3 format in "download" folder (dialect state of origin sub-folder)
    5. Create chunks of these audio using "silence" of 500ms as the "splitter"
    6. These chunks saved in "chunk" subfolder
    7. Remove chunks that have less than 5 second audio length
    8. Load and visualise the audio then annotate the audio
    9. Create pandas dataframe that keep the link of the audio chunk, audio length, direct text transcription and proper text transcription

| Audio File  |Start Time   |End Time   |Direct Transcription   |Proper Transcription   |
|---|---|---|---|---|
|/malaysian-dialects-audio/penang/chunk/2024-06-14-penang-chunk158.mp3|0.5   |2.5   |Depa kata tuan punya kedai ni dulu   |Dikatakan pemilik kedai ni dahulu   |
|..   |..   |..   |..   |..   |
|..   |..   |..   |..   |...   |
