<p align="center">
    <a href="#readme">
        <img alt="logo" width="80%" src="karangan-sekolah/wordcloud.png">
    </a>
</p>
<p align="center">
  <a href="https://github.com/huseinzol05/Malaya-Dataset/blob/master/LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
</p>

---

**Malaya-Dataset**, We gather Bahasa Malaysia corpus! This repository to store corpus for [Malaya](https://github.com/huseinzol05/Malaya). We will keep update this repository overtime.

## How we gather these corpus?

1. For news, articles and subtitles, we use crawler, you can get the code from here, [Malaya/crawler](https://github.com/huseinzol05/Malaya/tree/master/crawl)
2. For Bahasa, mostly we use Google Translator, you can get the code from here, [Malaya/translator](https://github.com/huseinzol05/Malaya/tree/master/translator)
3. Using social media, I catch most of live data from Twitter, Facebook and Instagram using crawlers, So I just search using Elasticsearch query.

## Table of contents
  * [Corpus](https://github.com/huseinzol05/Malaya-Dataset#corpus)
    * [200k English-Malay](https://github.com/huseinzol05/Malaya-Dataset#200k-english-malay)
    * [90k synonym](https://github.com/huseinzol05/Malaya-Dataset#90k-synonym)
    * [English-Malay translation](https://github.com/huseinzol05/Malaya-Dataset#english-malay-translation)
    * [Articles](https://github.com/huseinzol05/Malaya-Dataset#articles)
    * [Audience Nationality](https://github.com/huseinzol05/Malaya-Dataset#audience-nationality)
    * [Dependency](https://github.com/huseinzol05/Malaya-Dataset#dependency)
    * [Dictionary, 24550 unique words](https://github.com/huseinzol05/Malaya-Dataset#dictionary-24550-unique-words)
    * [Emotion](https://github.com/huseinzol05/Malaya-Dataset#emotion)
    * [Entities](https://github.com/huseinzol05/Malaya-Dataset#entities-json)
    * [Fake News](https://github.com/huseinzol05/Malaya-Dataset#fake-news)
    * [Gender](https://github.com/huseinzol05/Malaya-Dataset#gender)
    * [Insincere question](https://github.com/huseinzol05/Malaya-Dataset#insincere-question)
    * [Irony](https://github.com/huseinzol05/Malaya-Dataset#irony)
    * [Karangan sekolah](https://github.com/huseinzol05/Malaya-Dataset#karangan-sekolah)
    * [Language Detection, Wikipedia](https://github.com/huseinzol05/Malaya-Dataset#language-detection-wikipedia)
    * [News, crawled](https://github.com/huseinzol05/Malaya-Dataset#news-crawled)
    * [Normalize](https://github.com/huseinzol05/Malaya-Dataset#normalize)
    * [sentiment News](https://github.com/huseinzol05/Malaya-Dataset#sentiment-news)
    * [sentiment Twitter](https://github.com/huseinzol05/Malaya-Dataset#sentiment-twitter)
    * [sentiment Multidomain](https://github.com/huseinzol05/Malaya-Dataset#sentiment-multidomain)
    * [Part of Speech](https://github.com/huseinzol05/Malaya-Dataset#part-of-speech)
    * [Polarity](https://github.com/huseinzol05/Malaya-Dataset#polarity)
    * [Political landscape](https://github.com/huseinzol05/Malaya-Dataset#political-landscape)
    * [Question-Answer](https://github.com/huseinzol05/Malaya-Dataset#question-answer)
    * [Sarcastic news-headline](https://github.com/huseinzol05/Malaya-Dataset#sarcastic-news-headline)
    * [Stemmer](https://github.com/huseinzol05/Malaya-Dataset#stemmer)
    * [Subjectivity](https://github.com/huseinzol05/Malaya-Dataset#subjectivity)
    * [Toxicity](https://github.com/huseinzol05/Malaya-Dataset#toxicity)
    * [Subtitle](https://github.com/huseinzol05/Malaya-Dataset#subtitle)
  * [Suggestion](https://github.com/huseinzol05/Malaya-Dataset#suggestion)
  * [Citation](https://github.com/huseinzol05/Malaya-Dataset#citation)
  * [Donation](https://github.com/huseinzol05/Malaya-Dataset#donation)

## Corpus

#### [200K English-Malay](200k-english-malay)

Total size: 6.9 MB

#### [90k synonym](synonym)

Total size: 4.7 MB

#### [English-Malay translation](english-malay)

Total size: 91.2 MB

#### [Articles](articles)

Total size: 3.1 MB

1. Filem
2. Kerajaan
3. Pembelajaran
4. Pendidikan
5. Sekolah

#### [Audience Nationality](audience)

Total size: 246 KB

1. constituency
2. national

#### [Dependency](dependency)

Total size: 24.1 MB

#### [Dictionary, 24550 unique words](dictionary)

Total size: 428 KB

#### [Emotion](emotion)

Total size: 8.5 MB

1. Anger
2. Fear
3. Joy
4. Love
5. Sadness
6. Surprise

#### [Entities, JSON](entities)

Total size: 1.1 MB

1. OTHER - Other
2. law - law, regulation, related law documents, documents, etc
3. location - location, place
4. organization - organization, company, government, facilities, etc
5. person - person, group of people, believes, etc
6. quantity - numbers, quantity
7. time - date, day, time, etc
8. event - unique event happened, etc

#### [Fake News](fake-news)

Total size: 68.2 MB

1. Negative
2. Positive

#### [Gender](gender)

Total size: 2.2 MB

1. Unknown
2. Male
3. Female
4. Brand

#### [Insincere question](insincere-question)

Total size: 60.4 MB

1. Negative
2. Positive

#### [Irony](irony)

Total size: 465 KB

1. Positive
2. Negative

#### [Karangan sekolah](karangan-sekolah)

Total size: 221 KB

#### [Language-detection, Wikipedia](language-detection)

Total size: 26.2 MB
```python
(array(['OTHER', 'ara', 'ber', 'bul', 'ces', 'cmn', 'dan', 'deu', 'ell',
        'eng', 'epo', 'fin', 'fra', 'heb', 'hun', 'ind', 'ita', 'jpn',
        'kor', 'lat', 'lit', 'mar', 'mkd', 'nld', 'pol', 'por', 'rus',
        'spa', 'srp', 'swe', 'toki', 'tur', 'ukr', 'zlm'], dtype='<U5'),
 array([37910, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000,
        50000, 10000, 10000, 10000, 10000, 10000, 57327, 10000, 10000,
         3687, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000,
        10000, 10000, 10000, 10000, 10000, 10000, 53692]))
```

#### [News, crawled](news)

Total size: 16.6 MB

<details><summary>Complete list (117 news)</summary>

1. astro awani
2. bahasa pengaturcaraan
3. berjaya group
4. bisnes malaysia
5. bumiputera
6. cuti sekolah
7. ekonomi
8. felda
9. gaya hidup
10. harga tiket
11. isu 1mdb
12. isu agama
13. isu agong
14. isu agrikultur
15. isu air
16. isu airasia
17. isu ambank
18. isu anwar ibrahim
19. isu artis
20. isu astro
21. isu axiata
22. isu bahasa melayu
23. isu barisan nasional
24. isu bisnes
25. isu celcom
26. isu cikgu
27. isu cimb
28. isu cukai
29. isu cyberjaya
30. isu dadah
31. isu dahmakan
32. isu dunia
33. isu grab
34. isu gst
35. isu harakah
36. isu harga
37. isu icerd
38. isu imigren
39. isu kahwin
40. isu kapitalis
41. isu kerajaan
42. isu kesihatan
43. isu kuala lumpur
44. isu lgbt
45. isu mahathir
46. isu makanan
47. isu malaysia airlines
48. isu malaysia
49. isu maxis
50. isu minyak
51. isu najib razak
52. isu pas
53. isu pelajar
54. isu pelakon
55. isu pembangkang
56. isu perkauman
57. isu permainan
58. isu pertanian
59. isu pkr
60. isu politik
61. isu rosmah
62. isu sabah
63. isu sarawak
64. isu sekolah
65. isu selangor
66. isu semasa
67. isu singapore
68. isu sosial media
69. isu spotify
70. isu sukan
71. isu sultan melayu
72. isu tanah
73. isu teknologi
74. isu terkini
75. isu tm
76. isu ubat
77. isu umno
78. isu universiti
79. isu wan azizah
80. johor corporation
81. johor
82. kaum cina
83. kaum india
84. kelantan
85. kes remaja
86. kes rogol
87. kesihatan
88. khazanah nasional
89. kolej
90. kotak undi
91. lompat parti
92. malaysia airlines
93. melaka
94. modenas
95. mydin
96. negeri sembilan
97. orang asli
98. parti amanah
99. peluang pekerjaan
100. pengedar dadah
101. perkahwinan
102. perlis
103. perodua
104. petronas
105. pos laju
106. produk berbahaya
107. sabah
108. sarawak
109. selangor
110. sukan malaysia
111. sunway group
112. tabung haji
113. tadika
114. teknologi malaysia
115. tenaga nasional
116. terengganu
117. universiti

</details>

#### [Normalize](normalize)

Total size: 2.6 MB

#### [Sentiment News](news-sentiment)

Total size: 496 KB

1. Positive
2. Negative

#### [Sentiment Twitter](twitter-sentiment)

Total size: 50.6 MB

1. Positive
2. Negative

#### [Sentiment Multidomain](multidomain-sentiment)

Total size: 159 KB

1. Amazon review, Positive and Negative
2. IMDB review, Positive and Negative
3. Yelp review, Positive and Negative

#### [Part-of-Speech](part-of-speech)

Total size: 3.1 MB

1. ADJ - Adjective, kata sifat
2. ADP - Adposition
3. ADV - Adverb, kata keterangan
4. ADX - Auxiliary verb, kata kerja tambahan
5. CCONJ - Coordinating conjuction, kata hubung
6. DET - Determiner, kata penentu
7. NOUN - Noun, kata nama
8. NUM - Number, nombor
9. PART - Particle
10. PRON - Pronoun, kata ganti
11. PROPN - Proper noun, kata ganti nama khas
12. SCONJ - Subordinating conjunction
13. SYM - Symbol
14. VERB - Verb, kata kerja
15. X - Other

#### [Polarity](polarity)

Total size: 1.3 MB

1. Positive
2. Negative

#### [Political landscape](political-landscape)

Total size: 2 MB

1. Kerajaan
2. Pembangkang

#### [Question-Answer](question-answer)

Total size: 2.5 MB

```
1 mary pergi ke taman. 2 mary pergi ke dapur. 3 husein kembali ke pejabat.
4 husein perjalanan ke lorong. 5 jeff kembali ke bilik tidur. 6 fred berpindah ke lorong.
7 husein berpindah ke bilik mandi. 8 jeff kembali ke taman. 9 jeff kembali ke dapur.
10 fred kembali ke taman. 11 mary mendapat bola sepak di sana. 12 mary menyerahkan bola sepak kepada jeff.
13 apa yang mary berikan kepada jeff? <> bola sepak <> 12.
14 husein kembali ke lorong. 15 jeff kembali ke bilik tidur. 16 apa yang mary berikan kepada jeff? <> bola sepak <> 12.
17 fred berpindah ke bilik mandi. 18 mary mengambil susu di sana. 19 apa yang mary berikan kepada jeff? <> bola sepak <> 12.
20 fred pergi ke dapur. 21 mary menyerahkan susu itu kepada fred. 22 siapa yang memberikan susu itu kepada fred? <> mary <> 21.
23 fred berpindah ke lorong. 24 jeff pergi ke pejabat. 25 siapa yang mary memberikan susu itu? <> fred <> 21
```

#### [Sarcastic news-headline](sarcastic-news-headline)

Total size: 1.78 MB

1. Positive
2. Negative

#### [Stemmer](stemmer)

Total size: 6.5 MB

1. News stemming
2. Wikipedia stemming

#### [Subjectivity](subjectivity)

Total size: 1.4 MB

1. Positive
2. Negative

#### [Toxicity](toxicity)

Total size: 70 MB

Toxicity is multilabel, prefer to use sigmoid based.

1. toxic
2. severe toxic
3. obscene
4. threat
5. insult
6. identity hate

#### [Subtitle](subtitle)

Total size: 1.5 MB

## Suggestion

1. Always apply text augmentation, like swapping based words using synonyms or thesaurus. We gathered some synonyms if you want to use it, [90k synonyms](synonym).
2. Malaya also provided interface for text augmentation using word2vec, [Malaya-text-augmentation](https://malaya.readthedocs.io/en/latest/Generator.html#text-augmentation)

## Citation

1. Please citate the repository if use these corpus.
2. Please at least email us first before distributing these data. Remember all these hard workings we want to give it for free.
3. What do you see just the data, but nobody can see how much we spent our cost to make it public.

## Donation

1. **Husein** really need money to stay survive, he is still a human. **7053174643, CIMB Click, Husein Zolkepli**
