# CoSQL

Original website, https://yale-lily.github.io/cosql

Original paper, https://arxiv.org/abs/1909.05378

## download

1. cosql-translated.zip, https://f000.backblazeb2.com/file/malay-dataset/nlq/cosql-translated.zip

## how-to

```python
# !wget https://f000.backblazeb2.com/file/malay-dataset/nlq/cosql-translated.zip
# !unzip cosql-translated.zip
import json

with open('cosql-translated/cosql.json.data') as fopen:
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
@article{DBLP:journals/corr/abs-1909-05378,
  author    = {Tao Yu and
               Rui Zhang and
               Heyang Er and
               Suyi Li and
               Eric Xue and
               Bo Pang and
               Xi Victoria Lin and
               Yi Chern Tan and
               Tianze Shi and
               Zihan Li and
               Youxuan Jiang and
               Michihiro Yasunaga and
               Sungrok Shim and
               Tao Chen and
               Alexander R. Fabbri and
               Zifan Li and
               Luyao Chen and
               Yuwen Zhang and
               Shreya Dixit and
               Vincent Zhang and
               Caiming Xiong and
               Richard Socher and
               Walter S. Lasecki and
               Dragomir R. Radev},
  title     = {CoSQL: {A} Conversational Text-to-SQL Challenge Towards Cross-Domain
               Natural Language Interfaces to Databases},
  journal   = {CoRR},
  volume    = {abs/1909.05378},
  year      = {2019},
  url       = {http://arxiv.org/abs/1909.05378},
  archivePrefix = {arXiv},
  eprint    = {1909.05378},
  timestamp = {Wed, 12 May 2021 16:44:19 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1909-05378.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```