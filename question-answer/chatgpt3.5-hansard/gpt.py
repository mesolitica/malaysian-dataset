import openai
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import os
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)


# read eviroment variable
openai.api_key = os.environ.get('OPENAI_API_KEY')
