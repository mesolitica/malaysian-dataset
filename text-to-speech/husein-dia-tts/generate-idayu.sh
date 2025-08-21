while true; do PENALTY_EOS="false" python3 generate.py \
--file "introduction-sample-v2.parquet" \
--folder "introduction-idayu-v2" \
--reference_audio "shafiqah-idayu-enhanced-v2-v2-trim.mp3" \
--reference_text "Hi, saya adalah pembantu AI anda, selamat berkenalan. Apa yang saya boleh tolong untuk buatkan hari anda lebih ceria." \
--batch_size 6; done

while true; do PENALTY_EOS="false" python3 generate_dia.py \
--file "synthetic-text.parquet" \
--folder "synthetic-text-idayu" \
--reference_audio "shafiqah-idayu-enhanced-v2-v2-trim.mp3" \
--reference_text "Hi, saya adalah pembantu AI anda, selamat berkenalan. Apa yang saya boleh tolong untuk buatkan hari anda lebih ceria." \
--batch_size 6; done

while true; do PENALTY_EOS="false" python3 generate_dia.py \
--file "normalized-text.parquet" \
--folder "normalized-text-idayu" \
--reference_audio "shafiqah-idayu-enhanced-v2-v2-trim.mp3" \
--reference_text "Hi, saya adalah pembantu AI anda, selamat berkenalan. Apa yang saya boleh tolong untuk buatkan hari anda lebih ceria." \
--batch_size 6; done

while true; do PENALTY_EOS="false" python3 generate.py \
--file "normalized.parquet" \
--folder "shafiqah-idayu-normalized" \
--reference_audio "shafiqah-idayu-enhanced-v2-v2-trim.mp3" \
--reference_text "Hi, saya adalah pembantu AI anda, selamat berkenalan. Apa yang saya boleh tolong untuk buatkan hari anda lebih ceria." \
--batch_size 4 --replication 5; done