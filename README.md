<p align="center">
    <a href="#readme">
        <img alt="logo" width="80%" src="karangan-sekolah/wordcloud.png">
    </a>
</p>
<p align="center">
  <a href="https://github.com/huseinzol05/Malaya-Dataset/blob/master/LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
</p>

---

**Malaya-Dataset**, We gather Bahasa Malaysia corpus! This repository to store corpus for [Malaya](https://github.com/huseinzol05/Malaya) and [Bahasa-NLP-Tensorflow](https://github.com/huseinzol05/Bahasa-NLP-Tensorflow). We will keep update this repository overtime.

## How we gather these corpus?

1. For news, articles and subtitles, we use crawler, you can get the code from here, [Malaya/crawler](https://github.com/huseinzol05/Malaya/tree/master/crawl)
2. For Bahasa, mostly we use Google Translator, you can get the code from here, [Malaya/translator](https://github.com/huseinzol05/Malaya/tree/master/translator)
3. Using social media, I catch most of live data from Twitter, Facebook and Instagram using crawlers, So I just search using Elasticsearch query.
4. For speech, we recorded using wired microphone attached to Macbook Air.

## Table of contents
  * [Corpus](https://github.com/huseinzol05/Malaya-Dataset#corpus)
    * [200k English-Malay](https://github.com/huseinzol05/Malaya-Dataset#200k-english-malay)
    * [90k synonym](https://github.com/huseinzol05/Malaya-Dataset#90k-synonym)
    * [English-Malay translation](https://github.com/huseinzol05/Malaya-Dataset#english-malay-translation)
    * [Ngrams](https://github.com/huseinzol05/Malaya-Dataset#ngrams)
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
    * [Malaysia Entities](https://github.com/huseinzol05/Malaya-Dataset#malaysia-entities)
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
    * [Speech](https://github.com/huseinzol05/Malaya-Dataset#speech)
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

#### [Ngrams](ngram)

Unigram and Bigram collected from news, structure,
```python
{'saya': 1000}
```

Total size: 92 MB

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

Total size: 41.2 MB

1. Anger
2. Fear
3. Joy
4. Love
5. Sadness
6. Surprise

#### [Entities, JSON](entities)

Total size: 5.2 MB

1. OTHER - Other
2. law - law, regulation, related law documents, documents, etc
3. location - location, place
4. organization - organization, company, government, facilities, etc
5. person - person, group of people, believes, etc
6. quantity - numbers, quantity
7. time - date, day, time, etc
8. event - unique event happened, etc

#### [Fake News](fake-news)

Total size: 122.2 MB

1. Negative
2. Positive

Malaysia fake news, contributed by [syazanihussin](https://github.com/syazanihussin/FLUX/tree/master/data)

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

#### [Malaysia-entities](malaysia-entities)

Social media texts related to Malaysia entities.

Total size: 190.1 MB

<details><summary>Complete list (210 entities)</summary>

1. mahathir
2. anwar ibrahim
3. najib razak
4. pakatan harapan
5. syed saddiq
6. parti keadilan rakyat
7. umno
8. barisan nasional
9. parti islam semalaysia
10. nurul izzah
11. tunku ismail idris
12. mca
13. democratic action party
14. parti amanah
15. ppbm
16. mic
17. tun daim zainuddin
18. datuk seri abdul hadi awang
19. majlis pakatan harapan
20. wan azizah
21. parti pribumi bersatu malaysia
22. datuk seri azmin ali
23. datuk johari abdul
24. tengku razaleigh hamzah
25. tan sri dr rais yatim
26. rafizi ramli
27. bersatu
28. bernama
29. donald trump
30. perkasa
31. tan sri mokhzani mahathir
32. rais yatim
33. anthony loke siew fook
34. rosmah mansur
35. arul kanda
36. zeti aziz
37. robert kuok
38. hassan merican
39. ks jomo
40. jho low
41. kadir jasin
42. zakir naik
43. bung mokhtar
44. shafie apdal
45. ariff md yusof
46. felda
47. dato vida
48. jabatan perancangan bandar desa
49. jabatan perdana menteri malaysia
50. kementerian kewangan malaysia
51. kementerian dalam negeri malaysia
52. kementerian perdagangan dalam negeri hal ehwal pengguna malaysia
53. kementerian luar negeri malaysia
54. kementerian pertahanan malaysia
55. kementerian pendidikan malaysia
56. kementerian pembangunan luar bandar
57. kementerian kerja raya malaysia
58. kementerian kesihatan malaysia
59. kementerian komunikasi multimedia malaysia
60. kementerian perumahan kerajaan tempatan malaysia
61. kementerian pelancongan kebudayaan malaysia
62. kementerian pengangkutan malaysia
63. kementerian pembangunan wanita keluarga masyarakat malaysia
64. kementerian pertanian industri asas tani
65. kementerian perusahaan perladangan komoditi
66. kementerian perdagangan antarabangsa industri
67. kementerian sains teknologi inovasi malaysia
68. kementerian sumber manusia malaysia
69. kementerian sumber asli alam sekitar malaysia
70. kementerian wilayah persekutuan malaysia
71. kementerian tenaga teknologi hijau air malaysia
72. jabatan perkhidmatan awam malaysia
73. jabatan kemajuan islam (jakim) department of islamic development
74. jabatan parlimen malaysia
75. agensi kelayakan malaysia
76. agensi penguatkuasaan maritim malaysia
77. bahagian istiadat urusetia persidangan antarabangsa
78. bahagian hal ehwal undang-undang
79. bahagian kabinet perlembangan perhubungan antara kerajaan
80. bahagian kemajuan wilayah persekutuan perancangan lembah klang
81. bahagian keselamatan negara
82. bahagian pengurusan hartanah
83. bahagian pengurusan perkhidmatan sumber manusia
84. bahagian penyelidikan
85. biro bantuan guaman
86. biro pengaduan awam
87. biro tatanegara
88. istana negara
89. institut kefahaman islam malaysia
90. institut latihan kehakiman perundangan
91. pejabat ketua setiausaha negara
92. pejabat perdana menteri
93. jabatan peguam negara
94. majlis agama islam wilayah persekutuan
95. masjid negara
96. pejabat ketua pegawai keselamatan kerajaan malaysia
97. pejabat setiausaha persekutuan sabah
98. perpustakaan kuala lumpur
99. pejabat setiausaha persekutuan sarawak
100. lembaga tabung haji
101. penasihat sains
102. jabatan audit negara malaysia
103. jabatan pertahanan awam malaysia
104. suruhanjaya pengankutan awam darat
105. perbendaharaan malaysia
106. majlis tindakan ekonomik negara
107. jabatan perangkaan (jp) department of statistics
108. polis diraja malaysia
109. ikatan relawan rakyat malaysia
110. jabatan penjara malaysia
111. jabatan pendaftaran negara malaysia
112. lembaga penapisan filem
113. jabatan imigresen malaysia
114. suruhanjaya syarikat malaysia
115. suruhanjaya koperasi malaysia
116. perbadanan harta intelek malaysia
117. bank kerjasama rakyat malaysia
118. perbadanan nasional berhad
119. maktab koperasi malaysia
120. suruhanjaya persaingan malaysia
121. institut diplomasi hal ehwal luar negeri
122. angkatan tentera malaysia
123. tentera darat malaysia
124. tentera udara diraja malaysia
125. tentera laut diraja malaysia
126. program latihan khidmat negara
127. dewan bahasa pustaka
128. institut pendidikan guru malaysia
129. perbadanan tabung pendidikan tinggi nasional
130. institut terjemahan negara malaysia
131. kejora
132. felcra
133. risda
134. jabatan kerja raya malaysia
135. lembaga lebuhraya malaysia
136. lembaga jurutera malaysia
137. lembaga pembangunan industri pembinaan
138. institut jantung negara
139. klinik 1malaysia
140. insitut kanser negara
141. radio televisyen malaysia
142. suruhanjaya komunikasi multimedia malaysia
143. jabatan penerangan malaysia
144. jabatan perancangan bandar desa semenanjung malaysia
145. jabatan bomba penyelamat malaysia
146. jabatan perumahan negara
147. jabatan kerajaan tempatan
148. jabatan landskap negara
149. jabatan pengurusan sisa pepejal negara
150. tribunal perumahan pengurusan strata
151. perbadanan pengurusan sisa pepejal pembersihan awam
152. jabatan pelancongan malaysia
153. jabatan pengangkutan jalan
154. jabatan penerbangan awam
155. lembaga pelabuhan klang
156. jabatan laut malaysia
157. jabatan keselamatan jalan raya
158. lembaga pelabuhan kuantan
159. lembaga pelabuhan johor
160. lembaga pelabuhan pulau pinang
161. jabatan kebajikan masyarakat malaysia
162. institut penyelidikan kemajuan pertanian malaysia
163. lembaga kemajuan ikan malaysia
164. lembaga pemasaran pertanian persekutuan
165. jabatan pertanian malaysia
166. lembaga pertubuhan peladang
167. lembaga kemajuan pertanian kemubu
168. lembaga kemajuan pertanian muda
169. jabatan perikanan
170. jabatan perkhidmatan veterinar
171. lembaga perindustrian nanas malaysia
172. tabung ekonomi kumpulan usaha niaga
173. bank pertanian
174. lembaga minyak sawit malaysia
175. lembaga pembangunan pelaburan malaysia
176. agensi nuklear malaysia
177. institut penyelidikan teknologi nuklear malaysia
178. pusat sains negara
179. jabatan kimia malaysia
180. jabatan meteorologi malaysia
181. jabatan perkhidmatan awam
182. institut tadbiran awam negara
183. jabatan agama islam wilayah persekutuan
184. jabatan tenaga kerja semenanjung malaysia
185. jabatan alam sekitar
186. jabatan pengairan saliran
187. jabatan tanah galian wilayah persekutuan
188. jabatan perlindungan hidupan liar taman negara
189. dewan bandaraya kuala lumpur
190. perbadanan putrajaya
191. perbadanan labuan
192. jabatan bekalan air
193. jabatan perkhidmatan pembetungan
194. suruhanjaya tenaga
195. suruhanjaya perkhidmatan air negara
196. malaysian green technology corporation
197. yayasan hijau malaysia
198. mahkamah persekutuan
199. mahkamah syariah wilayah persekutuan
200. suruhanjaya perdagangan komoditi
201. suruhanjaya perkhidmatan awam
202. suruhanjaya perkhidmatan pendidikan
203. suruhanjaya pilihan raya
204. suruhanjaya pencegahan rasuah malaysia
205. tribunal perkhidmatan awam
206. unit khas teknologi tinggi
207. unit pemodenan tadbiran perancangan pengurusan malaysia
208. unit perancang ekonomi
209. unit penyelarasan pelaksanaan
210. urusetia persidangan antarabangsa protokol

</details>

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

#### [Speech](speech)

Total size: 276 MB

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

1. **Husein** really need money to stay survive, he is still a human. **7053174643, CIMB Bank, Husein Zolkepli**
