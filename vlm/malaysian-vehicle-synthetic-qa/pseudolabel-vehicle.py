from accelerate import Accelerator, InitProcessGroupKwargs
from torch.utils.data import DataLoader, Dataset
from datetime import datetime, timedelta
from dataclasses import dataclass
from glob import glob
import numpy as np
import torch
import json
import os
import re
from copy import deepcopy
from tqdm import tqdm
from io import BytesIO
from PIL import Image
from transformers import AutoModel, AutoTokenizer, HfArgumentParser


def collactor(rows):
    results = []
    for row in rows:
        if row is None:
            continue
        results.append(row)
    return results


class Train(Dataset):
    def __init__(self, file):
        self.data = []
        with open(file) as fopen:
            for l in fopen:
                l = json.loads(l)
                self.data.append(l)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        try:
            d = self.data[item].copy()
            image = Image.open(d['filename']).convert('RGB')
            d['image'] = image
            return d
        except BaseException as e:
            print(e)
            return None


@dataclass
class ModelArguments:
    indices_filename: 'str' = 'save-image-vehicle.jsonl'
    folder_output: str = 'output-vehicle'
    batch_size: int = 8
    dataloader_num_workers: int = 1
    no_question: int = 2


def main():
    global_rank = int(os.environ['RANK'])
    parser = HfArgumentParser(ModelArguments)
    model_args = parser.parse_args_into_dataclasses()[0]
    print(global_rank, model_args)

    os.makedirs(model_args.folder_output, exist_ok=True)

    torch_dtype = torch.bfloat16
    mixed_precision = 'bf16'
    kwargs = InitProcessGroupKwargs(timeout=timedelta(seconds=7200))
    accelerator = Accelerator(
        mixed_precision=mixed_precision,
        kwargs_handlers=[kwargs],
    )
    model = AutoModel.from_pretrained(
        'openbmb/MiniCPM-Llama3-V-2_5',
        trust_remote_code=True,
        attn_implementation='flash_attention_2',
        torch_dtype=torch_dtype
    )
    tokenizer = AutoTokenizer.from_pretrained(
        'openbmb/MiniCPM-Llama3-V-2_5', trust_remote_code=True)
    model = model.to(device='cuda')
    model.eval()
    _ = model.cuda()
    print(global_rank, model.dtype, model.device)

    existed = set()
    cars = {}
    with open('car-data.jsonl') as fopen:
        for l in fopen:
            l = json.loads(l)
            im = l['local_image'].split('_')[0]
            im = os.path.split(im)[1]
            if im not in existed:
                cars[im] = l
                existed.add(im)

    train = Train(model_args.indices_filename)
    dataloader = DataLoader(
        train,
        batch_size=model_args.batch_size,
        collate_fn=collactor,
        num_workers=model_args.dataloader_num_workers,
        pin_memory=True,
    )
    dataloader = accelerator.prepare(dataloader)

    start_step = 0
    steps = glob(os.path.join(model_args.folder_output, f'{global_rank}-*.json'))
    steps = [int(f.split('-')[-1].replace('.json', '')) for f in steps]
    if len(steps):
        start_step = max(steps)
        print(f'{global_rank}, continue from {start_step}')
    else:
        print(f'{global_rank}, failed to load last step count, continue from 0')

    dataloader = accelerator.skip_first_batches(dataloader, num_batches=start_step)
    batches = tqdm(dataloader, disable=not accelerator.is_local_main_process)

    for step, batch in enumerate(batches):
        step = step + start_step

        input_id_list, img_list, tgt_sizess = [], [], []

        for row in batch:
            keyword = row['keyword']
            image = row['image']
            t = f"""
vehicle name: {keyword}
this image gathered using the vehicle on google search, based on the image BUT DO NOT MENTIONED THE VEHICLE NAME,

generate a follow up question only related to the image
            """.strip()
            msgs = [{'role': 'user', 'content': t}]
            row = msgs
            copy_msgs = deepcopy(row)
            if image is not None and isinstance(copy_msgs[0]['content'], str):
                copy_msgs[0]['content'] = [image, copy_msgs[0]['content']]

            images = []
            tgt_sizes = []
            for i, msg in enumerate(copy_msgs):
                role = msg["role"]
                content = msg["content"]
                assert role in ["user", "assistant"]
                if i == 0:
                    assert role == "user", "The role of first msg should be user"
                if isinstance(content, str):
                    content = [content]

                cur_msgs = []
                for c in content:
                    if isinstance(c, Image.Image):
                        image = c
                        if model.config.slice_mode:
                            slice_images, image_placeholder = model.get_slice_image_placeholder(
                                image, tokenizer
                            )
                            cur_msgs.append(image_placeholder)
                            for slice_image in slice_images:
                                slice_image = model.transform(slice_image)
                                H, W = slice_image.shape[1:]
                                images.append(model.reshape_by_patch(slice_image))
                                tgt_sizes.append(torch.Tensor(
                                    [H // model.config.patch_size, W // model.config.patch_size]).type(torch.int32))
                        else:
                            images.append(model.transform(image))
                            cur_msgs.append(
                                tokenizer.im_start
                                + tokenizer.unk_token * model.config.query_num
                                + tokenizer.im_end
                            )
                    elif isinstance(c, str):
                        cur_msgs.append(c)

                msg['content'] = '\n'.join(cur_msgs)

            tgt_sizes = torch.vstack(tgt_sizes)
            input_ids = tokenizer.apply_chat_template(
                copy_msgs, tokenize=True, add_generation_prompt=False)
            input_id_list.append(input_ids)
            img_list.append(images)
            tgt_sizess.append(tgt_sizes)

        generation_config = {
            "top_p": 0.95,
            "top_k": 100,
            "temperature": 0.9,
            "do_sample": True,
            "repetition_penalty": 1.05
        }
        pattern = r'"(.*?)"'

        questions = []
        while len(questions) < model_args.no_question:
            with torch.inference_mode():
                res, vision_hidden_states = model.generate(
                    input_id_list=input_id_list,
                    max_inp_length=4096,
                    img_list=img_list,
                    tgt_sizes=tgt_sizess,
                    tokenizer=tokenizer,
                    max_new_tokens=1024,
                    vision_hidden_states=None,
                    return_vision_hidden_states=True,
                    stream=False,
                    **generation_config
                )
                selected = []
                for r in res:
                    if r.endswith('?'):
                        selected.append(r)
                        continue

                    match = re.search(pattern, r)
                    if match:
                        question = match.group(1)
                        selected.append(question)

                if len(selected) == len(input_id_list):
                    questions.append(selected)

        questions = [['describe everything'] * len(batch)] + questions
        print(len(questions), len(questions[0]))
        new_questions = []
        for no, q in enumerate(questions):
            qs = []
            for q_ in q:
                keyword = batch[no]['keyword']
                t = f"""
vehicle name: {keyword}
this image gathered using the vehicle on google search, based on the image BUT DO NOT MENTIONED THE VEHICLE NAME,

{q_}
                """.strip()
                qs.append(t)
            new_questions.append(qs)

        answers = []
        for i in range(len(new_questions)):
            new_input_ids = []
            for k in range(len(new_questions[i])):
                msgs = [{'role': 'user', 'content': new_questions[i][k]}]
                input_ids = tokenizer.apply_chat_template(
                    msgs, tokenize=True, add_generation_prompt=False)
                new_input_ids.append(input_ids)

            print(len(img_list), len(new_input_ids))

            res, vision_hidden_states = model.generate(
                input_id_list=new_input_ids,
                max_inp_length=4096,
                img_list=img_list,
                tgt_sizes=tgt_sizess,
                tokenizer=tokenizer,
                max_new_tokens=1024,
                vision_hidden_states=None,
                return_vision_hidden_states=True,
                stream=False,
                **generation_config
            )
            answers.append(res)

        answers = np.array(answers).T.tolist()
        questions = np.array(questions).T.tolist()
        data = []
        for k in range(len(batch)):
            batch[k].pop('image', None)
            batch[k]['questions'] = questions[k]
            batch[k]['answers'] = answers[k]
            data.append(batch[k])

        filename = os.path.join(model_args.folder_output, f'{global_rank}-{step}.json')
        with open(filename, 'w') as fopen:
            json.dump(data, fopen)

    accelerator.wait_for_everyone()


if __name__ == "__main__":
    main()
