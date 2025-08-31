
# Synthetic Husein TTS using Dia TTS

## how to Husein

```bash
bash generate-husein.sh
```

## how to Idayu

```bash
bash generate-idayu.sh
```

## Convert to UniCodec

```bash
python3 convert_unicodec.py --file "postfilter-idayu.parquet" --folder="postfilter-idayu"
```

## Convert to DistilCodec

```bash
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
python3 convert_distilcodec.py --file "tts.parquet" --folder="distilcodec" --replication 25

OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
python3 convert_distilcodec.py --file "stage2.parquet" --folder="stage2" --replication 15
```

## Calculate force alignment

```bash
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
python3 force_alignment.py --file "postfilter-idayu.parquet" --folder="postfilter-idayu-force-alignment"

OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
python3 force_alignment_spelling.py --file "husein.parquet" --folder="force-alignment-husein"

OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
python3 force_alignment_spelling.py --file "hard.parquet" --folder="force-alignment-hard" --replication 20
```