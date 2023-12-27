# Azure TTS

This directory to gather semisupervised transcribed on Azure Malay TTS.

```
All the videos, songs, images, and graphics used in the video belong to their respective owners and I does not claim any right over them.

Copyright Disclaimer under section 107 of the Copyright Act of 1976, allowance is made for "fair use" for purposes such as criticism, comment, news reporting, teaching, scholarship, education and research. Fair use is a use permitted by copyright statute that might otherwise be infringing.
```

Read more about commercial usage at https://docs.microsoft.com/en-us/answers/questions/460557/microsoft-azure-text-to-speech-commercial-usage.html

Guidelines for responsible deployment of synthetic voice technology, https://docs.microsoft.com/en-us/legal/cognitive-services/speech-service/custom-neural-voice/concepts-guidelines-responsible-deployment-synthetic

## Download

1. https://huggingface.co/datasets/mesolitica/azure-tts-yasmin/resolve/main/news-wavs.tar

  - 24000 sample rate, super clean.
  - narrator `ms-MY-YasminNeural`.
  - approximate 99.4 hours.
  - Texts from Malay Wikipedia and News.
  - Sentences between 2 words and 20 words.
  - transcription, https://huggingface.co/datasets/mesolitica/azure-tts-yasmin/resolve/main/postprocessing-edge-tts-news-yasmin.json

2. https://huggingface.co/datasets/mesolitica/azure-tts-yasmin/resolve/main/parliament-wavs.tar

  - 24000 sample rate, super clean.
  - narrator `ms-MY-YasminNeural`.
  - approximate 142 hours.
  - Texts from Malaysia Malay Parliament.
  - Sentences between 2 words and 25 words.
  - transcription, https://huggingface.co/datasets/mesolitica/azure-tts-yasmin/resolve/main/postprocessing-edge-tts-parliament-yasmin.json

3. https://huggingface.co/datasets/mesolitica/azure-tts-yasmin-wikipedia/resolve/main/yasmin-wiki.tar

  - 24000 sample rate, super clean.
  - narrator `ms-MY-YasminNeural`.
  - approximate 224 hours.
  - Texts from Malay Wikipedia.
  - Sentences between 2 words and 25 words.
  - transcription, https://huggingface.co/datasets/mesolitica/azure-tts-yasmin-wikipedia/resolve/main/postprocessing-edge-tts-wiki-yasmin.json

4. https://huggingface.co/datasets/mesolitica/azure-tts-osman/resolve/main/news-wavs.tar

  - 24000 sample rate, super clean.
  - narrator `ms-MY-OsmanNeural`.
  - approximate 94.5 hours.
  - Texts from Malay Wikipedia and News.
  - Sentences between 2 words and 20 words.
  - transcription, https://huggingface.co/datasets/mesolitica/azure-tts-osman/resolve/main/postprocessing-edge-tts-news.json

5. https://huggingface.co/datasets/mesolitica/azure-tts-osman/resolve/main/parliament-wavs.tar

  - 24000 sample rate, super clean.
  - narrator `ms-MY-OsmanNeural`.
  - approximate 133.2 hours.
  - Texts from Malaysia Malay Parliament.
  - Sentences between 2 words and 25 words.
  - transcription, https://huggingface.co/datasets/mesolitica/azure-tts-osman/resolve/main/postprocessing-edge-tts-parliament.json

6. https://huggingface.co/datasets/mesolitica/azure-tts-osman-wikipedia/resolve/main/osman-wiki.tar

  - 24000 sample rate, super clean.
  - narrator `ms-MY-OsmanNeural`.
  - approximate 224 hours.
  - Texts from Malay Wikipedia.
  - Sentences between 2 words and 20 words.
  - transcription, https://huggingface.co/datasets/mesolitica/azure-tts-osman-wikipedia/resolve/main/postprocessing-edge-tts-wiki-osman.json

7. https://huggingface.co/datasets/mesolitica/synthetic-azure-tts/resolve/main/yasmin-synthetic.tar

  - 24000 sample rate, super clean.
  - narrator `ms-MY-YasminNeural`.
  - Random texts generated using [edge-tts-synthetic-yasmin.ipynb](edge-tts-synthetic-yasmin.ipynb).
  - transcription, [synthetic-data-tts.json](synthetic-data-tts.json).

8. https://huggingface.co/datasets/mesolitica/synthetic-azure-tts/resolve/main/osman-synthetic.tar

  - 24000 sample rate, super clean.
  - narrator `ms-MY-OsmanNeural`.
  - Random texts generated using [edge-tts-synthetic-osman.ipynb](edge-tts-synthetic-osman.ipynb).
  - transcription, [synthetic-data-tts.json](synthetic-data-tts.json).