import numpy as np
import soundfile as sf
from scipy.io import wavfile
import azure.cognitiveservices.speech as speechsdk
import os
import json
from glob import glob
import time
from tqdm import tqdm


def to_ndarray(array):
    """
    Change list / tuple / bytes into np.array

    Parameters
    ----------
    array: list / tuple / bytes

    Returns
    -------
    result : np.array
    """

    if isinstance(array, list) or isinstance(array, tuple):
        array = np.array(array)
    elif isinstance(array, bytes) or isinstance(array, bytearray):
        if isinstance(array, bytearray):
            array = bytes(array)
        array = np.frombuffer(array, np.int16)
    return array


speech_config = speechsdk.SpeechConfig()
speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Raw24Khz16BitMonoPcm)
speech_config.speech_synthesis_voice_name = 'ms-MY-YasminNeural'
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)

with open('populated-text.json') as fopen:
    data = json.load(fopen)


for i in tqdm(range(len(data))):
    d = data[i]
    output_file = os.path.join('female', f'{i}.wav')

    if os.path.exists(output_file):
        continue

    while True:
        result = speech_synthesizer.speak_text_async(d['cleaned']).get()
        if result.reason == speechsdk.ResultReason.Canceled:
            print(result.cancellation_details)
            time.sleep(60)
        else:
            audio = to_ndarray(result.audio_data)
            wavfile.write(output_file, 24000, audio)
            break
