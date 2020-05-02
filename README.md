<p align="center">
    <a href="#readme">
        <img alt="logo" width="50%" src="wordcloud.png">
    </a>
</p>
<p align="center">
  <a href="https://github.com/huseinzol05/Malaya-Dataset/blob/master/LICENSE"><img alt="Apache License 2.0" src="https://img.shields.io/badge/License-Apache--2.0-yellow.svg"></a>
</p>

---

**Malaya-Dataset**, We gather Bahasa Malaysia corpus! This repository to store corpus for [Malaya](https://github.com/huseinzol05/Malaya) and [Bahasa-NLP-Tensorflow](https://github.com/huseinzol05/Bahasa-NLP-Tensorflow). We will keep update this repository overtime.

## How we gather these corpus?

1. For news, articles and subtitles, we use crawler, you can get the code from here, [Malaya/crawler](https://github.com/huseinzol05/Malaya/tree/master/crawl)
2. For Bahasa, mostly we use Google Translator, you can get the code from here, [Malaya/translator](https://github.com/huseinzol05/Malaya/tree/master/translator)
3. Using social media, we catch most of live data from Twitter, Facebook and Instagram using crawlers, So we just search using Elasticsearch query.
4. For speech, we recorded using wired microphone attached to Macbook Air 2013 while read some random texts from bahasa wikipedia.
5. We pay some linguists.
6. Lexicon -> weak learning from translated -> confident learning -> 5 iterations from humans.

## Acknowledgement

Thanks to [Im Big](https://www.facebook.com/imbigofficial/), [LigBlou](https://www.facebook.com/ligblou), [Mesolitica](https://mesolitica.com/) and [KeyReply](https://www.keyreply.com/) for sponsoring AWS Google and private cloud to deploy distributed crawlers.

<img alt="logo" width="50%" src="https://malaya-dataset.s3-ap-southeast-1.amazonaws.com/ligblou-mesolitca-keyreply.png">

## Table of contents
  * [Dictionary](#dictionary)
    * [73k English-Malay](#73k-english-malay)
    * [200k English-Malay](#200k-english-malay)
    * [90k synonym](#90k-synonym)
    * [Dictionary, 24550 unique words](#dictionary-24550-unique-words)
    * [Dialect](#dialect)
    * [Ngrams](#ngrams)
  * [Lexicon](#lexicon)
    * [Sentiment](#sentiment)
    * [Emotion](#emotion)
  * [Tagging](#tagging)
    * [Dependency](#dependency)
    * [Part-of-Speech](#part-of-speech)
    * [Entities](#entities-json)
  * [Sentiment](#sentiment-1)
    * [Local News](#local-news)
    * [Twitter](#twitter)
    * [Translated Twitter](#Translated-Twitter)
    * [Translated Multidomain](#Translated-Multidomain)
    * [Translated Polarity](#Translated-Polarity)
  * [Corpus](#corpus)
    * [Audience Nationality](#audience-nationality)
    * [Translated Emotion](#Translated-Emotion)
    * [Twitter Emotion](#Twitter-Emotion)
    * [Gender](#gender)
    * [Insincere question](#insincere-question)
    * [Irony](#irony)
    * [Language Detection](#language-detection)
    * [Malaysia Entities](#malaysia-entities)
    * [Malaysia Topics](#malaysia-topics)
    * [Political landscape](#political-landscape)
    * [Sarcastic news-headline](#sarcastic-news-headline)
    * [Subjectivity](#subjectivity)
    * [Toxicity-small](#toxicity-small)
    * [Toxicity-large](#toxicity-large)
  * [News](#news)
    * [Fake News](#fake-news)
    * [Crawled News](#crawled-news)
    * [30k News](#30k-news)
    * [Articles](#articles)
    * [CNN](#cnn-news)
  * [Speech](#speech)
    * [Tolong sebut](#tolong-sebut)
    * [Wikipedia](#wikipedia)
    * [Manglish](#manglish)
  * [Optical Character Recognition](#optical-character-recognition)
    * [Malay-to-Jawi](#malay-to-jawi)
    * [Malay handwriting (Satisfy-Regular)](#malay-handwriting-satisfy-regular)
  * [English-Malay translation](#english-malay-translation)
  * [Question-Answer](#question-answer)
    * [General](#general)
    * [SQUAD](#squad)
  * [Normalization](#normalization)
    * [Normalize](#normalize)
    * [Stemmer](#stemmer)
  * [Text-similarity](#text-similarity)
    * [Quora](#quora)
    * [SNLI](#snli)
  * [Dumping](#dumping)
    * [Karangan sekolah](#karangan-sekolah)
    * [Wikipedia](#wikipedia-1)
    * [Instagram](#instagram)
    * [Twitter](#twitter-1)
    * [Public news](#public-news)
    * [Parliament](#parliament)
    * [Singlish text](#singlish-text)
    * [Singapore news](#singapore-news)
    * [Subtitle](#subtitle)
  * [Crawl](#crawl)
    * [Foodpanda](#foodpanda)
    * [Klook](#klook)
    * [IIUM-Confession](#iium-confession)
    * [Wattpad](#wattpad)
    * [Academia PDF](#academia-pdf)
    * [ticket2u](#ticket2u)
  * [Suggestion](#suggestion)
  * [Citation](#citation)
  * [Donation](#donation)

## [Dictionary](dictionary)

**_Not an official released from Dewan Bahasa._**

#### 73k English-Malay

Total size: 1.1 MB

Originally posted by Facebook, https://dl.fbaipublicfiles.com/arrival/dictionaries/en-ms.txt

#### [200k English-Malay](dictionary/200k-english-malay)

Total size: 6.9 MB

#### [90k synonym](dictionary/synonym)

Total size: 4.7 MB    

#### [Dictionary, 24550 unique words](dictionary/dictionary)

Total size: 428 KB

#### [Dialect](dictionary/dialect)

Glossaries for,

1. johor
2. kedah
3. kelantan
4. negeri sembilan
5. melaka
6. pahang
7. penang
8. sukuan

Its a html table structure from http://prpm.dbp.gov.my/Cari1?keyword=%3d&d=150348&

#### [Ngrams](dictionary/ngram)

Total size: 92 MB

Unigram and Bigram collected from news, structure,
```python
{'saya': 1000}
```

## [Lexicon](lexicon)

Malaya provided lexicon generator to induce new lexicons, https://malaya.readthedocs.io/en/latest/Lexicon.html

#### [sentiment](lexicon/sentiment.json)

```python
{'negative': ['str1','str2'], 'positive': ['str3','str4']}
```

#### [emotion](lexicon/emotion.json)

```python
{'anger': ['str1'], 'fear': ['str2'], 'joy': ['str3'], 'love': ['str4'], 'sadness': ['str5'], 'surprise': ['str6']}
```

## [Tagging](tagging)

#### [Dependency](tagging/dependency)

Total size: 24.1 MB

#### [Part-of-Speech](tagging/part-of-speech)

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

Thank you [UD_Indonesian-GSD](https://github.com/UniversalDependencies/UD_Indonesian-GSD) for open-sourced Indonesia POS dataset, Malaya use it to transfer knowledge.

#### [Entities, JSON](tagging/entities)

Total size: 3.1 MB

1. OTHER - Other
2. law - law, regulation, related law documents, documents, etc
3. location - location, place
4. organization - organization, company, government, facilities, etc
5. person - person, group of people, believes, etc
6. quantity - numbers, quantity
7. time - date, day, time, etc
8. event - unique event happened, etc

Thank you [indonesia-ner](https://github.com/yusufsyaifudin/indonesia-ner) for open-sourced Indonesia entity dataset, Malaya use it to transfer knowledge.

## [Sentiment](sentiment)

#### [Local News](sentiment/news-sentiment)

Total size: 496 KB

1. Positive
2. Negative

#### [Twitter](sentiment/semi-supervised/twitter)

Total size: 519.4 MB

1. Positive, 1085719 sentences
2. Negative, 3463771 sentences

#### [Translated Twitter](sentiment/translate/twitter-sentiment)

Total size: 50.6 MB

1. Positive
2. Negative

#### [Translated Multidomain](sentiment/translate/multidomain-sentiment)

Total size: 159 KB

1. Amazon review, Positive and Negative
2. IMDB review, Positive and Negative
3. Yelp review, Positive and Negative

#### [Translated Polarity](sentiment/translate/polarity)

Total size: 1.3 MB

1. Positive
2. Negative

## [Corpus](corpus)

#### [Audience Nationality](corpus/audience)

Total size: 246 KB

1. constituency
2. national

#### [Translated Emotion](corpus/emotion/translate)

Total size: 7.2 MB

1. Anger
2. Fear
3. Joy
4. Love
5. Sadness
6. Surprise

#### [Twitter Emotion](corpus/emotion/lexicon)

Total size: 27.4 MB

1. Anger, 108813 rows
2. Fear, 20316 rows
3. Happy, 30962 rows
4. love, 20783 rows
5. Sadness, 26468 rows
6. Surprise, 13107 rows

#### [Gender](corpus/gender)

Total size: 2.2 MB

1. Unknown
2. Male
3. Female
4. Brand

#### [Insincere question](corpus/insincere-question)

Total size: 60.4 MB

1. Negative
2. Positive

#### [Irony](corpus/irony)

Total size: 465 KB

1. Positive
2. Negative

#### [Language-detection](corpus/language-detection)

1. english
2. malay
3. indonesia
4. rojak
5. manglish
6. others

sublanguages,

1. malay
2. kedah
3. johor
4. melaka
5. terengganu
6. sarawak
7. negeri-sembilan
8. kelantan
9. pahang
10. perak
11. sabah

#### [Malaysia-entities](corpus/malaysia-entities)

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

#### [Malaysia Topics](corpus/malaysia-topics)

Social media texts related to Malaysia topics.

Total size: 322.4 MB

<details><summary>Complete list (249 topics)</summary>

1. ganja
2. orang asli
3. kaum cina
4. k-pop
5. kaum india
6. pos laju
7. hari raya aidilfitri
8. hari raya aidiladha
9. syarikat permulaan
10. isu tanah
11. kaum melayu
12. facebook
13. keluar parti
14. sabotaj parti
15. kotak undi
16. humanoid
17. kemalangan penumpang cedera
18. kemalangan maut
19. individu penjara
20. kes rogol
21. kes cabul
22. kes rompakan
23. kes ragut
24. cambridge analytica
25. kokain
26. bebas tahanan
27. sosial media
28. twitter
29. instagram
30. mati dipukul
31. pengedar dadah
32. kematian wabak
33. letupan bom
34. isu dadah
35. isu bmf
36. isu diesel
37. isu china
38. isu saudi arabia
39. unifi
40. piala thomas
41. fifa
42. bahasa pengaturcaraan
43. baling botol
44. perkahwinan kanak-kanak
45. produk berbahaya
46. musim durian
47. world cup
48. motogp
49. euro 2020
50. ask me a question
51. thai cave
52. racist
53. bola sepak
54. hockey
55. sepak takraw
56. reformasi
57. deepavali
58. chinese new year
59. lazada sells
60. shopee sells
61. e-sport
62. valve corporation
63. dota2
64. counter strike global-offensive
65. asean football organization
66. blackpink
67. kecurian kereta
68. kecurian motosikal
69. youtube rewind
70. pewdiepie
71. isu tiket
72. kuota haji
73. tsunami
74. kes lemas
75. kes buang bayi
76. kes pecah rumah
77. paedophilia
78. kes luar nikah
79. kes tangkap basah
80. kes bawah umur
81. pdrm
82. 1mdb
83. gst
84. sst
85. tiga penjuru
86. pilihan raya umum
87. pilihan raya kecil
88. pusat daerah mangundi
89. masalah air
90. rumah mampu milik
91. pendidikan
92. sekolah
93. universiti
94. maktab rendah sains mara
95. kesihatan
96. hutang negara
97. ekonomi
98. sosial
99. menteri besar kedah
100. menteri besar perak
101. menteri besar perlis
102. menteri besar selangor
103. menteri besar johor
104. menteri besar kelantan
105. menteri besar terengganu
106. menteri besar negeri sembilan
107. felda
108. kwsp
109. sosco
110. bank malaysia
111. bank negara
112. perdana menteri
113. timbalan perdana menteri
114. menteri dalam negeri
115. menteri kewangan
116. menteri pertahanan
117. menteri belia dan sukan
118. majlis penasihat
119. skim peduli sihat
120. ptptn
121. projek mega
122. gaji minimum
123. menyiasat skandal
124. highway tol
125. tabung haji
126. tentera malaysia
127. infrastruktur
128. kos sara hidup
129. pengangkutan awam
130. perkhidmatan awam
131. isu wanita
132. survei institut darul ehsan
133. inisiatif peduli rakyat
134. teknologi
135. internet
136. kecerdasan buatan
137. ahli dewan undangan negeri
138. suruhanjaya pilihan raya malaysia
139. kertas undi
140. akta pilihan raya
141. undi pos
142. undi rosak
143. harga minyak
144. petrol
145. subsidi kerajaan
146. mh370
147. gaji menteri
148. jabatan bubar
149. telekom malaysia
150. agama
151. lgbt
152. agama islam
153. masyarakat
154. liberalisme
155. kapitalisme
156. idealogi
157. parlimen
158. pusat transformasi bandar
159. institut diraja
160. tsunami fitnah
161. makro-ekonomi
162. mikro-ekonomi
163. pasaran saham malaysia
164. pendapatan negara
165. nilai ringgit jatuh
166. gaji median
167. bursa malaysia
168. malaysia baru
169. keluar parlimen
170. dewan rakyat
171. tabung harapan
172. isu singapura
173. isu rohingya
174. isu syria
175. malaysia-indonesia
176. isu gaza
177. isu palestin
178. isu yaman
179. harimau malaya
180. isu kuil
181. isu lynas
182. isu masjid
183. isu sosma
184. isu ecrl
185. royalti minyak
186. kes rasuah
187. kewangan dan perniagaan
188. saham dan komoditi
189. isu kerugian
190. bumiputera
191. alam sekitar
192. isu kemiskinan
193. sumber asli
194. pertanian malaysia
195. pertanian durian
196. pertanian padi
197. pertanian getah
198. pertanian kelapa sawit
199. pertanian pisang
200. pertanian nenas
201. akuakultur malaysia
202. hortikultur malaysia
203. icerd
204. yang di-pertuan agong
205. perlembagaan malaysia
206. malaysia airlines
207. malaysia airport
208. kuala lumpur international airport
209. malacca airport
210. bintulu airport
211. kota kinabalu airport
212. kuching airport
213. labuan airport
214. lahad datu airport
215. langkawi airport
216. limbang airport
217. miri airport
218. penang airport
219. sandakan airport
220. sibu airport
221. sultan abdul halim airport
222. sultan haji ahmad shah airport
223. sultan azlan shah airport
224. sultan ismail petra airport
225. sultan mahmud airport
226. tawau airport
227. tioman airport
228. anggota bomba
229. angkatan tentera darat
230. angkatan tentera laut
231. angkatan tentera udara
232. anggota ambulans
233. anggota polis
234. perkhidmatan kehakiman
235. perkhidmatan am persekutuan
236. industri 4.0
237. kumpulan pengganas tempatan
238. kumpulan pengganas asing
239. sultan selangor
240. sultan kedah
241. sultan kelantan
242. sultan perlis
243. sultan johor
244. sultan negeri sembilan
245. sultan terengganu
246. pemilihan agong
247. isu plastik
248. gejala sosial
249. isytihar darurat

</details>

#### [Sarcastic news-headline](corpus/sarcastic-news-headline)

Total size: 1.78 MB

1. Positive
2. Negative

#### [Subjectivity](corpus/subjectivity)

Total size: 1.4 MB

1. Positive
2. Negative

#### [Toxicity-small](corpus/toxicity-small)

Total size: 69 MB

Toxicity-small is multilabels and multiclasses, prefer to use sigmoid / logistic.

1. toxic
2. severe toxic
3. obscene
4. threat
5. insult
6. identity hate

#### [Toxicity-large](corpus/toxicity-large)

Total size: 640 MB

Toxicity-large is multilabels and multiclasses, prefer to use sigmoid / logistic.

1. severe toxic
2. obscene
3. identity attack
4. insult
5. threat
6. asian
7. atheist
8. bisexual
9. black
10. buddhist
11. christian
12. female
13. heterosexual
14. hindu
15. homosexual, gay or lesbian
16. intellectual or learning disability
17. jewish
18. latino
19. male
20. muslim
21. other disability
22. other gender
23. other race or ethnicity
24. other religion
25. other sexual orientation
26. physical disability
27. psychiatric or mental illness
28. transgender
29. white
30. malay
31. chinese

#### [Political landscape](corpus/political-landscape)

Total size: 2 MB

1. Kerajaan (BN)
2. Pembangkang (PAS, DAP, PKR)

## [News](news)

#### [Fake News](news/fake-news)

Total size: 122.2 MB

1. Negative
2. Positive

Malaysia fake news, contributed by [syazanihussin](https://github.com/syazanihussin/FLUX/tree/master/data)

#### [30k News](news/news-30k)

Total size: 66.6 MB

Crawled on Google news using these keywords,

```python
strings = [
    'bank negara OR kewangan malaysia OR kementerian kewangan',
    'mata wang malaysia OR bon malaysia OR saham malaysia',
    'perdagangan malaysia OR ekonomi malaysia OR sosial malaysia',
    'kementerian malaysia',
    'kaum melayu OR kaum cina',
    'stock market malaysia OR saham malaysia',
    'malaysia parliament OR parlimen malaysia',
    'asia OR asean',
    'malaysia property OR hartanah malaysia',
    'artis OR wanita',
    'pendidikan OR kesihatan OR infrastruktur'
    'dr mahathir OR wan zizah OR lim guan eng OR muhyiddin OR mohamad sabu OR azmin ali',
    'umno OR pkr OR mic OR barisan nasional OR parti amanah OR dap',
    'isu kerajaan OR isu pembangkang',
    'politik OR malaysia OR dunia OR bisnes',
    'sukan OR hiburan OR teknologi OR gaya hidup OR automotif'
    'johor OR kedah OR kelantan OR melaka',
    'negeri sembilan OR pahang OR pulau pinang OR perak',
    'perlis OR sabah OR sarawak OR selangor',
    'terengganu OR kuala lumpur OR labuan OR putrajaya',
]
```

#### [Crawled News](news/news-new)

Total size: 308.7 MB

<details><summary>Complete list (462 news)</summary>

1. isu pengedar dadah
2. isu suruhanjaya tenaga
3. isu polis diraja malaysia
4. isu pakatan harapan
5. isu individu penjara
6. isu bumiputera
7. isu anwar ibrahim
8. isu mati dipukul
9. isu isu plastik
10. isu pasaran saham malaysia
11. isu undi rosak
12. isu bank malaysia
13. isu isu rohingya
14. sukan elektronik
15. isu kes buang bayi
16. isu isu singapura
17. isu lembaga pelabuhan johor
18. isu kota kinabalu airport
19. isu jabatan bekalan air
20. isu barisan nasional
21. isu kementerian perdagangan dalam negeri hal ehwal pengguna malaysia
22. isu mh370
23. isu sumber asli
24. isu kes tangkap basah
25. isu lembaga kemajuan ikan malaysia
26. isu paedophilia
27. isu suruhanjaya syarikat malaysia
28. isu suruhanjaya pengankutan awam darat
29. isu jabatan pengangkutan jalan
30. isu tunku ismail idris
31. isu asean football organization
32. isu kes cabul
33. isu lembaga pembangunan industri pembinaan
34. isu kumpulan pengganas tempatan
35. isu isu yaman
36. isu isu wanita
37. isu pejabat setiausaha persekutuan sabah
38. isu bank kerjasama rakyat malaysia
39. isu pusat transformasi bandar
40. isu jabatan parlimen malaysia
41. isu e-sport
42. isu perkhidmatan kehakiman
43. isu bebas tahanan
44. isu jabatan penjara malaysia
45. isu kewangan dan perniagaan
46. isu mahathir
47. isu menteri besar perak
48. isu perkahwinan kanak-kanak
49. isu kementerian perusahaan perladangan komoditi
50. isu kementerian tenaga teknologi hijau air malaysia
51. isu angkatan tentera malaysia
52. isu tioman airport
53. isu institut latihan kehakiman perundangan
54. isu lembaga kemajuan pertanian muda
55. isu tribunal perkhidmatan awam
56. isu datuk seri abdul hadi awang
57. isu lazada sells
58. isu perbadanan harta intelek malaysia
59. isu rosmah mansur
60. isu unit khas teknologi tinggi
61. isu pewdiepie
62. isu liberalisme
63. isu bintulu airport
64. isu perkhidmatan am persekutuan
65. isu agensi nuklear malaysia
66. isu sultan johor
67. isu k-pop
68. isu mic
69. isu humanoid
70. isu alam sekitar
71. isu perpustakaan kuala lumpur
72. isu institut kefahaman islam malaysia
73. isu jabatan perumahan negara
74. isu institut penyelidikan teknologi nuklear malaysia
75. isu jabatan penerbangan awam
76. isu lembaga pelabuhan pulau pinang
77. isu jabatan tanah galian wilayah persekutuan
78. isu kementerian kesihatan malaysia
79. .DS_Store
80. isu kes ragut
81. isu institut tadbiran awam negara
82. isu deepavali
83. isu bahasa pengaturcaraan
84. isu jabatan kebajikan masyarakat malaysia
85. isu menteri besar selangor
86. isu pertanian nenas
87. isu ikatan relawan rakyat malaysia
88. isu suruhanjaya pilihan raya malaysia
89. isu musim durian
90. isu isu diesel
91. isu pejabat perdana menteri
92. isu industri 4.0
93. isu kementerian kerja raya malaysia
94. isu malaysia airport
95. isu 1mdb
96. isu angkatan tentera laut
97. isu jabatan perikanan
98. isu isu kuil
99. isu menteri besar kedah
100. isu pejabat ketua setiausaha negara
101. isu letupan bom
102. isu yang di-pertuan agong
103. isu isu syria
104. isu sultan ismail petra airport
105. isu kuala lumpur international airport
106. isu parti keadilan rakyat
107. isu radio televisyen malaysia
108. isu lembaga pemasaran pertanian persekutuan
109. isu instagram
110. isu mca
111. isu jabatan landskap negara
112. isu sandakan airport
113. isu kes rompakan
114. isu lembaga pelabuhan kuantan
115. isu isu dadah
116. isu kapitalisme
117. isu kementerian pengangkutan malaysia
118. isu langkawi airport
119. isu kokain
120. isu sibu airport
121. isu makanan malaysia
122. isu kemalangan penumpang cedera
123. isu istana negara
124. isu fifa
125. isu perbendaharaan malaysia
126. isu masalah air
127. isu isu gaza
128. isu majlis penasihat
129. isu jabatan pengairan saliran
130. isu tabung ekonomi kumpulan usaha niaga
131. isu pertanian kelapa sawit
132. isu syed saddiq
133. isu bahagian hal ehwal undang-undang
134. isu institut terjemahan negara malaysia
135. isu pertanian malaysia
136. isu majlis agama islam wilayah persekutuan
137. isu zakir naik
138. isu nurul izzah
139. isu kuching airport
140. isu donald trump
141. isu telekom malaysia
142. isu menteri besar kelantan
143. isu royalti minyak
144. isu kementerian perdagangan antarabangsa industri
145. isu nilai ringgit jatuh
146. isu kos sara hidup
147. isu isytihar darurat
148. isu twitter
149. isu lembaga jurutera malaysia
150. isu ahli dewan undangan negeri
151. isu tribunal perumahan pengurusan strata
152. isu orang asli
153. isu jabatan pertahanan awam malaysia
154. isu dewan bahasa pustaka
155. isu angkatan tentera udara
156. isu perbadanan nasional berhad
157. isu kematian wabak
158. isu kes lemas
159. isu pendidikan
160. isu kadir jasin
161. isu hari raya aidiladha
162. isu racist
163. isu ks jomo
164. isu bersatu
165. isu datuk johari abdul
166. isu pdrm
167. mata wang digital
168. isu bursa malaysia
169. isu bernama
170. isu maktab koperasi malaysia
171. isu kesihatan
172. isu anthony loke siew fook
173. isu menteri besar terengganu
174. isu shopee sells
175. isu agama islam
176. isu sultan haji ahmad shah airport
177. isu lembaga kemajuan pertanian kemubu
178. isu kes luar nikah
179. isu menteri pertahanan
180. isu tsunami
181. isu wan azizah
182. isu gaji menteri
183. kecerdasan buatan
184. isu tawau airport
185. isu parti pribumi bersatu malaysia
186. isu agensi penguatkuasaan maritim malaysia
187. isu institut penyelidikan kemajuan pertanian malaysia
188. isu akta pilihan raya
189. isu gaji median
190. isu bahagian penyelidikan
191. isu tentera malaysia
192. isu majlis pakatan harapan
193. isu hutang negara
194. isu isu palestin
195. isu subsidi kerajaan
196. isu counter strike global-offensive
197. isu tan sri mokhzani mahathir
198. isu universiti
199. isu pertanian getah
200. isu sultan kedah
201. isu kementerian pembangunan wanita keluarga masyarakat malaysia
202. isu jabatan imigresen malaysia
203. isu youtube rewind
204. isu shafie apdal
205. isu bahagian kemajuan wilayah persekutuan perancangan lembah klang
206. isu rais yatim
207. isu icerd
208. isu menteri belia dan sukan
209. isu jabatan kimia malaysia
210. isu perkasa
211. isu kuota haji
212. isu sepak takraw
213. isu tan sri dr rais yatim
214. isu sosial media
215. isu saham dan komoditi
216. isu valve corporation
217. isu infrastruktur
218. isu jabatan bomba penyelamat malaysia
219. isu hassan merican
220. isu pilihan raya kecil
221. isu felcra
222. isu malaysia airlines
223. isu bahagian keselamatan negara
224. isu malaysia-indonesia
225. isu tabung haji
226. isu pertanian durian
227. isu institut diraja
228. isu skim peduli sihat
229. isu menteri besar johor
230. isu kes pecah rumah
231. isu world cup
232. isu suruhanjaya perkhidmatan awam
233. isu lgbt
234. isu ariff md yusof
235. isu rafizi ramli
236. isu jabatan pendaftaran negara malaysia
237. isu jabatan perdana menteri malaysia
238. isu insitut kanser negara
239. isu kaum melayu
240. isu pengangkutan awam
241. isu perkhidmatan awam
242. isu jabatan pelancongan malaysia
243. isu kecurian kereta
244. isu jabatan peguam negara
245. isu kementerian wilayah persekutuan malaysia
246. isu facebook
247. isu sultan selangor
248. isu kertas undi
249. isu suruhanjaya perkhidmatan pendidikan
250. isu masjid negara
251. isu isu ecrl
252. isu sabotaj parti
253. aplikasi malaysia
254. isu penasihat sains
255. isu unit penyelarasan pelaksanaan
256. isu dato vida
257. isu isu masjid
258. isu parti islam semalaysia
259. isu hari raya aidilfitri
260. isu isu bmf
261. isu kementerian komunikasi multimedia malaysia
262. isu bola sepak
263. isu jabatan tenaga kerja semenanjung malaysia
264. isu kementerian sains teknologi inovasi malaysia
265. isu kumpulan pengganas asing
266. isu rumah mampu milik
267. isu isu kemiskinan
268. isu kementerian pelancongan kebudayaan malaysia
269. isu menteri besar negeri sembilan
270. isu undi pos
271. isu tiga penjuru
272. isu lembaga tabung haji
273. isu jabatan perancangan bandar desa semenanjung malaysia
274. isu euro 2020
275. isu kaum india
276. isu idealogi
277. isu biro pengaduan awam
278. isu isu tanah
279. isu sosial
280. isu thai cave
281. pengaturcaraan
282. isu perdana menteri
283. isu pertanian padi
284. isu anggota polis
285. isu institut diplomasi hal ehwal luar negeri
286. isu suruhanjaya pilihan raya
287. isu pilihan raya umum
288. isu miri airport
289. isu lembaga pertubuhan peladang
290. isu petrol
291. isu ptptn
292. isu kementerian dalam negeri malaysia
293. isu harimau malaya
294. isu tentera laut diraja malaysia
295. isu malaysia baru
296. isu anggota bomba
297. isu teknologi
298. isu akuakultur malaysia
299. isu unit perancang ekonomi
300. isu dewan rakyat
301. isu survei institut darul ehsan
302. isu bahagian pengurusan perkhidmatan sumber manusia
303. isu jabatan kerajaan tempatan
304. isu isu saudi arabia
305. isu pusat sains negara
306. isu unifi
307. isu inisiatif peduli rakyat
308. isu jabatan agama islam wilayah persekutuan
309. isu syarikat permulaan
310. isu jabatan audit negara malaysia
311. isu parlimen
312. isu highway tol
313. isu kecerdasan buatan
314. isu gaji minimum
315. isu blackpink
316. isu pejabat setiausaha persekutuan sarawak
317. isu jabatan penerangan malaysia
318. isu jabatan kemajuan islam (jakim) department of islamic development
319. isu kecurian motosikal
320. isu masyarakat
321. isu yayasan hijau malaysia
322. isu kementerian kewangan malaysia
323. isu bung mokhtar
324. isu suruhanjaya perdagangan komoditi
325. isu sekolah
326. isu malaysian green technology corporation
327. isu hockey
328. isu bank pertanian
329. isu kementerian sumber manusia malaysia
330. isu tengku razaleigh hamzah
331. isu keluar parti
332. isu sultan perlis
333. isu kementerian pembangunan luar bandar
334. isu pendapatan negara
335. isu suruhanjaya perkhidmatan air negara
336. isu isu kerugian
337. isu piala thomas
338. isu jabatan pertanian malaysia
339. isu suruhanjaya persaingan malaysia
340. isu agensi kelayakan malaysia
341. isu dewan bandaraya kuala lumpur
342. isu tun daim zainuddin
343. isu jabatan perlindungan hidupan liar taman negara
344. isu menteri besar perlis
345. isu projek mega
346. isu program latihan khidmat negara
347. isu klinik 1malaysia
348. isu najib razak
349. isu harga minyak
350. isu hortikultur malaysia
351. isu democratic action party
352. isu zeti aziz
353. isu kementerian pendidikan malaysia
354. isu lembaga pembangunan pelaburan malaysia
355. isu tentera udara diraja malaysia
356. isu keluar parlimen
357. isu lahad datu airport
358. isu isu sosma
359. isu kwsp
360. isu pusat daerah mangundi
361. isu perbadanan putrajaya
362. isu anggota ambulans
363. isu kementerian pertahanan malaysia
364. isu penang airport
365. isu isu lynas
366. isu pejabat ketua pegawai keselamatan kerajaan malaysia
367. isu ask me a question
368. isu kejora
369. isu mahkamah syariah wilayah persekutuan
370. isu gejala sosial
371. isu perbadanan pengurusan sisa pepejal pembersihan awam
372. isu jabatan pengurusan sisa pepejal negara
373. isu ekonomi
374. isu isu tiket
375. isu mikro-ekonomi
376. isu kes rasuah
377. isu suruhanjaya pencegahan rasuah malaysia
378. isu menteri kewangan
379. isu suruhanjaya koperasi malaysia
380. isu menyiasat skandal
381. isu labuan airport
382. isu ppbm
383. isu sultan negeri sembilan
384. isu kotak undi
385. isu pemilihan agong
386. isu perbadanan labuan
387. isu isu china
388. isu sultan azlan shah airport
389. isu sultan abdul halim airport
390. isu baling botol
391. isu malacca airport
392. isu bank negara
393. isu kes rogol
394. isu kes bawah umur
395. isu datuk seri azmin ali
396. mata wang malaysia
397. isu pos laju
398. isu tabung harapan
399. isu majlis tindakan ekonomik negara
400. isu pelancongan malaysia
401. isu perlembagaan malaysia
402. isu jabatan perkhidmatan pembetungan
403. isu dota2
404. isu timbalan perdana menteri
405. isu sst
406. isu umno
407. isu ganja
408. isu kaum cina
409. isu jho low
410. isu robert kuok
411. isu lembaga penapisan filem
412. isu parti amanah
413. isu reformasi
414. isu jabatan perkhidmatan awam malaysia
415. isu unit pemodenan tadbiran perancangan pengurusan malaysia
416. isu kemalangan maut
417. isu jabatan keselamatan jalan raya
418. isu kementerian pertanian industri asas tani
419. isu chinese new year
420. isu cambridge analytica
421. isu gst
422. isu jabatan meteorologi malaysia
423. isu jabatan kerja raya malaysia
424. isu sultan mahmud airport
425. isu makro-ekonomi
426. isu kementerian sumber asli alam sekitar malaysia
427. isu jabatan laut malaysia
428. isu jabatan perkhidmatan awam
429. isu sultan kelantan
430. isu jabatan perancangan bandar desa
431. isu biro bantuan guaman
432. isu mahkamah persekutuan
433. isu tentera darat malaysia
434. isu pertanian pisang
435. isu institut jantung negara
436. isu institut pendidikan guru malaysia
437. isu arul kanda
438. isu biro tatanegara
439. isu sultan terengganu
440. aset digital
441. isu lembaga minyak sawit malaysia
442. isu sosco
443. isu risda
444. isu lembaga perindustrian nanas malaysia
445. isu kementerian luar negeri malaysia
446. isu produk berbahaya
447. isu suruhanjaya komunikasi multimedia malaysia
448. isu bahagian kabinet perlembangan perhubungan antara kerajaan
449. isu agama
450. isu lembaga pelabuhan klang
451. isu motogp
452. isu maktab rendah sains mara
453. isu perbadanan tabung pendidikan tinggi nasional
454. isu internet
455. isu jabatan perkhidmatan veterinar
456. isu menteri dalam negeri
457. isu lembaga lebuhraya malaysia
458. isu jabatan bubar
459. isu kementerian perumahan kerajaan tempatan malaysia
460. isu tsunami fitnah
461. isu bahagian pengurusan hartanah
462. isu felda

</details>

#### [Articles](news/articles)

Total size: 3.1 MB

1. Filem
2. Kerajaan
3. Pembelajaran
4. Pendidikan
5. Sekolah

#### [CNN News](news/cnn-news)

Consist of body and summarization.

Originally from [Question Answering Corpus](https://github.com/deepmind/rc-data), had permission to translate dataset to another language.

Total size: 453 MB

## [Speech](speech)

#### Tolong sebut

Total size: 276 MB

**Voices contributed by**,

1. `sebut-perkataan-man` voices by [Husein Zolkepli](https://www.linkedin.com/in/husein-zolkepli/)
2. `tolong-sebut` voices by [Khalil Nooh](https://www.linkedin.com/in/khalilnooh/)
3. `sebut-perkataan-woman` voices by [Mas Aisyah Ahmad](https://www.linkedin.com/in/mas-aisyah-ahmad-b46508a9/)

#### Wikipedia

Total size: 1.08 GB

**Voices contributed by**,

1. voices by [Husein Zolkepli](https://www.linkedin.com/in/husein-zolkepli/)

#### Manglish

Total size: 1.9 GB

## [Optical Character Recognition](ocr)

#### Malay-to-Jawi

Total size: 445.3 MB

Dataset is simple, malay label can get from the name [idola.png](ocr/idola.png).

![alt text](ocr/idola.png)

#### Malay handwriting (Satisfy-Regular)

Total size: 194.4 MB

Dataset is simple, malay label can get from the name [syarif.png](ocr/syarif.png).

![alt text](ocr/syarif.png)

## [English-Malay translation](english-malay)

**Output from Google Translate.**

Total size: 91.2 MB

## [Question-Answer](question-answer)

#### [General](question-answer/general)

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

#### [SQUAD](question-answer/squad)

**Translating still in progress**.

Originally from [SQUAD (Stanford Question Answering Dataset)](https://rajpurkar.github.io/SQuAD-explorer/)

Allow to translate to different language, [stated here](https://groups.google.com/forum/#!searchin/squad-stanford-qa/translate%7Csort:date/squad-stanford-qa/tLNlhhMZIFM/x9il9aF2CgAJ), and distributed under the [CC BY-SA 4.0 license](http://creativecommons.org/licenses/by-sa/4.0/legalcode).

## [Normalization](normalization)

#### [Normalize](normalization/normalize)

Total size: 2.6 MB

#### [Stemmer](normalization/stemmer)

Total size: 6.5 MB

1. News stemming
2. Wikipedia stemming

## [Text similarity](text-similarity)

#### [Quora](text-similarity/quora)

Originally from [First Quora Dataset Release: Question Pairs](https://data.quora.com/First-Quora-Dataset-Release-Question-Pairs), protected by [Terms of Service](https://www.quora.com/about/tos), allowing for non-commercial use.

Total size: 60.8 MB

#### [SNLI](text-similarity/snli)

Translated from [The Stanford Natural Language Inference (SNLI) Corpus](https://nlp.stanford.edu/projects/snli/.)

Total size: 55 MB

## [Dumping](dumping)

#### [Karangan sekolah](dumping/karangan-sekolah)

Total size: 221 KB

#### Wikipedia

Total size: 240.2 MB, 1663373 sentences, [download link](https://huseinhouse-storage.s3-ap-southeast-1.amazonaws.com/bert-bahasa/dumping-wiki-6-july-2019.json).

Total size: 255.1 MB, 1303844 sentences, [download link](https://huseinhouse-storage.s3-ap-southeast-1.amazonaws.com/bert-bahasa/dumping-wiki-20-july-2019.json).

**RAW**, Total size: 243.2 MB, 1748387 sentences, [download link](https://malaya-dataset.s3-ap-southeast-1.amazonaws.com/wikidump1-raw.json)

#### Instagram

Total size: 418.2 MB, 695571 sentences, [download link](https://huseinhouse-storage.s3-ap-southeast-1.amazonaws.com/bert-bahasa/dumping-instagram-6-july-2019.json).

#### [Twitter](dumping/twitter)

Total size: 2662.4 MB

#### Public news

Total size: 57.7 MB, 399251 sentences, [download link](https://huseinhouse-storage.s3-ap-southeast-1.amazonaws.com/bert-bahasa/dumping-news-6-july-2019.json).

#### Parliament

Total size: 46.7 MB, 252095 sentences, [download link](https://huseinhouse-storage.s3-ap-southeast-1.amazonaws.com/bert-bahasa/dumping-parliament-7-july-2019.json).

#### Singlish text

Singlish is a mix of Chinese, Bahasa, Tamil and majority English, singaporean slang.

Random crawled from different singaporean websites and blogs.

Total size: 1.2 GB, 19870766 sentences, [download link](https://huseinhouse-storage.s3-ap-southeast-1.amazonaws.com/bert-bahasa/singlish.txt).

Contributed by [brytjy](https://github.com/brytjy).

#### Singapore news

Total size: 213.1 MB, 1760382 sentences, [download link](https://huseinhouse-storage.s3-ap-southeast-1.amazonaws.com/bert-bahasa/sg-news.txt).

Contributed by [brytjy](https://github.com/brytjy).

#### [Subtitle](dumping/subtitle)

Total size: 1.5 MB

#### [Common-crawl](dumping/common-crawl)

List of `mse` language websites only. 

Total index size: 25.6 MB

Total website size: ~7.0 GB

**Please contact me personally to get entire data related**.

## [Crawl](crawl)

**This is crawled data, proceed with caution**.

#### [Foodpanda](crawl/foodpanda)

Crawled up to 4697 restaurants registered in https://www.foodpanda.my/.

Contain location, restaurant name, star rating, characteristics, delivery methods and food descriptions.

Total size: 94.1 MB

#### [Klook](crawl/klook)

Crawled up to 200 interesting locations from MY and SG klook.

Total size: 10.3 MB

#### [IIUM-Confession](crawl/iium-confession)

Crawled up to 20k confession posts.

Total size: 75.1 MB

#### [Wattpad](crawl/wattpad)

Crawled using keywords,

1. melayu
2. malaysia
3. seram
4. hantu
5. puisi
6. sajak
7. cerita

Crawled up to 7k fiction stories.

Total size: 97 MB

#### [Academia PDF](crawl/pdf)

Crawled up to 224 pdfs related to,

1. melayu
2. sejarah
3. etnik
4. bahasa
5. politik
6. makanan
7. idealogi

Total size: 50 MB

#### [ticket2u](crawl/ticket2u)

Contains 4282 events in Malaysia from 2017,

```python
{'row': {'rownum': '4282',
  'rowtotal': '4282',
  'rowpp': '18',
  'link': 'https://www.ticket2u.com.my/event/10223/emi-business-networking-3.0',
  'time': '4:00PM',
  'avatar': 'https://www.ticket2u.com.my/upload/event/listing/0-10223-8ce30523-200c-4bfa-98a9-daadd142989b-GYQ6_X.jpg',
  'datefrom106': '26 Oct 2017',
  'dateto106': '26 Oct 2017',
  'day': 'Thursday',
  'date': '26',
  'month': 'Oct',
  'year': '2017',
  'datefrom': '2017-10-26T16:00:00',
  'dateto': '2017-10-26T19:00:00',
  'active': '1',
  'id': '10223',
  'name': 'EMI Business Networking 3.0',
  'titlename': 'EMI Business Networking 3.0',
  'excerpt': '',
  'pid': '0',
  'basecurrency': 'RM',
  'online': '0',
  'countryid': '1',
  'stateid': '1',
  'areaid': '0',
  'locname': 'Denai Alam Recreational and Riding Club',
  'statename': 'WP Kuala Lumpur',
  'latitude': '3.150970999999999',
  'type': '619',
  'regboo': '0',
  'pricefrom': '75.00',
  'longitude': '101.51955099999998',
  'eventcat': 'Business Sharing and Networking Event',
  'eventcatcode': 'business',
  'eventsubcat': 'Networking',
  'eventsubcatcode': 'networking',
  'showdate': '1',
  'exclusive': '0',
  'notexclusive': '0',
  'issaleend': '1',
  'status': 'expired'}}
```

## Suggestion

1. Feel free to contact me to request new dataset.

## Citation

1. Please citate the repository if use these corpus.

```
@misc{Malaya-Dataset, We gather Bahasa Malaysia corpus! This repository to store corpus for Malaya,
  author = {Husein, Zolkepli},
  title = {Malaya-Dataset},
  year = {2018},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/huseinzol05/Malaya-Dataset}}
}
```

2. Please at least email us first before distributing these data. Remember all these hard workings we want to give it for free.
3. What do you see just the data, but nobody can see how much we spent our cost to make it public.

## Donation

<a href="https://www.patreon.com/bePatron?u=7291337"><img src="https://static1.squarespace.com/static/54a1b506e4b097c5f153486a/t/58a722ec893fc0a0b7745b45/1487348853811/patreon+art.jpeg" width="40%"></a>

Or, One time donation without credit card hustle, **7053174643, CIMB Bank, Husein Zolkepli**
