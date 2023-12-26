nlq
===

CoSQL
-----

Original website, https://yale-lily.github.io/cosql

Original paper, https://arxiv.org/abs/1909.05378

download
~~~~~~~~

1. cosql-translated.zip, https://f000.backblazeb2.com/file/malay-dataset/nlq/cosql-translated.zip

how-to
~~~~~~

.. code:: python

   ## !wget https://f000.backblazeb2.com/file/malay-dataset/nlq/cosql-translated.zip
   ## !unzip cosql-translated.zip
   import json

   with open('cosql-translated/cosql.json.data') as fopen:
   data = json.load(fopen)

   data[0]

.. code:: text

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

Citation
~~~~~~~~

.. code:: bibtex

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

SParC
-----

Original website, https://yale-lily.github.io/sparc

Original paper, https://arxiv.org/abs/1906.02285

download
~~~~~~~~

1. sparc-translated.zip, https://f000.backblazeb2.com/file/malay-dataset/nlq/sparc-translated.zip

how-to
~~~~~~

.. code:: python

   ## !wget https://f000.backblazeb2.com/file/malay-dataset/nlq/sparc-translated.zip
   ## !unzip sparc-translated.zip
   import json

   with open('sparc-translated/sparc.json.data') as fopen:
   data = json.load(fopen)

   data[0]

.. code:: text

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

Citation
~~~~~~~~

.. code:: bibtex

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

Spider
------

Original website, https://github.com/taoyds/spider

Original paper, https://arxiv.org/abs/1809.08887

download
~~~~~~~~

download at https://f000.backblazeb2.com/file/malay-dataset/nlq/spider-translated.zip

.. code:: python

   ## !wget https://f000.backblazeb2.com/file/malay-dataset/nlq/spider-translated.zip
   ## !unzip spider-translated.zip
   import json

   with open('spider-translated/spider.json.data') as fopen:
   data = json.load(fopen)

   data[0]

.. code:: text

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

Citation
~~~~~~~~

.. code:: bibtex

   @inproceedings{Yu&al.18c,
   title     = {Spider: A Large-Scale Human-Labeled Dataset for Complex and Cross-Domain Semantic Parsing and Text-to-SQL Task},
   author    = {Tao Yu and Rui Zhang and Kai Yang and Michihiro Yasunaga and Dongxu Wang and Zifan Li and James Ma and Irene Li and Qingning Yao and Shanelle Roman and Zilin Zhang and Dragomir Radev}
   booktitle = "Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing",
   address   = "Brussels, Belgium",
   publisher = "Association for Computational Linguistics",
   year      = 2018
   }
