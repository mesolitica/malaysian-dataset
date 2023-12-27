# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/dua-3.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/dua-belas-13.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/dua-puluh-21.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/dua-puluh-dua-23.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/dua-puluh-empat-25.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/dua-puluh-enam-27.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/dua-puluh-lapan-29.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/dua-puluh-lima-26.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/dua-puluh-satu-22.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/dua-puluh-sembilan-30.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/dua-puluh-tiga-24.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/dua-puluh-tujuh-28.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/empat-5.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/empat-belas-15.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/enam-7.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/enam-belas-17.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/lapan-9.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/lapan-belas-19.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/lima-6.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/lima-belas-16.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/pengenalan-1.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/satu-2.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/sebelas-12.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/sembilan-10.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/sembilan-belas-20.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/sepuluh-11.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/tiga-4.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/tiga-belas-14.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/tiga-puluh-31.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/tiga-puluh-dua-33.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/tiga-puluh-empat-35.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/tiga-puluh-satu-32.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/tiga-puluh-tiga-34.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/tujuh-8.mp3
# !wget https://f000.backblazeb2.com/file/malaya-speech-model/audiobook/salina/tujuh-belas-18.mp3


import os

os.system('mkdir output-wav-salina output-text-salina')
os.environ['CUDA_VISIBLE_DEVICES'] = '2'

import speech_recognition as sr
import soundfile as sf
from tqdm import tqdm

r = sr.Recognizer()

from pydub.silence import split_on_silence, detect_nonsilent
from pydub import AudioSegment
import numpy as np
import malaya_speech
from malaya_speech import Pipeline
from scipy.io.wavfile import write

p = Pipeline()

model_v2 = malaya_speech.vad.deep_model(model='vggvox-v2')
pipeline = (
    p.map(malaya_speech.utils.generator.frames, frame_duration_ms=30)
    .batching(20)
    .foreach_map(model_v2.predict)
    .flatten()
)

from glob import glob

mp3s = glob('*.mp3')
mp3s

for file in mp3s:
    print(file)
    try:
        audio = AudioSegment.from_mp3(file)
        sample_rate = audio.frame_rate
        samples = np.array(audio.get_array_of_samples())
        samples = malaya_speech.astype.int_to_float(samples)
        samples_16k = malaya_speech.resample(samples, sample_rate, 16000)
        frames_16k = list(
            malaya_speech.utils.generator.frames(samples_16k, 30, 16000)
        )
        frames = list(
            malaya_speech.utils.generator.frames(samples, 30, sample_rate)
        )
        result = p.emit(samples_16k)
        frames_deep_v2_batch = [
            (frame, result['flatten'][no]) for no, frame in enumerate(frames)
        ]
        results = malaya_speech.split.split_vad(
            frames_deep_v2_batch, n=5, negative_threshold=0.1
        )

        for no in tqdm(range(len(results))):
            result = results[no]

            sf.write('test.wav', result.array, sample_rate)

            try:

                with sr.AudioFile('test.wav') as source:
                    a = r.record(source)

                text = r.recognize_google(a, language='ms')
                filename = f'{file}-{no}.wav'
                if len(text):
                    text_filename = f'output-text-salina/{filename}.txt'
                    with open(text_filename, 'w') as fopen:
                        fopen.write(text)

                    sf.write(
                        f'output-wav-salina/{filename}',
                        result.array,
                        sample_rate,
                    )
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
