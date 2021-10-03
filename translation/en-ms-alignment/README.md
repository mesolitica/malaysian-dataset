# Alignment

Prepare alignment for EN-MS using [eflomal](https://github.com/robertostling/eflomal).

## Download

1. EN, https://f000.backblazeb2.com/file/malay-dataset/translation/en-ms-alignment/EN
2. MS, https://f000.backblazeb2.com/file/malay-dataset/translation/en-ms-alignment/MS
3. fwd, https://f000.backblazeb2.com/file/malay-dataset/translation/en-ms-alignment/fwd
4. rev, https://f000.backblazeb2.com/file/malay-dataset/translation/en-ms-alignment/rev
5. align.priors, https://f000.backblazeb2.com/file/malay-dataset/translation/en-ms-alignment/align.priors

## how-to

1. Build https://github.com/robertostling/eflomal,

```bash
make
make INSTALLDIR=~/.local/bin install
python3 setup.py install --user
```

2. Align EN-MS text,

```bash
python3 test.py
```

## Citation

```bibtex
@misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Alignment EN-MS,
  author = {Husein, Zolkepli},
  title = {Malay-Dataset},
  year = {2018},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/huseinzol05/malay-dataset/tree/master/translation/english-news}}
}
```