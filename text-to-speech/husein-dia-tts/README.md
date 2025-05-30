# Synthetic Husein TTS using Dia TTS

## how to Husein

```bash
python3 generate.py \
--file "introduction-sample.parquet" \
--folder "introduction-husein" \
--reference_audio "husein-assistant.mp3" \
--reference_text "Uhm, hello, selamat pagi ye, saya dari customer service, boleh saya bantu you dengan apa apa ke?" \
--batch_size 6
```

## how to Idayu

```bash
python3 generate.py \
--file "introduction-sample.parquet" \
--folder "introduction-idayu" \
--reference_audio "shafiqah-idayu-enhanced-v2-v2-trim.mp3" \
--reference_text "Hi, saya adalah pembantu AI anda, selamat berkenalan. Apa yang saya boleh tolong untuk buatkan hari anda lebih ceria." \
--batch_size 6
```