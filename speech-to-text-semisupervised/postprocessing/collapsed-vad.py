from streaming import LocalDataset
from streaming import MDSWriter
from silero_vad import load_silero_vad
from datasets import Audio
from glob import glob
from tqdm import tqdm
import json
import numpy as np
import os
import re
import torch
import IPython.display as ipd
import mp
import soundfile as sf


sr = 16000
window_size_samples = 512

def segment_texts(text):
    pattern = r'<\|(\d+(?:\.\d+)?)\|>(.*?)(?=<\||\Z)'
    
    matches = re.findall(pattern, text, re.DOTALL)
    
    result = []
    for i, (start_time, content) in enumerate(matches):
        content = content
        if content:
            end_time = matches[i+1][0] if i+1 < len(matches) else start_time
            result.append((float(start_time), float(end_time), f"<|{start_time}|>{content}<|{end_time}|>"))
    
    return result

import pickle
import os

class Pointer:
    def __init__(self, filename):
        self.filename = filename
        self.index = -1

    def _save(self):
        with open(self.filename, 'wb') as fopen:
            pickle.dump(self.index, fopen)

    def increment(self):
        self.index += 1
        self._save()

    def load(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, 'rb') as fopen:
            self.index = pickle.load(fopen)

def loop(files):
    
    audio = Audio(sampling_rate=sr)
    model = load_silero_vad(onnx=True)
    files, index = files
    filename = f'vad-audio-{index}.jsonl'
    fopen_l = open(filename, 'a')
    pointer = Pointer(f'{filename}.pickle')
    pointer.load()
    n = 0
    for f in files:
        with open(f) as fopen:
            for l in tqdm(fopen):
                if n > pointer.index:
                    entry = json.loads(l)
                    
                    audio_filename = entry['audio_filename']
                    if not os.path.exists(audio_filename):
                        continue

                    y = audio.decode_example(audio.encode_example(audio_filename))['array']
                    label = entry['text']
                    segments = segment_texts(label)

                    r = 0

                    for k in range(len(segments)):

                        segment = segments[k]
                        segment_text = re.sub(r'<\|.*?\|>', '', segment[2])

                        if k + 1 < len(segments):
                            segment_text_2 = re.sub(r'<\|.*?\|>', '', segments[k+1][2])
                            if segment_text == segment_text_2:
                                label = label.replace(segment[2], f"<|{segment[0]}|><|{segment[1]}|>")
                                r += 1
                                continue


                        segment_audio = torch.Tensor(y[int(segment[0] * sr): int(segment[1] * sr)])
                        audio_length_samples = len(segment_audio)

                        speech_probs = []

                        for current_start_sample in range(0, audio_length_samples, window_size_samples):
                            chunk = segment_audio[current_start_sample: current_start_sample + window_size_samples]
                            if len(chunk) < window_size_samples:
                                chunk = torch.nn.functional.pad(chunk, (0, int(window_size_samples - len(chunk))))
                            speech_prob = model(chunk, sr).item()
                            speech_probs.append(speech_prob)

                        vad_prob = np.mean(speech_probs)

                        if vad_prob < 0.001:
                            label = label.replace(segment[2], f"<|{segment[0]}|><|{segment[1]}|>")
                    
                    entry['text'] = label  
                    entry['file'] = f
                    entry['index'] = n
                    fopen_l.write(f'{json.dumps(entry)}\n')
                    fopen_l.flush()
                    
                    pointer.index = n
                    pointer._save()
                
                n += 1

def main():
    files = sorted(glob('partition-audio-vad/*.jsonl'), key = lambda x: int(x.split('-')[-1].replace('.jsonl', '')))
    # loop((files[:1], 0))
    mp.multiprocessing(files, loop, cores = 32, returned = False)

if __name__ == "__main__":
    main()