from pydub import AudioSegment
from tqdm import tqdm
from glob import glob
import os
import numpy as np
import subprocess
import re
import soundfile as sf
import mp

max_hours = 4

def get_length(file):
    process = subprocess.Popen(
        ['ffmpeg', '-i', file],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    stdout, stderr = process.communicate()
    matches = re.search(
        r"Duration:\s{1}(?P<hours>\d+?):(?P<minutes>\d+?):(?P<seconds>\d+\.\d+?),",
        stdout.decode(),
        re.DOTALL).groupdict()
    return float(matches['hours']) * 60 * 60 + \
        float(matches['minutes']) * 60 + float(matches['seconds'])

os.makedirs('filtered-24k', exist_ok = True)
files = glob('my-videos/audio/*.mp3')
files.extend(glob('my-videos/*.mp3'))
len(files)

def standardization(audio):
    """
    Preprocess the audio file, including setting sample rate, bit depth, channels, and volume normalization.

    Args:
        audio (str or AudioSegment): Audio file path or AudioSegment object, the audio to be preprocessed.

    Returns:
        dict: A dictionary containing the preprocessed audio waveform, audio file name, and sample rate, formatted as:
              {
                  "waveform": np.ndarray, the preprocessed audio waveform, dtype is np.float32, shape is (num_samples,)
                  "name": str, the audio file name
                  "sample_rate": int, the audio sample rate
              }

    Raises:
        ValueError: If the audio parameter is neither a str nor an AudioSegment.
    """
    name = "audio"
    
    if (get_length(audio) / 60 / 60) > max_hours:
        return None

    if isinstance(audio, str):
        name = os.path.basename(audio)
        audio = AudioSegment.from_file(audio)
    elif isinstance(audio, AudioSegment):
        name = f"audio_{audio_count}"
        audio_count += 1
    else:
        raise ValueError("Invalid audio type")

    if (audio.duration_seconds / 60 / 60) > max_hours:
        return None

    # Convert the audio file to WAV format
    audio = audio.set_frame_rate(24000)
    audio = audio.set_sample_width(2)  # Set bit depth to 16bit
    audio = audio.set_channels(1)  # Set to mono

    # Calculate the gain to be applied
    target_dBFS = -20
    gain = target_dBFS - audio.dBFS

    # Normalize volume and limit gain range to between -3 and 3
    normalized_audio = audio.apply_gain(min(max(gain, -3), 3))

    waveform = np.array(normalized_audio.get_array_of_samples(), dtype=np.float32)
    max_amplitude = np.max(np.abs(waveform))
    if max_amplitude == 0:
        return None
    waveform /= max_amplitude  # Normalize

    return {
        "waveform": waveform,
        "name": name,
        "sample_rate": 24000,
    }

def loop(files):
    files, index = files
    for f in tqdm(files):
        filename = os.path.join('filtered-24k', os.path.split(f)[1])
        if os.path.exists(filename) and os.stat(filename).st_size > 1000:
            continue
        try:
            r = standardization(f)
            if r is None:
                continue
            
            sf.write(filename, r['waveform'], r['sample_rate'])
        except Exception as e:
            print(e)
    print(index, 'done')
    
# loop((files, 0))
mp.multiprocessing(files, loop, cores = 15, returned = False)