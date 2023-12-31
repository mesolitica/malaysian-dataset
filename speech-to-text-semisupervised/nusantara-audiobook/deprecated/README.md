# Nusantara Audiobook

This directory to gather semisupervised transcribed on Malay audiobook.

```
All the videos, songs, images, and graphics used in the video belong to their respective owners and I does not claim any right over them.

Copyright Disclaimer under section 107 of the Copyright Act of 1976, allowance is made for "fair use" for purposes such as criticism, comment, news reporting, teaching, scholarship, education and research. Fair use is a use permitted by copyright statute that might otherwise be infringing.
```

## Download

1. https://f000.backblazeb2.com/file/malaya-speech-model/data/dari-pasentran-ke-istana.gz

  - Originally from https://nusantaraudiobooks.com/books/dari-pesantren-ke-istana-biografi-presiden-ke-4-indonesia-kiai-haji-abdurrahman-wahid
  - 44100 sample rate, super clean.
  - narrator Danny Abdullah.
  - approximate 19.63 hours.
  - VAD = 2, https://f000.backblazeb2.com/file/malaya-speech-model/data/dari-pasentran-ke-istana-short.gz
  - Semisupervised using PyTorch Conformer Medium, [semisupervised-pasentran-turki.json](semisupervised-pasentran-turki.json), notebook [semisupervised-pasentran-turki.ipynb](semisupervised-pasentran-turki.ipynb).
  - Put commas and apply true case, [true-case-pasentran-turki.json](https://huggingface.co/datasets/mesolitica/put-comma-true-case-audiobook/raw/main/true-case-pasentran-turki.json) notebook [put-comma-true-case-pasentran-turki.ipynb](put-comma-true-case-pasentran-turki.ipynb)

2. https://f000.backblazeb2.com/file/malaya-speech-model/data/turki.gz

  - Originally from https://nusantaraudiobooks.com/books/dari-sultan-hingga-ataturk-turki
  - 44100 sample rate, super clean.
  - narrator Danny Abdullah.
  - approximate 7.73 hours.
  - VAD = 2, https://f000.backblazeb2.com/file/malaya-speech-model/data/turki-short.gz
  - Semisupervised using PyTorch Conformer Medium, [semisupervised-pasentran-turki.json](semisupervised-pasentran-turki.json), notebook [semisupervised-pasentran-turki.ipynb](semisupervised-pasentran-turki.ipynb).
  - Put commas and apply true case, [true-case-pasentran-turki.json](https://huggingface.co/datasets/mesolitica/put-comma-true-case-audiobook/raw/main/true-case-pasentran-turki.json) notebook [put-comma-true-case-pasentran-turki.ipynb](put-comma-true-case-pasentran-turki.ipynb)

3. https://f000.backblazeb2.com/file/malaya-speech-model/data/salina.gz

  - Originally from https://nusantaraudiobooks.com/books/salina
  - 44100 sample rate, super clean.
  - narrator T Elida Bustaman.
  - approximate 24.66 hours.
  - VAD = 2, https://f000.backblazeb2.com/file/malaya-speech-model/data/salina-short.gz
  - Semisupervised using PyTorch Conformer Medium, [semisupervised-salina.json](semisupervised-salina.json), notebook [semisupervised-salina.ipynb](semisupervised-salina.ipynb).
  - Put commas and apply true case, [true-case-salina.json](https://huggingface.co/datasets/mesolitica/put-comma-true-case-audiobook/raw/main/true-case-salina.json) notebook [put-comma-true-case-salina.ipynb](put-comma-true-case-salina.ipynb)

4. Text only, https://f000.backblazeb2.com/file/malaya-speech-model/data/text-audiobook.tar.gz

5. Test set, https://f000.backblazeb2.com/file/malaya-speech-model/data/testset-audiobook.tar.gz

6. Train set with augmentation, https://f000.backblazeb2.com/file/malaya-speech-model/data/trainset-audiobook.tar.gz

7.  https://f000.backblazeb2.com/file/malaya-speech-model/data/salina-supervised-sani.tar.gz

  - Originally from https://nusantaraudiobooks.com/books/salina
  - Supervised by https://github.com/khursani8
  - approximate 19.32 hours.
  - Put commas and apply true case, [comma-salina-sani.json](comma-salina-sani.json), notebook [alignment-salina-sani.ipynb](alignment-salina-sani.ipynb).

8. https://f000.backblazeb2.com/file/malaya-speech-model/data/dari-pasentran-ke-istana-supervised-sani.tar.gz

  - Originally from https://nusantaraudiobooks.com/books/dari-pesantren-ke-istana-biografi-presiden-ke-4-indonesia-kiai-haji-abdurrahman-wahid
  - Supervised by https://github.com/khursani8
  - approximate 13.84 hours.
  - Put commas and apply true case, [comma-dari-pasentran-ke-istana-sani.json](comma-dari-pasentran-ke-istana-sani.json), notebook [alignment-dari-pasentran-ke-istana-sani.ipynb](alignment-dari-pasentran-ke-istana-sani.ipynb).

## Citation

```bibtex
@misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Semisupervised Speech Recognition from Audiobook,
  author = {Husein, Zolkepli},
  title = {Malay-Dataset},
  year = {2018},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/huseinzol05/malaya-speech/tree/master/data/semisupervised-audiobook}}
}
```