# Alignment

Prepare alignment for MS-EN using [eflomal](https://github.com/robertostling/eflomal).

## Download

1. fwd, https://f000.backblazeb2.com/file/malay-dataset/ms-en-alignment/fwd
2. rev, https://f000.backblazeb2.com/file/malay-dataset/ms-en-alignment/rev
3. align.priors, https://f000.backblazeb2.com/file/malay-dataset/ms-en-alignment/align.priors

## how-to

1. Build https://github.com/robertostling/eflomal,

```bash
make
make INSTALLDIR=~/.local/bin install
python3 setup.py install --user
```

2. Align MS-EN text, [prepare-ms-en-fwd-rev.ipynb](prepare-ms-en-fwd-rev.ipynb).