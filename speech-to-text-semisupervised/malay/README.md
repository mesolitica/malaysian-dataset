# Malay

## how-to

1. Download Malay youtube videos, [download-videos.ipynb](download-videos.ipynb).

2. Run semisupervised using Google Speech, [semisupervised-googlespeech.py](semisupervised-googlespeech.py).

3. Run [transcribe.ipynb](transcribe.ipynb) to correct output from googlespeech.

```
All the videos, songs, images, and graphics used in the video belong to their respective owners and I does not claim any right over them.

Copyright Disclaimer under section 107 of the Copyright Act of 1976, allowance is made for "fair use" for purposes such as criticism, comment, news reporting, teaching, scholarship, education and research. Fair use is a use permitted by copyright statute that might otherwise be infringing.
```

## Download

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


## Download supervised

1. [label-semisupervised-malay.tar.gz](label-semisupervised-malay.tar.gz)

  - 16000 sample rate.
  - random length between 2 - 20 seconds, windowed using google VAD.
  - 768 over 57895 done, approximate 1.3 hours.

## Citation

```bibtex
@misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Semisupervised Speech Recognition from Malay Youtube Videos,
  author = {Husein, Zolkepli},
  title = {Malay-Dataset},
  year = {2018},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/huseinzol05/malaya-speech/tree/master/data/semisupervised-malay}}
}
```