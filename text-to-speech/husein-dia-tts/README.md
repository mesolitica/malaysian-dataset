
# Synthetic Husein TTS using Dia TTS

## how to Husein

```bash
python3 generate.py \
--file "introduction-sample-v2.parquet" \
--folder "introduction-husein-v3" \
--reference_audio "husein-assistant.mp3" \
--reference_text "Uhm, hello, selamat pagi ye, saya dari customer service, boleh saya bantu you dengan apa apa ke?" \
--batch_size 6
```

```bash
python3.10 generate_dia.py \
--file "synthetic-text.parquet" \
--folder "synthetic-text-husein" \
--reference_audio "husein-assistant.mp3" \
--reference_text "Uhm, hello, selamat pagi ye, saya dari customer service, boleh saya bantu you dengan apa apa ke?" \
--batch_size 2
```

```bash
CUDA_VISIBLE_DEVICES="2" python3.10 generate_dia.py \
--file "normalized-text.parquet" \
--folder "normalized-text-husein" \
--reference_audio "husein-assistant.mp3" \
--reference_text "Uhm, hello, selamat pagi ye, saya dari customer service, boleh saya bantu you dengan apa apa ke?" \
--batch_size 6
```

## how to Idayu

```bash
python3 generate.py \
--file "introduction-sample-v2.parquet" \
--folder "introduction-idayu-v2" \
--reference_audio "shafiqah-idayu-enhanced-v2-v2-trim.mp3" \
--reference_text "Hi, saya adalah pembantu AI anda, selamat berkenalan. Apa yang saya boleh tolong untuk buatkan hari anda lebih ceria." \
--batch_size 6
```

```bash
CUDA_VISIBLE_DEVICES="1" python3.10 generate_dia.py \
--file "synthetic-text.parquet" \
--folder "synthetic-text-idayu" \
--reference_audio "shafiqah-idayu-enhanced-v2-v2-trim.mp3" \
--reference_text "Hi, saya adalah pembantu AI anda, selamat berkenalan. Apa yang saya boleh tolong untuk buatkan hari anda lebih ceria." \
--batch_size 6
```

```bash
python3.10 generate_dia.py \
--file "normalized-text.parquet" \
--folder "normalized-text-idayu" \
--reference_audio "shafiqah-idayu-enhanced-v2-v2-trim.mp3" \
--reference_text "Hi, saya adalah pembantu AI anda, selamat berkenalan. Apa yang saya boleh tolong untuk buatkan hari anda lebih ceria." \
--batch_size 6
```

## Convert to UniCodec

```bash
python3.10 convert_unicodec.py --file "postfilter-idayu.parquet" --folder="postfilter-idayu"
python3.10 convert_unicodec.py --file "postfilter-idayu-part2.parquet" --folder="postfilter-idayu-part2"
python3.10 convert_unicodec.py --file "postfilter-husein-part2.parquet" --folder="postfilter-husein-part2"
```

## Convert to DistilCodec

```bash
python3 convert_distilcodec.py --file "tts.parquet" --folder="distilcodec" --replication 25
python3 convert_distilcodec.py --file "chunk.parquet" --folder="distilcodec-chunk" --replication 25
```

## Calculate force alignment

```bash
python3.10 force_alignment.py --file "postfilter-idayu.parquet" --folder="postfilter-idayu-force-alignment"
CUDA_VISIBLE_DEVICES="2" python3.10 force_alignment.py --file "postfilter-husein.parquet" --folder="postfilter-husein-force-alignment"
```

```bash
python3.10 force_alignment_spelling.py --file "postfilter-idayu-part2.parquet" --folder="postfilter-idayu-part2-force-alignment"
python3.10 force_alignment_spelling.py --file "postfilter-husein-part2.parquet" --folder="postfilter-husein-part2-force-alignment"
```