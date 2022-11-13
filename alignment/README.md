# Alignment

Purpose of this dataset to do word alignment, example,

```text
a black cat
kucing hitam

-> 1-1 2-0
```

## how-to

Or you can skip the steps and download the priors.

1. Install eflomal

```bash
git clone https://github.com/robertostling/eflomal.git
cd eflomal
make
make install -e INSTALLDIR=~/bin
python3 setup.py install --user
```

2. Install fast_align,

```bash
git clone https://github.com/clab/fast_align.git
cd fast_align
mkdir build
cd build
cmake ..
make
```

## download

1. align.priors EN-MS, https://f000.backblazeb2.com/file/malay-dataset/alignment/align.priors
