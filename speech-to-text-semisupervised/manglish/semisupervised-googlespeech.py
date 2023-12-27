from pydub.silence import split_on_silence, detect_nonsilent
from pydub import AudioSegment
from tqdm import tqdm


def split(
    file,
    min_silence_len=500,
    silence_thresh=-20,
    max_len=7,
    keep_silence=1000,
):
    audio = AudioSegment.from_mp3(file)
    audio_chunks = split_on_silence(
        audio,
        min_silence_len=min_silence_len,
        silence_thresh=silence_thresh,
        keep_silence=keep_silence,
    )

    audios, temp, length = [], [], 0
    for i in range(len(audio_chunks)):
        if length + audio_chunks[i].duration_seconds >= max_len and len(temp):
            audios.append(sum(temp))
            temp = []
            length = 0
        temp.append(audio_chunks[i])
        length += audio_chunks[i].duration_seconds

    if len(temp):
        audios.append(sum(temp))

    return audios, audio


import speech_recognition as sr
import os
import uuid

r = sr.Recognizer()


def audiosegment_google_speech(audio, filename, lang='en-SG'):
    if os.path.exists('output-wav/' + filename):
        return False

    audio.set_frame_rate(32000).set_channels(1).export(filename, format='wav')
    try:
        with sr.AudioFile(filename) as source:
            a = r.record(source)

        text = r.recognize_google(a, language=lang)
    except BaseException:
        text = ''

    if len(text):
        text_filename = f'output-text/{filename}.txt'
        with open(text_filename, 'w') as fopen:
            fopen.write(text)

        audio.set_frame_rate(16000).set_channels(1).export(
            'output-wav/' + filename, format='wav'
        )

    os.remove(filename)

    return True


from glob import glob

files = glob('*.mp3')
rejected = [
    'lyrics',
    'beyblade',
    'dub',
    'bare bear',
    'chibi',
    'namewee',
    'ultraman',
    'terjemahan',
]
files = [f for f in files if all([r not in f.lower() for r in rejected])]
len(files)

for file in files:
    mp3 = file.replace(' ', '-')
    if mp3 != file:
        os.replace(file, mp3)

files = glob('*.mp3')
rejected = [
    'lyrics',
    'beyblade',
    'dub',
    'bare bear',
    'chibi',
    'namewee',
    'ultraman',
    'terjemahan',
]
files = [f for f in files if all([r not in f.lower() for r in rejected])]

skip_first = 5
for no, filename in enumerate(files):
    try:
        audios, audio = split(filename)
        audios = audios[skip_first:]
        print(filename, len(audios))

        for part in tqdm(range(len(audios))):
            temp_filename = f'{filename}-part-{part}.wav'
            audiosegment_google_speech(audios[part], temp_filename)
    except Exception as e:
        print(e)
        pass

    print(f'DONE: {no + 1} / {len(files)}')
