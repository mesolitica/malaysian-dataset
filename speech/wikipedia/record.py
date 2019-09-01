import queue
import sys
import sounddevice as sd
import soundfile as sf
import numpy
import os
import tempfile
import json

with open('dumping-wiki-6-july-2019.json') as fopen:
    wiki = json.load(fopen)

combined_wiki = ' '.join(wiki).split()
len(combined_wiki)

length = 4
texts = []
for i in range(0, len(combined_wiki), length):
    texts.append(' '.join(combined_wiki[i : i + length]))

device_info = sd.query_devices(None, 'input')
device = None
samplerate = int(device_info['default_samplerate'])
channels = 1
subtype = None

for no, text in enumerate(texts):
    try:
        filename = 'streaming/%s.wav' % (text)
        if os.path.isfile(filename):
            continue

        print(
            'say: %s, if too hard, press c + enter to skip, else any button + enter to continue'
            % (text)
        )
        skip = input().lower()
        if skip == 'c':
            continue

        q = queue.Queue()

        def callback(indata, frames, time, status):
            if status:
                print(status, file = sys.stderr)
            q.put(indata.copy())

        with sf.SoundFile(
            filename,
            mode = 'x',
            samplerate = samplerate,
            channels = channels,
            subtype = subtype,
        ) as file:
            with sd.InputStream(
                samplerate = samplerate,
                device = device,
                channels = channels,
                callback = callback,
            ):
                print('#' * 80)
                print('press Ctrl+C to stop the recording')
                print('say: %s' % (text))
                print('#' * 80, '\n')
                while True:
                    file.write(q.get())
    except KeyboardInterrupt:
        print(
            '\nRecording finished: %s, left %d\n'
            % (repr(filename), len(texts) - no)
        )

    except:
        pass
