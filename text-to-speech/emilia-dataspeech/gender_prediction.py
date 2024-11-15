from transformers import AutoFeatureExtractor, AutoModelForAudioClassification
from torch.utils.data import DataLoader
from torch.nn import functional as F
from tqdm import tqdm
from glob import glob
import torch
import torchaudio
import numpy as np
import click
import os

def new_path(f):
    f = f.replace('.mp3', '.gender')
    splitted = f.split('/')
    base_folder = splitted[0] + '_gender'
    splitted = '/'.join([base_folder] + splitted[1:])
    return splitted

class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, dataset, sampling_rate=16000, max_audio_len=5):
        self.dataset = dataset
        self.sampling_rate = sampling_rate
        self.max_audio_len = max_audio_len

    def __len__(self):
        return len(self.dataset)

    def _cutorpad(self, audio):
        effective_length = self.sampling_rate * self.max_audio_len
        len_audio = len(audio)

        if len_audio > effective_length:
            audio = audio[:effective_length]

        return audio

    def __getitem__(self, index):
        filepath = self.dataset[index]
        speech_array, sr = torchaudio.load(filepath)

        if speech_array.shape[0] > 1:
            speech_array = torch.mean(speech_array, dim=0, keepdim=True)

        if sr != self.sampling_rate:
            transform = torchaudio.transforms.Resample(sr, self.sampling_rate)
            speech_array = transform(speech_array)
            sr = self.sampling_rate

        speech_array = speech_array.squeeze().numpy()
        speech_array = self._cutorpad(speech_array)

        return {"input_values": speech_array, "attention_mask": None, 'file': filepath}

class CollateFunc:
    def __init__(self, processor, max_length=None, padding=True, pad_to_multiple_of=None, sampling_rate=16000):
        self.padding = padding
        self.processor = processor
        self.max_length = max_length
        self.sampling_rate = sampling_rate
        self.pad_to_multiple_of = pad_to_multiple_of

    def __call__(self, batch):
        input_features = []
        files = []

        for audio in batch:
            input_tensor = self.processor(audio["input_values"], sampling_rate=self.sampling_rate).input_values
            input_tensor = np.squeeze(input_tensor)
            input_features.append({"input_values": input_tensor})
            files.append(audio['file'])

        batch = self.processor.pad(
            input_features,
            padding=self.padding,
            max_length=self.max_length,
            pad_to_multiple_of=self.pad_to_multiple_of,
            return_tensors="pt",
        )

        return batch, files


@click.command()
@click.option("--path", help="files path in glob pattern")
@click.option("--global-index", default=1, help="global index")
@click.option("--local-index", default=0, help="local index")
def function(path, global_index, local_index):
    
    model = 'alefiury/wav2vec2-large-xlsr-53-gender-recognition-librispeech'
    num_labels = 2
    
    feature_extractor = AutoFeatureExtractor.from_pretrained(model)
    model = AutoModelForAudioClassification.from_pretrained(
        pretrained_model_name_or_path=model,
        num_labels=num_labels, torch_dtype = torch.bfloat16
    ).eval().cuda()

    files = glob(path)
    filtered_files = []
    for f in files:
        new_f = new_path(f)
        if os.path.exists(new_f) and os.path.getsize(new_f) > 2:
            continue
        filtered_files.append(f)
        
    dataset = CustomDataset(filtered_files)
    data_collator = CollateFunc(
        processor=feature_extractor,
        padding=True,
        sampling_rate=16000,
    )

    dataloader = DataLoader(
        dataset=dataset,
        batch_size=16,
        collate_fn=data_collator,
        shuffle=False,
        num_workers=10
    )

    device = model.device
    dtype = model.dtype
    label_mapping = {0: "female", 1: "male"}

    with torch.no_grad():
        for batch in tqdm(dataloader):
            batch, files_ = batch
            input_values = batch['input_values'].type(dtype).to(device)

            logits = model(input_values).logits
            scores = F.softmax(logits, dim=-1)
            
            labels = [label_mapping[i] for i in torch.argmax(scores, dim=1).cpu().detach().numpy()]
            
            for no, f in enumerate(files_):
                splitted = new_path(f)
                
                os.makedirs(os.path.split(splitted)[0], exist_ok = True)
                with open(splitted, 'w') as fopen:
                    fopen.write(labels[no])

if __name__ == '__main__':
    function()