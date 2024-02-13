import json
import argparse
import os
import pickle
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', help='filename')
args = parser.parse_args()
filename = args.filename

model = AutoModelForCausalLM.from_pretrained(
    'mesolitica/malaysian-mistral-7b-32k-instructions-v4',
    use_flash_attention_2=True,
    torch_dtype=torch.float16
)

_ = model.cuda()
tokenizer = AutoTokenizer.from_pretrained(
    'mesolitica/malaysian-mistral-7b-32k-instructions-v4'
)


class Pointer:
    def __init__(self, filename):
        self.filename = filename
        self.index = 0

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


pointer = Pointer(f'{filename}.pickle')
pointer.load()

file = open(f'{filename}.requested', 'a')
max_length = 4096

with open(filename) as fopen:
    for i, l in tqdm(enumerate(fopen)):
        if i >= pointer.index:
            text = json.loads(l)
            if len(tokenizer.tokenize(text)) < max_length:
                prompt_ms = f"""
    for the following paragraph, berikan perenggan yang sama dalam bahasa Melayu berkualiti tinggi seperti dalam ayat dalam Wikipedia

    {text}
    """
                messages = [
                    {'role': 'user', 'content': prompt_ms.strip()},
                ]
                prompt = tokenizer.apply_chat_template(messages, tokenize=False)
                inputs = tokenizer(
                    [prompt],
                    return_tensors='pt',
                    add_special_tokens=False).to('cuda')
                generate_kwargs = dict(
                    inputs,
                    max_new_tokens=4096,
                    top_p=0.95,
                    top_k=50,
                    temperature=0.9,
                    do_sample=True,
                    num_beams=1,
                )
                r = model.generate(**generate_kwargs)
                r = tokenizer.decode(r[0])
                data = {'src': text, 'r': r}

                d = json.dumps(data)
                file.write(f'{d}\n')
                file.flush()

            pointer.index = i
            pointer._save()

file.close()
