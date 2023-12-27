stt-semisupervised
==================

Malay
-----

how-to
~~~~~~

1. Download Malay youtube videos, `download-videos.ipynb <download-videos.ipynb>`__.

2. Run semisupervised using Google Speech, `semisupervised-googlespeech.py <semisupervised-googlespeech.py>`__.

3. Run `transcribe.ipynb <transcribe.ipynb>`__ to correct output from googlespeech.

::

   All the videos, songs, images, and graphics used in the video belong to their respective owners and I does not claim any right over them.

   Copyright Disclaimer under section 107 of the Copyright Act of 1976, allowance is made for "fair use" for purposes such as criticism, comment, news reporting, teaching, scholarship, education and research. Fair use is a use permitted by copyright statute that might otherwise be infringing.


Download
~~~~~~~~

1. https://f000.backblazeb2.com/file/malay-dataset/speech/semisupervised-malay.tar.gz

16k sample rate, atleast 90% voice activity, 93 hours.

2. https://f000.backblazeb2.com/file/malay-dataset/speech/semisupervised-malay-part2.tar.gz

16k sample rate, atleast 90% voice activity, 70 hours.

3. https://f000.backblazeb2.com/file/malay-dataset/speech/semisupervised-malay-part3.tar.gz

16k sample rate, atleast 90% voice activity, 59 hours.

4. V2, https://f000.backblazeb2.com/file/malay-dataset/speech/semisupervised-26-02-2021-part1.tar

16k sample rate, atleast 90% voice activity, 36 hours.

5. V2, https://f000.backblazeb2.com/file/malay-dataset/speech/semisupervised-26-02-2021-part2.tar

16k sample rate, atleast 90% voice activity, 68 hours.

6. V2, https://f000.backblazeb2.com/file/malay-dataset/speech/semisupervised-26-02-2021-part3.tar

16k sample rate, atleast 90% voice activity, 250 hours.

7. V2, https://f000.backblazeb2.com/file/malay-dataset/speech/semisupervised-26-02-2021-part4.tar

16k sample rate, atleast 90% voice activity, 265 hours.

8. V3, https://f000.backblazeb2.com/file/malay-dataset/speech/semisupervised-24-03-2021-part1.tar

16k sample rate, atleast 80% voice activity, 660 hours.

9. V3, https://f000.backblazeb2.com/file/malay-dataset/speech/semisupervised-24-03-2021-part2.tar

16k sample rate, atleast 80% voice activity, 688 hours.

10. V3, https://f000.backblazeb2.com/file/malay-dataset/speech/semisupervised-24-03-2021-part3.tar

16k sample rate, atleast 80% voice activity, 456 hours.

Download supervised
~~~~~~~~~~~~~~~~~~~

1. `label-semisupervised-malay.tar.gz <label-semisupervised-malay.tar.gz>`__

- 16000 sample rate.
- random length between 2 - 20 seconds, windowed using google VAD.
- 768 over 57895 done, approximate 1.3 hours.

Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Semisupervised Speech Recognition from Malay Youtube Videos,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malaya-speech/tree/master/data/semisupervised-malay}}
   }

Manglish
--------

how-to
~~~~~~

1. Download Malay youtube videos, `download-videos.ipynb <download-videos.ipynb>`__.

2. Run semisupervised using Google Speech, `semisupervised-googlespeech.py <semisupervised-googlespeech.py>`__.

16k sample rate, atleast 90% voice activity, 107 hours.

Download at https://f000.backblazeb2.com/file/malay-dataset/speech/semisupervised-manglish.tar.gz

::

   All the videos, songs, images, and graphics used in the video belong to their respective owners and I does not claim any right over them.

   Copyright Disclaimer under section 107 of the Copyright Act of 1976, allowance is made for "fair use" for purposes such as criticism, comment, news reporting, teaching, scholarship, education and research. Fair use is a use permitted by copyright statute that might otherwise be infringing.


