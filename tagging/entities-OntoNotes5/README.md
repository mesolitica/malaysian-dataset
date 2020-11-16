## Description

```python
"""
Describe OntoNotes5 Entities supported. https://spacy.io/api/annotation#named-entities
"""
d = [
    {'Tag': 'PERSON', 'Description': 'People, including fictional.'},
    {
        'Tag': 'NORP',
        'Description': 'Nationalities or religious or political groups.',
    },
    {
        'Tag': 'FAC',
        'Description': 'Buildings, airports, highways, bridges, etc.',
    },
    {
        'Tag': 'ORG',
        'Description': 'Companies, agencies, institutions, etc.',
    },
    {'Tag': 'GPE', 'Description': 'Countries, cities, states.'},
    {
        'Tag': 'LOC',
        'Description': 'Non-GPE locations, mountain ranges, bodies of water.',
    },
    {
        'Tag': 'PRODUCT',
        'Description': 'Objects, vehicles, foods, etc. (Not services.)',
    },
    {
        'Tag': 'EVENT',
        'Description': 'Named hurricanes, battles, wars, sports events, etc.',
    },
    {'Tag': 'WORK_OF_ART', 'Description': 'Titles of books, songs, etc.'},
    {'Tag': 'LAW', 'Description': 'Named documents made into laws.'},
    {'Tag': 'LANGUAGE', 'Description': 'Any named language.'},
    {
        'Tag': 'DATE',
        'Description': 'Absolute or relative dates or periods.',
    },
    {'Tag': 'TIME', 'Description': 'Times smaller than a day.'},
    {'Tag': 'PERCENT', 'Description': 'Percentage, including "%".'},
    {'Tag': 'MONEY', 'Description': 'Monetary values, including unit.'},
    {
        'Tag': 'QUANTITY',
        'Description': 'Measurements, as of weight or distance.',
    },
    {'Tag': 'ORDINAL', 'Description': '"first", "second", etc.'},
    {
        'Tag': 'CARDINAL',
        'Description': 'Numerals that do not fall under another type.',
    },
]
```

## GPE-Guidelines

https://www.ling.upenn.edu/courses/Fall_2009/ling001/GPE_Guidelines.pdf