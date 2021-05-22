# SParC

Original website, https://yale-lily.github.io/sparc

Original paper, https://arxiv.org/abs/1906.02285

## download

1. sparc-translated.zip, https://f000.backblazeb2.com/file/malay-dataset/nlq/sparc-translated.zip

## how-to

```python
# !wget https://f000.backblazeb2.com/file/malay-dataset/nlq/sparc-translated.zip
# !unzip sparc-translated.zip
import json

with open('sparc-translated/sparc.json.data') as fopen:
    data = json.load(fopen)
    
data[0]
```

```text
{'db_id': 'concert_singer',
 'query': 'SELECT count(*) FROM singer',
 'query_toks': ['SELECT', 'count', '(', '*', ')', 'FROM', 'singer'],
 'query_toks_no_value': ['select', 'count', '(', '*', ')', 'from', 'singer'],
 'question': 'How many singers do we have?',
 'question_toks': ['How', 'many', 'singers', 'do', 'we', 'have', '?'],
 'sql': {'except': None,
  'from': {'conds': [], 'table_units': [['table_unit', 1]]},
  'groupBy': [],
  'having': [],
  'intersect': None,
  'limit': None,
  'orderBy': [],
  'select': [False, [[3, [0, [0, 0, False], None]]]],
  'union': None,
  'where': []},
 'question_bahasa': 'Berapa banyak penyanyi yang kita ada?'}
```

## Citation

```bibtex
@article{DBLP:journals/corr/abs-1906-02285,
  author    = {Tao Yu and
               Rui Zhang and
               Michihiro Yasunaga and
               Yi Chern Tan and
               Xi Victoria Lin and
               Suyi Li and
               Heyang Er and
               Irene Li and
               Bo Pang and
               Tao Chen and
               Emily Ji and
               Shreya Dixit and
               David Proctor and
               Sungrok Shim and
               Jonathan Kraft and
               Vincent Zhang and
               Caiming Xiong and
               Richard Socher and
               Dragomir R. Radev},
  title     = {SParC: Cross-Domain Semantic Parsing in Context},
  journal   = {CoRR},
  volume    = {abs/1906.02285},
  year      = {2019},
  url       = {http://arxiv.org/abs/1906.02285},
  archivePrefix = {arXiv},
  eprint    = {1906.02285},
  timestamp = {Wed, 12 May 2021 16:44:19 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1906-02285.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```