3. Run `transcribe.ipynb <transcribe.ipynb>`__ to correct output from googlespeech.

Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Semisupervised Speech Recognition from Manglish Youtube Videos,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malaya-speech/tree/master/data/semisupervised-manglish}}
   }

Nusantara Audiobook
-------------------

This directory to gather semisupervised transcribed on Malay audiobook.

::

   All the videos, songs, images, and graphics used in the video belong to their respective owners and I does not claim any right over them.

   Copyright Disclaimer under section 107 of the Copyright Act of 1976, allowance is made for "fair use" for purposes such as criticism, comment, news reporting, teaching, scholarship, education and research. Fair use is a use permitted by copyright statute that might otherwise be infringing.


Download
~~~~~~~~

1. https://f000.backblazeb2.com/file/malaya-speech-model/data/dari-pasentran-ke-istana.gz

- Originally from https://nusantaraudiobooks.com/books/dari-pesantren-ke-istana-biografi-presiden-ke-4-indonesia-kiai-haji-abdurrahman-wahid
- 44100 sample rate, super clean.
- narrator Danny Abdullah.
- approximate 19.63 hours.
- VAD = 2, https://f000.backblazeb2.com/file/malaya-speech-model/data/dari-pasentran-ke-istana-short.gz
- Semisupervised using PyTorch Conformer Medium, `semisupervised-pasentran-turki.json <semisupervised-pasentran-turki.json>`__, notebook `semisupervised-pasentran-turki.ipynb <semisupervised-pasentran-turki.ipynb>`__.
- Put commas and apply true case, `true-case-pasentran-turki.json <https://huggingface.co/datasets/mesolitica/put-comma-true-case-audiobook/raw/main/true-case-pasentran-turki.json>`__ notebook `put-comma-true-case-pasentran-turki.ipynb <put-comma-true-case-pasentran-turki.ipynb>`__

2. https://f000.backblazeb2.com/file/malaya-speech-model/data/turki.gz

- Originally from https://nusantaraudiobooks.com/books/dari-sultan-hingga-ataturk-turki
- 44100 sample rate, super clean.
- narrator Danny Abdullah.
- approximate 7.73 hours.
- VAD = 2, https://f000.backblazeb2.com/file/malaya-speech-model/data/turki-short.gz
- Semisupervised using PyTorch Conformer Medium, `semisupervised-pasentran-turki.json <semisupervised-pasentran-turki.json>`__, notebook `semisupervised-pasentran-turki.ipynb <semisupervised-pasentran-turki.ipynb>`__.
- Put commas and apply true case, `true-case-pasentran-turki.json <https://huggingface.co/datasets/mesolitica/put-comma-true-case-audiobook/raw/main/true-case-pasentran-turki.json>`__ notebook `put-comma-true-case-pasentran-turki.ipynb <put-comma-true-case-pasentran-turki.ipynb>`__

3. https://f000.backblazeb2.com/file/malaya-speech-model/data/salina.gz

- Originally from https://nusantaraudiobooks.com/books/salina
- 44100 sample rate, super clean.
- narrator T Elida Bustaman.
- approximate 24.66 hours.
- VAD = 2, https://f000.backblazeb2.com/file/malaya-speech-model/data/salina-short.gz
- Semisupervised using PyTorch Conformer Medium, `semisupervised-salina.json <semisupervised-salina.json>`__, notebook `semisupervised-salina.ipynb <semisupervised-salina.ipynb>`__.
- Put commas and apply true case, `true-case-salina.json <https://huggingface.co/datasets/mesolitica/put-comma-true-case-audiobook/raw/main/true-case-salina.json>`__ notebook `put-comma-true-case-salina.ipynb <put-comma-true-case-salina.ipynb>`__

4. Text only, https://f000.backblazeb2.com/file/malaya-speech-model/data/text-audiobook.tar.gz

5. Test set, https://f000.backblazeb2.com/file/malaya-speech-model/data/testset-audiobook.tar.gz

