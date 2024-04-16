# masabih.org

## download

https://huggingface.co/datasets/radenmuaz/masabih.org
https://huggingface.co/datasets/radenmuaz/masabih.org/blob/main/mishkat_al_masabih.jsonl


# scrape

Website uses js a to render html, so need to load with selenium Chrome (not headless), then use bs4.

```
python scrape_mishkat_al_masabih.py
```