import os

os.environ['CUDA_VISIBLE_DEVICES'] = ''

from pydub.silence import split_on_silence, detect_nonsilent
from pydub import AudioSegment
from tqdm import tqdm
import malaya_speech
import numpy as np
from malaya_speech import Pipeline
import IPython.display as ipd
import soundfile as sf
import speech_recognition as sr
import os
import uuid
from glob import glob
from unidecode import unidecode
from malaya_speech.model.frame import Frame
from malaya_speech.utils.group import (
    combine_frames,
    group_frames,
    group_frames_threshold,
)

os.system('mkdir output-wav output-text')
r = sr.Recognizer()
vad = malaya_speech.vad.webrtc()


def split_vad_duration(
    frames,
    max_duration: float = 5.0,
    negative_threshold: float = 0.1,
    sample_rate: int = 16000,
):
    """
    Split a sample into multiple samples based maximum duration of voice activities.

    Parameters
    ----------
    frames: List[Tuple[Frame, label]]
    max_duration: float, optional (default = 5.0)
        Maximum duration to assume one sample combined from voice activities.
    negative_threshold: float, optional (default = 0.1)
        If `negative_threshold` is 0.1, means that, length negative samples must at least 0.1 second.
    sample_rate: int, optional (default = 16000)
        sample rate for frames.

    Returns
    -------
    result : List[Frame]
    """
    grouped = group_frames(frames)
    grouped = group_frames_threshold(
        grouped, threshold_to_stop=negative_threshold
    )
    results, temp, lengths = [], [], 0
    for no, g in enumerate(grouped):
        a = g[0]
        l = len(a.array) / sample_rate
        lengths += l
        temp.append(a)
        if lengths >= max_duration:
            results.append(combine_frames(temp))
            temp = []
            lengths = 0

    if len(temp):
        results.append(combine_frames(temp))
    return results


def split(file, max_duration=5.0):
    audio = AudioSegment.from_mp3(file).set_channels(1)
    y = np.array(audio.get_array_of_samples())
    y_ = np.array(audio.set_frame_rate(16000).get_array_of_samples())
    frames = malaya_speech.generator.frames(y, 30, audio.frame_rate)
    frames_ = malaya_speech.generator.frames(
        y_, 30, 16000, append_ending_trail=False
    )
    frames_webrtc = [
        (frames[no], vad(frame)) for no, frame in enumerate(frames_)
    ]
    splitted = split_vad_duration(
        frames_webrtc,
        max_duration=max_duration,
        negative_threshold=0.1,
        sample_rate=audio.frame_rate,
    )
    return splitted, audio, audio.frame_rate


def audiosegment_google_speech(audio, filename, sample_rate, lang='ms'):
    if os.path.exists('output-wav/' + filename):
        return False

    sf.write(filename, audio.array, sample_rate)
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

        a = malaya_speech.resample(
            malaya_speech.astype.int_to_float(audio.array), sample_rate, 16000
        )
        sf.write('output-wav/' + filename, a, 16000)

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
    'vlog',
    'puisi',
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
    'vlog',
    'puisi',
]
files = [f for f in files if all([r not in f.lower() for r in rejected])]
maxlen_audio = 17

for no, filename in enumerate(files):
    wavs = glob('output-wav/*.wav')
    if any([filename in w for w in wavs]):
        print(f'skip {filename}, exist')
        continue
    try:
        audios, audio, sample_rate = split(filename)
        print(filename, len(audios))

        for part in tqdm(range(len(audios))):
            temp_filename = f'{filename}-part-{part}.wav'

            if len(audios[part].array) / sample_rate >= maxlen_audio:
                print(f'{temp_filename} longer than {maxlen_audio} seconds')
                continue

            audiosegment_google_speech(audios[part], temp_filename, sample_rate)
    except Exception as e:
        print(e)

    print(f'DONE: {no + 1} / {len(files)}')
