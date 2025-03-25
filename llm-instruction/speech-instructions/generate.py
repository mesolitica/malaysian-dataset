import click
from dynamicbatch_ttspipeline.f5_tts.load import (
    load_f5_tts,
    load_vocoder,
    target_sample_rate,
    hop_length,
    nfe_step,
    cfg_strength,
    sway_sampling_coef,
)
from dynamicbatch_ttspipeline.f5_tts.utils import (
    chunk_text,
    convert_char_to_pinyin,
)
from pydub import AudioSegment, silence
from tqdm import tqdm
import torchaudio
import torch
import torch.nn.functional as F
import numpy as np
import librosa
import soundfile as sf
import json
from ctc_forced_aligner import (
    load_audio,
    load_alignment_model,
    generate_emissions,
    preprocess_text,
    get_alignments,
    get_spans,
    postprocess_results,
)
import re
import os

language = 'ms'
torch_dtype = torch.bfloat16
device = 'cuda'
batch_size = 16

@click.command()
@click.option('--model_name', default = 'mesolitica/Malaysian-F5-TTS-v2')
@click.option('--input_file')
@click.option('--folder')
@click.option('--global_index', default = 1)
@click.option('--index', default = 0)
@click.option('--retry', default = 5)
@click.option('--threshold', default = -15)
@click.option('--maxlen', default = 200)
def main(model_name, input_file, folder, global_index, index, retry, threshold, maxlen):
    alignment_model, alignment_tokenizer = load_alignment_model(
        device,
        dtype=torch.float16 if device == "cuda" else torch.float32,
    )
    model = load_f5_tts(
        model_name = model_name, 
        device = device, 
        dtype = torch.float16,
    )
    _ = model.eval()
    vocoder = load_vocoder(device = device)

    folder_fail = folder + '-failed'
    folder_force_alignment = folder + '-alignment_alignment'
    os.makedirs(folder, exist_ok = True)
    os.makedirs(folder_fail, exist_ok = True)
    os.makedirs(folder_force_alignment, exist_ok = True)

    with open(input_file) as fopen:
        instructions = json.load(fopen)

    for i in tqdm(range((len(instructions) // global_index) * index, (len(instructions) // global_index) * (index + 1), 1)):
        
        new_filename = os.path.join(folder, f'{i}.mp3')
        if os.path.exists(new_filename):
            continue
        
        failed_filename = os.path.join(folder_fail, f'{i}.mp3')
        if os.path.exists(failed_filename):
            continue

        new_filename_force_alignment = os.path.join(folder_force_alignment, f'{i}.json')

        voice = instructions[i]['speaker']['audio']
        original_text = instructions[i]['speaker']['transcription']

        audio_input = voice
        dwav, sr_ = torchaudio.load(audio_input)
        dwav = dwav.mean(dim=0).numpy()
        target_rms = 0.1
        audio = dwav
        rms = np.sqrt(np.mean(np.square(audio)))
        if rms < target_rms:
            audio = audio * target_rms / rms

        if sr_ != target_sample_rate:
            audio = librosa.resample(audio, orig_sr = sr_, target_sr = target_sample_rate)
            
        audios = torch.tensor(audio)[None].cuda()

        ref_text = original_text
        if not ref_text.endswith(". ") and not ref_text.endswith("。"):
            if ref_text.endswith("."):
                ref_text += " "
            else:
                ref_text += ". "
        
        max_chars = int(len(ref_text.encode("utf-8")) / (audios.shape[-1] / sr_) * (25 - audios.shape[-1] / sr_))
        ref_audio_len = audios.shape[-1] // hop_length
        speed = 1

        if 'pronunciation' in instructions[i] and len(instructions[i]['pronunciation']):
            gen_text = instructions[i]['pronunciation']
        else:
            gen_text = instructions[i]['question']
        gen_text = gen_text.replace('\'', '').replace('"', '').replace('!', '.')
        gen_text = re.sub(r'[ ]+', ' ', gen_text).strip()
        if len(gen_text) < 3:
            continue
        if len(gen_text) > maxlen:
            continue
        gen_text  = f'. {gen_text}'
        final_text_lists, durations, after_durations = [], [], []
        text_list = [ref_text + gen_text]
        final_text_list = convert_char_to_pinyin(text_list)
        ref_text_len = len(ref_text.encode("utf-8"))
        gen_text_len = len(gen_text.encode("utf-8"))
        after_duration = int(ref_audio_len / ref_text_len * gen_text_len / speed)
        final_text_lists = [final_text_list[0]]
        durations = [ref_audio_len + after_duration]
        after_durations = [after_duration]
        
        failed = True

        for _ in range(retry):
            with torch.no_grad():
                generated, _ = model.sample(
                    cond=audios.repeat(len(final_text_lists), 1),
                    text=final_text_lists,
                    duration=torch.Tensor(durations).to(device).type(torch.long),
                    steps=nfe_step,
                    cfg_strength=2,
                    sway_sampling_coef=-1.0,
                )
                generated_mel_spec = generated.to(torch.float32)[:, ref_audio_len:, :].permute(0, 2, 1)
                generated_wave = vocoder.decode(generated_mel_spec)
                if rms < target_rms:
                    generated_wave = generated_wave * rms / target_rms
                actual_after_durations = [d * hop_length for d in after_durations]
                new_wav = generated_wave[0, :actual_after_durations[0]]
                audio_waveform = torchaudio.functional.resample(
                    new_wav, orig_freq=24000, new_freq=16000
                ).type(torch.float16)
                emissions, stride = generate_emissions(
                    alignment_model, audio_waveform, batch_size=1
                )
                tokens_starred, text_starred = preprocess_text(
                    gen_text,
                    romanize=True,
                    language=language,
                )
                segments, scores, blank_token = get_alignments(
                    emissions,
                    tokens_starred,
                    alignment_tokenizer,
                )
                spans = get_spans(tokens_starred, segments, blank_token)
                word_timestamps = postprocess_results(text_starred, spans, stride, scores)
                scores = [w['score'] for w in word_timestamps if w['score'] <= threshold]
                if not len(scores):
                    a = new_wav.cpu().numpy()
                    sf.write(new_filename, a, 24000)
                    with open(new_filename_force_alignment, 'w') as fopen:
                        json.dump(word_timestamps, fopen)
                    failed = False
                    break
        
        if failed:
            with open(failed_filename, 'w') as fopen:
                fopen.write('yes')

if __name__ == '__main__':
    main()