import speech_recognition as sr
from scipy.io.wavfile import write
import json
import os
import time

with open('dumping-wiki-6-july-2019.json') as fopen:
    wiki = json.load(fopen)

combined_wiki = ' '.join(wiki).split()
len(combined_wiki)

length = 4
texts = []
for i in range(0, len(combined_wiki), length):
    texts.append(' '.join(combined_wiki[i : i + length]))

r = sr.Recognizer()
r.energy_threshold = 1000
r.pause_threshold = 0.5
m = sr.Microphone()

try:
    print('A moment of silence, please...')
    print('Set minimum energy threshold to {}'.format(r.energy_threshold))
    print('Adjusting minimum energy...')
    with m as source:
        r.adjust_for_ambient_noise(source, duration = 3)
    print('Now set minimum energy threshold to {}'.format(r.energy_threshold))
    for _ in range(50):
        time.sleep(0.1)
    for no, text in enumerate(texts):
        filename = 'streaming/%s.wav' % (text)
        try:
            if os.path.isfile(filename):
                continue
            print('Say: %s' % (text))
            with m as source:
                audio = r.listen(source)
            print('Got it! saving')
            with open(filename, 'wb') as f:
                f.write(audio.get_wav_data())
            print(
                '\nRecording finished: %s, left %d\n'
                % (repr(filename), len(texts) - no)
            )
        except KeyboardInterrupt:
            print('skip %s' % (filename))
            continue

except KeyboardInterrupt:
    pass
