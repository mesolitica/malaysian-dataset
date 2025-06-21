
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
python3 generate.py \
--file "response-sample-v2.parquet" \
--folder "response-husein-v3" \
--reference_audio "husein-assistant.mp3" \
--reference_text "Uhm, hello, selamat pagi ye, saya dari customer service, boleh saya bantu you dengan apa apa ke?" \
--batch_size 6
```

```bash
python3 generate.py \
--file "en_chatbot.parquet" \
--folder "en_chatbot-husein-v2" \
--reference_audio "husein-assistant.mp3" \
--reference_text "Uhm, hello, selamat pagi ye, saya dari customer service, boleh saya bantu you dengan apa apa ke?" \
--batch_size 6
```

```bash
python3 generate.py \
--file "en_politics_chatbot.parquet" \
--folder "en_chatbot_politics-husein-v2" \
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
python3 generate.py \
--file "response-sample-v2.parquet" \
--folder "response-idayu-v2" \
--reference_audio "shafiqah-idayu-enhanced-v2-v2-trim.mp3" \
--reference_text "Hi, saya adalah pembantu AI anda, selamat berkenalan. Apa yang saya boleh tolong untuk buatkan hari anda lebih ceria." \
--batch_size 6
```

```bash
python3 generate.py \
--file "en_chatbot.parquet" \
--folder "en_chatbot-idayu" \
--reference_audio "shafiqah-idayu-enhanced-v2-v2-trim.mp3" \
--reference_text "Hi, saya adalah pembantu AI anda, selamat berkenalan. Apa yang saya boleh tolong untuk buatkan hari anda lebih ceria." \
--batch_size 6
```

```bash
python3 generate.py \
--file "en_politics_chatbot.parquet" \
--folder "en_politics_chatbot-idayu" \
--reference_audio "shafiqah-idayu-enhanced-v2-v2-trim.mp3" \
--reference_text "Hi, saya adalah pembantu AI anda, selamat berkenalan. Apa yang saya boleh tolong untuk buatkan hari anda lebih ceria." \
--batch_size 6
```

## Convert to UniCodec

```bash
python3 convert_unicodec.py --file "postfilter-idayu.parquet" --folder="postfilter-idayu"
```