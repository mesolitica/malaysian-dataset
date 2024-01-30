import os
os.environ['CUDA_VISIBLE_DEVICES'] = '1'

import json
from pprint import pprint
from transformers import AutoModelForCausalLM, AutoTokenizer
from tqdm import tqdm
import torch
import random

os.makedirs('llava-multi', exist_ok=True)

tokenizer = AutoTokenizer.from_pretrained('mistralai/Mistral-7B-Instruct-v0.2')
model = AutoModelForCausalLM.from_pretrained(
    'mistralai/Mistral-7B-Instruct-v0.2',
    use_flash_attention_2=True,
    torch_dtype=torch.float16
)
tokenizer.pad_token = tokenizer.eos_token
model.cuda()


def predict(prompt):
    inputs = tokenizer(
        prompt,
        return_tensors='pt',
        add_special_tokens=False,
        padding=True).to('cuda')
    generate_kwargs = dict(
        inputs,
        max_new_tokens=1024,
        top_p=0.95,
        top_k=50,
        temperature=0.3,
        do_sample=True,
        num_beams=1,
    )
    response = model.generate(**generate_kwargs).to('cpu')
    return response


data = []
with open('llava-multi-images-template.jsonl') as fopen:
    for l in fopen:
        data.append(json.loads(l))

for i in tqdm(range(len(data))):
    filename = os.path.join('llava-multi', f'{i}.json')
    if os.path.exists(filename):
        continue

    prompts = data[i]['prompts']
    response = predict(prompts)
    decoded_response = tokenizer.batch_decode(response, skip_special_tokens=True)
    with open(filename, 'w') as fopen:
        json.dump(decoded_response, fopen)
