## how-to

download at https://f000.backblazeb2.com/file/malay-dataset/nlq/cosql-translated.zip

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