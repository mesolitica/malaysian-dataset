# Generate synthetic voice using F5-TTS

## how to

1. Run generate,

```bash
python3 generate.py \
--voice "anwar-ibrahim-enhanced-v2.wav" \
--original_text "Saya ingin nyatakan bahawa, cara menangani masalah ekonomi dalam krisis, tidak sama dalam keadaan biasa. Sebab itu soal defisit, soal hutang, soal termasuk monatarium." \
--text_file "news-berita-politik.json" \
--folder "anwar-news-politics-normalized-v2" \
--global_index 1 \
--index 0
```

- Voice you can get at [anwar-ibrahim-enhanced-v2.wav](https://huggingface.co/datasets/mesolitica/TTS/blob/main/anwar-ibrahim-enhanced-v2.wav).
- Text file you can get at [news-berita-politik.json](https://huggingface.co/datasets/mesolitica/TTS/resolve/main/texts/news-berita-politik.json).