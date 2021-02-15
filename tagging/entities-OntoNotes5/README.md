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

## Download translated Ontonotes

https://f000.backblazeb2.com/file/malay-dataset/tagging/ontonotes5/translated-ontonotes5.json

## Processed Ontonotes

train set, https://f000.backblazeb2.com/file/malay-dataset/tagging/ontonotes5/processed-train-ontonotes5.json

test set, https://f000.backblazeb2.com/file/malay-dataset/tagging/ontonotes5/processed-test-ontonotes5.json

## Augmented

Prefix, https://f000.backblazeb2.com/file/malay-dataset/tagging/ontonotes5/

1. augmentation-address-ontonotes5.json
2. augmentation-event-ontonotes5.json
3. augmentation-fac-ontonotes5.json
4. augmentation-gpe-ontonotes5.json
5. augmentation-language-ontonotes5.json
6. augmentation-law-ontonotes5.json
7. augmentation-loc-ontonotes5.json
8. augmentation-norp-ontonotes5.json
9. augmentation-org-ontonotes5.json
10. augmentation-person-ontonotes5.json
11. augmentation-product-ontonotes5.json
12. augmentation-work-of-art-ontonotes5.json

Train test set, ontonotes5-train-test.json