6. Train set with augmentation, https://f000.backblazeb2.com/file/malaya-speech-model/data/trainset-audiobook.tar.gz

7. https://f000.backblazeb2.com/file/malaya-speech-model/data/salina-supervised-sani.tar.gz

- Originally from https://nusantaraudiobooks.com/books/salina
- Supervised by https://github.com/khursani8
- approximate 19.32 hours.
- Put commas and apply true case, `comma-salina-sani.json <comma-salina-sani.json>`__, notebook `alignment-salina-sani.ipynb <alignment-salina-sani.ipynb>`__.

8. https://f000.backblazeb2.com/file/malaya-speech-model/data/dari-pasentran-ke-istana-supervised-sani.tar.gz

- Originally from https://nusantaraudiobooks.com/books/dari-pesantren-ke-istana-biografi-presiden-ke-4-indonesia-kiai-haji-abdurrahman-wahid
- Supervised by https://github.com/khursani8
- approximate 13.84 hours.
- Put commas and apply true case, `comma-dari-pasentran-ke-istana-sani.json <comma-dari-pasentran-ke-istana-sani.json>`__, notebook `alignment-dari-pasentran-ke-istana-sani.ipynb <alignment-dari-pasentran-ke-istana-sani.ipynb>`__.

Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Semisupervised Speech Recognition from Audiobook,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malaya-speech/tree/master/data/semisupervised-audiobook}}
   }

distributed multi-GPUs pseudolabel using Whisper
------------------------------------------------

This pseudolabel included fast hashing load audio files and continue last step decoded.

how-to
~~~~~~

1. Prepare chunks hash map, `prepare-indices-chunks.ipynb <prepare-indices-chunks.ipynb>`__.

2. Generate chunks hash map, `generate-global-indices.ipynb <generate-global-indices.ipynb>`__.

Use accelerate
^^^^^^^^^^^^^^

1. Configure accelerate,

.. code:: bash

   accelerate config

2. Run accelerate,

.. code:: bash

   ~/my-env/bin/accelerate launch run.py --indices_filename=global-indices.json --batch_size=4

Use torchrun
^^^^^^^^^^^^

.. code:: bash

   NCCL_P2P_DISABLE=1 NCCL_IB_DISABLE=1 ~/my-env/bin/torchrun --nproc_per_node 2 \
   -m run \
   --indices_filename=global-indices.json --batch_size=4

NCCL is not required.

Run in 4x A100
""""""""""""""

We use batch size of 52,

.. code:: bash

   NCCL_P2P_DISABLE=1 NCCL_IB_DISABLE=1 torchrun --nproc_per_node 4 \
   -m run \
   --indices_filename=crawl-youtube-global-indices.json --batch_size=52

Noisy Audiobook
---------------

::

   All the videos, songs, images, and graphics used in the video belong to their respective owners and I does not claim any right over them.

   Copyright Disclaimer under section 107 of the Copyright Act of 1976, allowance is made for "fair use" for purposes such as criticism, comment, news reporting, teaching, scholarship, education and research. Fair use is a use permitted by copyright statute that might otherwise be infringing.


download
~~~~~~~~

1. Harry Potter,

- audio, https://huggingface.co/datasets/mesolitica/semisupervised-audiobook/resolve/main/harry-potter-noisy.tar.gz
- transcription, https://huggingface.co/datasets/mesolitica/semisupervised-audiobook/resolve/main/harry-potter-processed.json

2. Teme,

- audio, https://huggingface.co/datasets/mesolitica/semisupervised-audiobook/resolve/main/teme-noisy.tar.gz
- transcription, https://huggingface.co/datasets/mesolitica/semisupervised-audiobook/resolve/main/teme-processed.json

3. Bukan Kerana Aku,

- audio, https://huggingface.co/datasets/mesolitica/semisupervised-audiobook/resolve/main/bukan-kerana-aku-noisy.tar.gz
- transcription, https://huggingface.co/datasets/mesolitica/semisupervised-audiobook/resolve/main/bukan-kerana-aku-processed.json
