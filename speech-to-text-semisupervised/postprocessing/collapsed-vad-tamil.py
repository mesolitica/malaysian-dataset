from streaming import LocalDataset
from streaming import MDSWriter
from silero_vad import load_silero_vad
from datasets import Audio
from glob import glob
from tqdm import tqdm
import numpy as np
import IPython.display as ipd
import soundfile as sf
import json
import pickle
import os
import re
import torch
import mp


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

def loop(ranged):
    
    audio = Audio(sampling_rate=sr)
    model = load_silero_vad(onnx=True)
    ranged, index = ranged
    filename = f'vad-audio-tamil-{index}.jsonl'
    fopen_l = open(filename, 'a')
    pointer = Pointer(f'{filename}.pickle')
    pointer.load()
    dataset = LocalDataset('tamil-mosaic')
    n = 0
    for i in tqdm(ranged):
        if n >= pointer.index:
            entry = dataset[i]
                    
            audio_filename = entry['audio_filename']
            if not os.path.exists(audio_filename):
                continue

            y = audio.decode_example(audio.encode_example(audio_filename))['array']
            label = entry['new_text']
            label_en = entry['new_text_en']
            label_ms = entry['new_text_ms']
            segments = segment_texts(label)

            r = 0

            for k in range(len(segments)):

                segment = segments[k]
                segment_text = re.sub(r'<\|.*?\|>', '', segment[2])

                if k + 1 < len(segments):
                    segment_text_2 = re.sub(r'<\|.*?\|>', '', segments[k+1][2])
                    if segment_text == segment_text_2:
                        label = label.replace(segment[2], f"<|{segment[0]}|><|{segment[1]}|>")
                        if len(label_ms):
                            label_ms = label_ms.replace(segment[2], f"<|{segment[0]}|><|{segment[1]}|>")

                        if len(label_en):
                            label_en = label_en.replace(segment[2], f"<|{segment[0]}|><|{segment[1]}|>")

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
                    if len(label_ms):
                        label_ms = label_ms.replace(segment[2], f"<|{segment[0]}|><|{segment[1]}|>")
                    if len(label_en):
                        label_en = label_en.replace(segment[2], f"<|{segment[0]}|><|{segment[1]}|>")

            
            entry['new_text'] = label  
            entry['new_text_en'] = label_en
            entry['new_text_ms'] = label_ms  
            entry['index'] = n
            fopen_l.write(f'{json.dumps(entry)}\n')
            fopen_l.flush()
            
            pointer.index = n
            pointer._save()
        
        n += 1

def main():
    dataset = LocalDataset('tamil-mosaic')
    mp.multiprocessing(range(len(dataset)), loop, cores = 32, returned = False)

if __name__ == "__main__":
    main()