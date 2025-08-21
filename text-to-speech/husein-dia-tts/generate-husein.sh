while true; do PENALTY_EOS="false" python3 generate.py \
--file "introduction-sample-v2.parquet" \
--folder "introduction-husein-v3" \
--reference_audio "husein-assistant.mp3" \
--reference_text "Uhm, hello, selamat pagi ye, saya dari customer service, boleh saya bantu you dengan apa apa ke?" \
--batch_size 6; done

while true; do PENALTY_EOS="false" python3 generate_dia.py \
--file "synthetic-text.parquet" \
--folder "synthetic-text-husein" \
--reference_audio "husein-assistant.mp3" \
--reference_text "Uhm, hello, selamat pagi ye, saya dari customer service, boleh saya bantu you dengan apa apa ke?" \
--batch_size 2; done

while true; do PENALTY_EOS="false" python3 generate_dia.py \
--file "normalized-text.parquet" \
--folder "normalized-text-husein" \
--reference_audio "husein-assistant.mp3" \
--reference_text "Uhm, hello, selamat pagi ye, saya dari customer service, boleh saya bantu you dengan apa apa ke?" \
--batch_size 6; done

while true; do PENALTY_EOS="false" python3 generate.py \
--file "normalized.parquet" \
--folder "husein-assistant-normalized" \
--reference_audio "husein-assistant.mp3" \
--reference_text "Uhm, hello, selamat pagi ye, saya dari customer service, boleh saya bantu you dengan apa apa ke?" \
--batch_size 4 --replication 5; done