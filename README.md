<p align="center">
    <a href="#readme">
        <img alt="logo" width="50%" src="wordcloud.png">
    </a>
</p>
<p align="center">
  <a href="https://github.com/huseinzol05/Malaya-Dataset/blob/master/LICENSE"><img alt="Apache License 2.0" src="https://img.shields.io/badge/License-Apache--2.0-yellow.svg"></a>
</p>

---

**Malay-Dataset**, We gather Bahasa Malaysia corpus! 

This repository to store corpus for [Malaya](https://github.com/huseinzol05/Malaya) and [Bahasa-NLP-Tensorflow](https://github.com/huseinzol05/Bahasa-NLP-Tensorflow). 

**We will keep update this repository overtime**.

## How we gather dataset?

1. For news, articles and subtitles, we use crawler, you can get the code from here, [Malaya/crawler](https://github.com/huseinzol05/Malaya/tree/master/misc/crawl).
2. For Bahasa, mostly we use Google Translator, you can get the code from here, [Malaya/translator](https://github.com/huseinzol05/Malaya/tree/master/misc/translator).
3. Using social media, we catch most of live data from Twitter, Facebook and Instagram using crawlers, So we just search using Elasticsearch query.
4. For speech, we recorded using wired microphone attached to Macbook Air 2013 while read some random texts from bahasa wikipedia.
5. We pay some linguists to supervised.
6. Lexicon -> weak learning from translated -> confident learning -> 5 iterations from humans.

## Acknowledgement

Thanks to [Im Big](https://www.facebook.com/imbigofficial/), [LigBlou](https://www.facebook.com/ligblou), [Mesolitica](https://mesolitica.com/) and [KeyReply](https://www.keyreply.com/) for sponsoring AWS Google and private cloud to deploy distributed crawlers.

<img alt="logo" width="50%" src="https://malaya-dataset.s3-ap-southeast-1.amazonaws.com/ligblou-mesolitca-keyreply.png">

## Table of contents
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
  * [Crawl](#crawl)
    * [Foodpanda](#foodpanda)
    * [Klook](#klook)
    * [IIUM-Confession](#iium-confession)
    * [Wattpad](#wattpad)
    * [Academia PDF](#academia-pdf)
    * [ticket2u](#ticket2u)
  * [Dictionary](#dictionary)
    * [73k English-Malay](#73k-english-malay)
    * [200k English-Malay](#200k-english-malay)
    * [90k synonym](#90k-synonym)
    * [Dictionary, 24550 unique words](#dictionary-24550-unique-words)
    * [Dialect](#dialect)
    * [Ngrams](#ngrams)
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
  * [English-Malay translation](#english-malay-translation)
  * [Lexicon](#lexicon)
    * [Sentiment](#sentiment)
    * [Emotion](#emotion)
  * [News](#news)
    * [Fake News](#fake-news)
    * [Crawled News](#crawled-news)
    * [30k News](#30k-news)
    * [Articles](#articles)
  * [Normalization](#normalization)
    * [Normalize](#normalize)
    * [Stemmer](#stemmer)
  * [Optical Character Recognition](#optical-character-recognition)
    * [Malay-to-Jawi](#malay-to-jawi)
    * [Malay handwriting (Satisfy-Regular)](#malay-handwriting-satisfy-regular)
  * [Question-Answer](#question-answer)
    * [General](#general)
    * [SQUAD](#squad)
    * [Natural Questions](#Natural-Questions)
  * [Sentiment](#sentiment-1)
    * [Local News](#local-news)
    * [Twitter](#twitter)
    * [Translated Twitter](#Translated-Twitter)
    * [Translated Multidomain](#Translated-Multidomain)
    * [Translated Polarity](#Translated-Polarity)
  * [Speech](#speech)
    * [Tolong sebut](#tolong-sebut)
    * [Wikipedia](#wikipedia)
    * [Manglish](#manglish)
  * [Summarization](#summarization)
    * [CNN News](#cnn-news)
    * [Gigawords](#gigawords)
    * [Multinews](#multinews)
    * [Semisupervised](#semisupervised)
  * [Tagging](#tagging)
    * [Dependency](#dependency)
    * [Part-of-Speech](#part-of-speech)
    * [Entities](#entities-json)
  * [Text-similarity](#text-similarity)
    * [Quora](#quora)
    * [SNLI](#snli)
  * [Suggestion](#suggestion)
  * [Citation](#citation)
  * [Donation](#donation)

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

Total size: 3236.5 MB

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

## [English-Malay translation](english-malay)

**Output from Google Translate.**

Total size: 91.2 MB

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

Total size: 523.2 MB

<details><summary>Complete list (701 news)</summary>

1. Perayaan Cahaya
2. Perayaan Ponggal
3. Tahun Baru Hindu
4. angkat berat
5. anjing
6. antarabangsa
7. aplikasi malaysia
8. arnab
9. aset digital
10. babi
11. baca buku
12. badak sumbu
13. banjir
14. berenang
15. bina badan
16. bola baling
17. bola jaring
18. bola keranjang
19. boling padang
20. buaya
21. bulan
22. burung
23. dakwah islam
24. disinfeksi
25. dunia islam
26. ekonomi islam
27. gajah
28. galaksi
29. gelandangan
30. godam
31. hari krismas
32. harimau
33. hoki padang
34. hujan
35. ikan
36. islam nusantara
37. isu 1mdb
38. isu Suku Bagahak
39. isu Suku Bajau
40. isu Suku Brunei
41. isu Suku Iban
42. isu Suku Idahan
43. isu Suku Iranun
44. isu Suku Kadazandusun
45. isu Suku Lundayeh
46. isu Suku Murut
47. isu Suku Suluk
48. isu Suku Tidong
49. isu afghanistan
50. isu afrika
51. isu agama islam
52. isu agama
53. isu agensi kelayakan malaysia
54. isu agensi nuklear malaysia
55. isu agensi penguatkuasaan maritim malaysia
56. isu ahli dewan undangan negeri
57. isu airasia
58. isu akta pilihan raya
59. isu akuakultur malaysia
60. isu alam sekitar
61. isu amerika
62. isu anggota ambulans
63. isu anggota bomba
64. isu anggota polis
65. isu angkatan tentera laut
66. isu angkatan tentera malaysia
67. isu angkatan tentera udara
68. isu anthony loke siew fook
69. isu anwar ibrahim
70. isu apple
71. isu arab
72. isu argentina
73. isu ariff md yusof
74. isu arul kanda
75. isu asean football organization
76. isu ask me a question
77. isu australia
78. isu axiata
79. isu ayam penyet
80. isu ayam
81. isu baba dan nyonya
82. isu bahagian hal ehwal undang-undang
83. isu bahagian kabinet perlembangan perhubungan antara kerajaan
84. isu bahagian kemajuan wilayah persekutuan perancangan lembah klang
85. isu bahagian keselamatan negara
86. isu bahagian pengurusan hartanah
87. isu bahagian pengurusan perkhidmatan sumber manusia
88. isu bahagian penyelidikan
89. isu bahasa pengaturcaraan
90. isu baling botol
91. isu bangladesh
92. isu bank kerjasama rakyat malaysia
93. isu bank malaysia
94. isu bank negara
95. isu bank pertanian
96. isu barisan nasional
97. isu bebas tahanan
98. isu berjaya group
99. isu bernama
100. isu bersatu
101. isu bihun sup
102. isu bintulu airport
103. isu biro bantuan guaman
104. isu biro pengaduan awam
105. isu biro tatanegara
106. isu blackpink
107. isu bmw
108. isu bola sepak
109. isu boling
110. isu brazil
111. isu brunei
112. isu bumi
113. isu bumiputera
114. isu bung mokhtar
115. isu bursa malaysia
116. isu cambodia
117. isu cambridge analytica
118. isu celcom
119. isu chinese new year
120. isu cikgu
121. isu cimb
122. isu colombia
123. isu costa Rica
124. isu counter strike global-offensive
125. isu covid
126. isu cukai
127. isu daging
128. isu dato vida
129. isu datuk johari abdul
130. isu datuk seri abdul hadi awang
131. isu datuk seri azmin ali
132. isu deepavali
133. isu democratic action party
134. isu denmark
135. isu dewan bahasa pustaka
136. isu dewan bandaraya kuala lumpur
137. isu dewan rakyat
138. isu diabetes
139. isu digi
140. isu doktor
141. isu donald trump
142. isu dota2
143. isu e-sport
144. isu ekonomi
145. isu eropah
146. isu euro 2020
147. isu facebook
148. isu felcra
149. isu felda
150. isu fifa
151. isu finland
152. isu foodpanda
153. isu futsal
154. isu gaji median
155. isu gaji menteri
156. isu gaji minimum
157. isu gamuda berhad
158. isu ganja
159. isu gejala sosial
160. isu german
161. isu gimnastik
162. isu golf
163. isu google
164. isu grab
165. isu grabfood
166. isu gst
167. isu halal
168. isu harga minyak
169. isu hari raya aidiladha
170. isu hari raya aidilfitri
171. isu harimau malaya
172. isu hassan merican
173. isu highway tol
174. isu hockey
175. isu honda
176. isu hortikultur malaysia
177. isu humanoid
178. isu hutang negara
179. isu ibm
180. isu icerd
181. isu idealogi
182. isu ikan
183. isu ikatan relawan rakyat malaysia
184. isu ikea
185. isu india
186. isu individu penjara
187. isu indonesia
188. isu industri 4.0
189. isu infrastruktur
190. isu inisiatif peduli rakyat
191. isu insitut kanser negara
192. isu instagram
193. isu institut diplomasi hal ehwal luar negeri
194. isu institut diraja
195. isu institut jantung negara
196. isu institut kefahaman islam malaysia
197. isu institut latihan kehakiman perundangan
198. isu institut pendidikan guru malaysia
199. isu institut penyelidikan kemajuan pertanian malaysia
200. isu institut penyelidikan teknologi nuklear malaysia
201. isu institut tadbiran awam negara
202. isu institut terjemahan negara malaysia
203. isu internet
204. isu iran
205. isu iraq
206. isu israel
207. isu istana negara
208. isu isu badminton
209. isu isu bmf
210. isu isu china
211. isu isu dadah
212. isu isu diesel
213. isu isu ecrl
214. isu isu gaza
215. isu isu kemiskinan
216. isu isu kerugian
217. isu isu kuil
218. isu isu lynas
219. isu isu masjid
220. isu isu palestin
221. isu isu plastik
222. isu isu rohingya
223. isu isu saudi arabia
224. isu isu singapura
225. isu isu sosma
226. isu isu syria
227. isu isu tanah
228. isu isu tiket
229. isu isu wanita
230. isu isu yaman
231. isu isytihar darurat
232. isu itali
233. isu jabatan agama islam wilayah persekutuan
234. isu jabatan audit negara malaysia
235. isu jabatan bekalan air
236. isu jabatan bomba penyelamat malaysia
237. isu jabatan bubar
238. isu jabatan imigresen malaysia
239. isu jabatan kebajikan masyarakat malaysia
240. isu jabatan kemajuan islam (jakim) department of islamic development
241. isu jabatan kerajaan tempatan
242. isu jabatan kerja raya malaysia
243. isu jabatan keselamatan jalan raya
244. isu jabatan kimia malaysia
245. isu jabatan landskap negara
246. isu jabatan laut malaysia
247. isu jabatan meteorologi malaysia
248. isu jabatan parlimen malaysia
249. isu jabatan peguam negara
250. isu jabatan pelancongan malaysia
251. isu jabatan pendaftaran negara malaysia
252. isu jabatan penerangan malaysia
253. isu jabatan penerbangan awam
254. isu jabatan pengairan saliran
255. isu jabatan pengangkutan jalan
256. isu jabatan pengurusan sisa pepejal negara
257. isu jabatan penjara malaysia
258. isu jabatan perancangan bandar desa semenanjung malaysia
259. isu jabatan perancangan bandar desa
260. isu jabatan perdana menteri malaysia
261. isu jabatan perikanan
262. isu jabatan perkhidmatan awam malaysia
263. isu jabatan perkhidmatan awam
264. isu jabatan perkhidmatan pembetungan
265. isu jabatan perkhidmatan veterinar
266. isu jabatan perlindungan hidupan liar taman negara
267. isu jabatan pertahanan awam malaysia
268. isu jabatan pertanian malaysia
269. isu jabatan perumahan negara
270. isu jabatan tanah galian wilayah persekutuan
271. isu jabatan tenaga kerja semenanjung malaysia
272. isu jepun
273. isu jho low
274. isu jordan
275. isu k-pop
276. isu kadir jasin
277. isu kahwin
278. isu kapitalisme
279. isu kaum cina
280. isu kaum india
281. isu kaum melayu
282. isu kecerdasan buatan
283. isu kecurian kereta
284. isu kecurian motosikal
285. isu kejora
286. isu keluar parlimen
287. isu keluar parti
288. isu kemalangan maut
289. isu kemalangan penumpang cedera
290. isu kematian wabak
291. isu kementerian dalam negeri malaysia
292. isu kementerian kerja raya malaysia
293. isu kementerian kesihatan malaysia
294. isu kementerian kewangan malaysia
295. isu kementerian komunikasi multimedia malaysia
296. isu kementerian luar negeri malaysia
297. isu kementerian pelancongan kebudayaan malaysia
298. isu kementerian pembangunan luar bandar
299. isu kementerian pembangunan wanita keluarga masyarakat malaysia
300. isu kementerian pendidikan malaysia
301. isu kementerian pengangkutan malaysia
302. isu kementerian perdagangan antarabangsa industri
303. isu kementerian perdagangan dalam negeri hal ehwal pengguna malaysia
304. isu kementerian pertahanan malaysia
305. isu kementerian pertanian industri asas tani
306. isu kementerian perumahan kerajaan tempatan malaysia
307. isu kementerian perusahaan perladangan komoditi
308. isu kementerian sains teknologi inovasi malaysia
309. isu kementerian sumber asli alam sekitar malaysia
310. isu kementerian sumber manusia malaysia
311. isu kementerian tenaga teknologi hijau air malaysia
312. isu kementerian wilayah persekutuan malaysia
313. isu kereta
314. isu kertas undi
315. isu kes bawah umur
316. isu kes buang bayi
317. isu kes cabul
318. isu kes lemas
319. isu kes luar nikah
320. isu kes pecah rumah
321. isu kes ragut
322. isu kes rasuah
323. isu kes rogol
324. isu kes rompakan
325. isu kes tangkap basah
326. isu kesihatan
327. isu kewangan dan perniagaan
328. isu kfc
329. isu khazanah
330. isu klinik 1malaysia
331. isu kokain
332. isu korea selatan
333. isu korea utara
334. isu kos sara hidup
335. isu kota kinabalu airport
336. isu kotak undi
337. isu ks jomo
338. isu kuala lumpur international airport
339. isu kuching airport
340. isu kumpulan pengganas asing
341. isu kumpulan pengganas tempatan
342. isu kuota haji
343. isu kwsp
344. isu labuan airport
345. isu lahad datu airport
346. isu laksa
347. isu langkawi airport
348. isu laos
349. isu lazada sells
350. isu lembaga jurutera malaysia
351. isu lembaga kemajuan ikan malaysia
352. isu lembaga kemajuan pertanian kemubu
353. isu lembaga kemajuan pertanian muda
354. isu lembaga lebuhraya malaysia
355. isu lembaga minyak sawit malaysia
356. isu lembaga pelabuhan johor
357. isu lembaga pelabuhan klang
358. isu lembaga pelabuhan kuantan
359. isu lembaga pelabuhan pulau pinang
360. isu lembaga pemasaran pertanian persekutuan
361. isu lembaga pembangunan industri pembinaan
362. isu lembaga pembangunan pelaburan malaysia
363. isu lembaga penapisan filem
364. isu lembaga perindustrian nanas malaysia
365. isu lembaga pertubuhan peladang
366. isu lembaga tabung haji
367. isu letupan bom
368. isu lgbt
369. isu lhdn
370. isu liberalisme
371. isu mahathir
372. isu mahkamah persekutuan
373. isu mahkamah syariah wilayah persekutuan
374. isu majlis agama islam wilayah persekutuan
375. isu majlis pakatan harapan
376. isu majlis penasihat
377. isu majlis tindakan ekonomik negara
378. isu makanan malaysia
379. isu makro-ekonomi
380. isu maktab koperasi malaysia
381. isu maktab rendah sains mara
382. isu malacca airport
383. isu malaysia airlines
384. isu malaysia airport
385. isu malaysia baru
386. isu malaysia-indonesia
387. isu malaysian green technology corporation
388. isu malware
389. isu masalah air
390. isu masjid negara
391. isu masyarakat
392. isu mati dipukul
393. isu maybank
394. isu mca
395. isu mcdonald
396. isu media prima
397. isu memorandum
398. isu menteri belia dan sukan
399. isu menteri besar johor
400. isu menteri besar kedah
401. isu menteri besar kelantan
402. isu menteri besar negeri sembilan
403. isu menteri besar perak
404. isu menteri besar perlis
405. isu menteri besar selangor
406. isu menteri besar terengganu
407. isu menteri dalam negeri
408. isu menteri kewangan
409. isu menteri pertahanan
410. isu menyiasat skandal
411. isu mercedes
412. isu mesir
413. isu mexico
414. isu mh370
415. isu mic
416. isu microsoft
417. isu mikro-ekonomi
418. isu minyak
419. isu miri airport
420. isu motogp
421. isu motosikal
422. isu mrsm
423. isu muhyiddin
424. isu murtabak
425. isu musim durian
426. isu myanmar
427. isu mydin
428. isu najib razak
429. isu nasa
430. isu nasi dagang
431. isu nasi kandar
432. isu nasi kerabu
433. isu nasi
434. isu nepal
435. isu new zealand
436. isu nilai ringgit jatuh
437. isu novel
438. isu nurul izzah
439. isu orang asli
440. isu paedophilia
441. isu pakatan harapan
442. isu pakistan
443. isu palestin
444. isu parlimen
445. isu parti amanah
446. isu parti islam semalaysia
447. isu parti keadilan rakyat
448. isu parti pribumi bersatu malaysia
449. isu pasaran saham malaysia
450. isu pdrm
451. isu pejabat ketua pegawai keselamatan kerajaan malaysia
452. isu pejabat ketua setiausaha negara
453. isu pejabat perdana menteri
454. isu pejabat setiausaha persekutuan sabah
455. isu pejabat setiausaha persekutuan sarawak
456. isu pelancongan malaysia
457. isu pemilihan agong
458. isu penang airport
459. isu penasihat sains
460. isu pendapatan negara
461. isu pendidikan
462. isu pengangkutan awam
463. isu pengedar dadah
464. isu perabot
465. isu perancis
466. isu perbadanan harta intelek malaysia
467. isu perbadanan labuan
468. isu perbadanan nasional berhad
469. isu perbadanan pengurusan sisa pepejal pembersihan awam
470. isu perbadanan putrajaya
471. isu perbadanan tabung pendidikan tinggi nasional
472. isu perbendaharaan malaysia
473. isu perdana menteri
474. isu perkahwinan kanak-kanak
475. isu perkasa
476. isu perkhidmatan am persekutuan
477. isu perkhidmatan awam
478. isu perkhidmatan kehakiman
479. isu perlembagaan malaysia
480. isu perodua
481. isu perpustakaan kuala lumpur
482. isu pertanian durian
483. isu pertanian getah
484. isu pertanian kelapa sawit
485. isu pertanian malaysia
486. isu pertanian nenas
487. isu pertanian padi
488. isu pertanian pisang
489. isu petrol
490. isu petronas
491. isu pewdiepie
492. isu piala thomas
493. isu pilihan raya kecil
494. isu pilihan raya umum
495. isu ping pong
496. isu plus
497. isu polis diraja malaysia
498. isu portugal
499. isu pos laju
500. isu pos malaysia
501. isu pos
502. isu ppbm
503. isu prasarana
504. isu privasi
505. isu produk berbahaya
506. isu program latihan khidmat negara
507. isu projek mega
508. isu ptptn
509. isu pusat daerah mangundi
510. isu pusat sains negara
511. isu pusat transformasi bandar
512. isu racist
513. isu radio televisyen malaysia
514. isu rafizi ramli
515. isu rais yatim
516. isu reformasi
517. isu rhb
518. isu risda
519. isu robert kuok
520. isu rohingya
521. isu rosmah mansur
522. isu roti canai
523. isu royalti minyak
524. isu rumah mampu milik
525. isu rusia
526. isu sabotaj parti
527. isu saham dan komoditi
528. isu sahur
529. isu sandakan airport
530. isu saudi
531. isu sekolah
532. isu sepak takraw
533. isu shafie apdal
534. isu shopee sells
535. isu sibu airport
536. isu sime darby
537. isu sirim
538. isu skim peduli sihat
539. isu sosco
540. isu sosial media
541. isu sosial
542. isu ssm
543. isu sst
544. isu starbucks
545. isu subsidi kerajaan
546. isu sultan abdul halim airport
547. isu sultan azlan shah airport
548. isu sultan haji ahmad shah airport
549. isu sultan ismail petra airport
550. isu sultan johor
551. isu sultan kedah
552. isu sultan kelantan
553. isu sultan mahmud airport
554. isu sultan negeri sembilan
555. isu sultan perlis
556. isu sultan selangor
557. isu sultan terengganu
558. isu sumber asli
559. isu sungai
560. isu sunway
561. isu suruhanjaya komunikasi multimedia malaysia
562. isu suruhanjaya koperasi malaysia
563. isu suruhanjaya pencegahan rasuah malaysia
564. isu suruhanjaya pengankutan awam darat
565. isu suruhanjaya perdagangan komoditi
566. isu suruhanjaya perkhidmatan air negara
567. isu suruhanjaya perkhidmatan awam
568. isu suruhanjaya perkhidmatan pendidikan
569. isu suruhanjaya persaingan malaysia
570. isu suruhanjaya pilihan raya malaysia
571. isu suruhanjaya pilihan raya
572. isu suruhanjaya syarikat malaysia
573. isu suruhanjaya tenaga
574. isu survei institut darul ehsan
575. isu sweden
576. isu syarikat permulaan
577. isu syarikat
578. isu syed saddiq
579. isu syria
580. isu tabung ekonomi kumpulan usaha niaga
581. isu tabung haji
582. isu tabung harapan
583. isu taekwondo
584. isu tan sri dr rais yatim
585. isu tan sri mokhzani mahathir
586. isu tawau airport
587. isu teknologi
588. isu telefon
589. isu telegram
590. isu telekom malaysia
591. isu tengku razaleigh hamzah
592. isu tenis
593. isu tentera darat malaysia
594. isu tentera laut diraja malaysia
595. isu tentera malaysia
596. isu tentera udara diraja malaysia
597. isu thai cave
598. isu tiga penjuru
599. isu timbalan perdana menteri
600. isu tioman airport
601. isu toyota
602. isu tribunal perkhidmatan awam
603. isu tribunal perumahan pengurusan strata
604. isu trojan
605. isu tsunami fitnah
606. isu tsunami
607. isu tun daim zainuddin
608. isu tunku ismail idris
609. isu turki
610. isu twitter
611. isu u mobile
612. isu uem
613. isu umno
614. isu undi pos
615. isu undi rosak
616. isu unifi
617. isu unit khas teknologi tinggi
618. isu unit pemodenan tadbiran perancangan pengurusan malaysia
619. isu unit penyelarasan pelaksanaan
620. isu unit perancang ekonomi
621. isu united kingdom
622. isu universiti
623. isu ustaz
624. isu ustazah
625. isu vaksin
626. isu valve corporation
627. isu vietnam
628. isu wan azizah
629. isu whatsapp
630. isu world cup
631. isu yaman
632. isu yang di-pertuan agong
633. isu yayasan hijau malaysia
634. isu youtube rewind
635. isu youtube
636. isu ytl
637. isu zakir naik
638. isu zeti aziz
639. jururawat
640. jurutera
641. kambing
642. kecerdasan buatan
643. kelahiran jesus
644. kelawar
645. kemalangan
646. kemarau
647. kerajaan adil
648. kerajaan prihatin
649. kerajaan sayang
650. kerajaan zalim
651. kes dera
652. kes positif
653. kucing
654. kuda
655. landak
656. lapangan terbang
657. lelaki
658. lembu
659. lohong hitam
660. lumba basikal
661. makanan segera
662. mata air
663. mata wang digital
664. mata wang kripto
665. mata wang malaysia
666. mata wang
667. memanah
668. menembak
669. menganggur
670. monyet
671. musang
672. nasional berhad
673. olahraga
674. parti bersatu
675. peluang pekerjaan
676. pencemaran air
677. pencemaran udara
678. pengaturcaraan
679. perahu layar
680. perayaan Hari Gawai
681. perempuan
682. permainan
683. pesawat
684. pinjaman bank
685. pinjaman islam
686. ragbi
687. rusa
688. saham syarikat
689. sanitasi
690. sejarah islam
691. sejarah nabi
692. silat
693. singa
694. strategi bisnes
695. strategi perniagaan
696. sukan elektronik
697. swasta
698. tanda kiamat
699. tenaga nasional
700. tinju
701. zirafah

</details>

#### [Articles](news/articles)

Total size: 3.1 MB

1. Filem
2. Kerajaan
3. Pembelajaran
4. Pendidikan
5. Sekolah

## [Normalization](normalization)

#### [Normalize](normalization/normalize)

Total size: 2.6 MB

#### [Stemmer](normalization/stemmer)

Total size: 6.5 MB

1. News stemming
2. Wikipedia stemming

## [Optical Character Recognition](ocr)

#### Malay-to-Jawi

Total size: 445.3 MB

Dataset is simple, malay label can get from the name [idola.png](ocr/idola.png).

![alt text](ocr/idola.png)

#### Malay handwriting (Satisfy-Regular)

Total size: 194.4 MB

Dataset is simple, malay label can get from the name [syarif.png](ocr/syarif.png).

![alt text](ocr/syarif.png)

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

Total size: 129.1MB

**Translating still in progress**.

Originally from [SQUAD (Stanford Question Answering Dataset)](https://rajpurkar.github.io/SQuAD-explorer/).

Allow to translate to different language, [stated here](https://groups.google.com/forum/#!searchin/squad-stanford-qa/translate%7Csort:date/squad-stanford-qa/tLNlhhMZIFM/x9il9aF2CgAJ), and distributed under the [CC BY-SA 4.0 license](http://creativecommons.org/licenses/by-sa/4.0/legalcode).

#### [Natural Questions](question-answer/natural-questions)

Total size: 8MB

Originally from [Natural Questions](https://ai.google.com/research/NaturalQuestions/).

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

## [Speech](speech)

#### [Tolong sebut](speech/sebut-perkataan)

Total size: 276 MB

**Voices contributed by**,

1. `sebut-perkataan-man` voices by [Husein Zolkepli](https://www.linkedin.com/in/husein-zolkepli/)
2. `tolong-sebut` voices by [Khalil Nooh](https://www.linkedin.com/in/khalilnooh/)
3. `sebut-perkataan-woman` voices by [Mas Aisyah Ahmad](https://www.linkedin.com/in/mas-aisyah-ahmad-b46508a9/)

#### [Wikipedia](speech/wikipedia)

Total size: 1.08 GB

**Voices contributed by**,

1. voices by [Husein Zolkepli](https://www.linkedin.com/in/husein-zolkepli/)

#### [Manglish](speech/manglish)

Total size: 1.9 GB

## [Summarization](summarization)

#### [CNN News](summarization/cnn-news)

Consist of long news and summary of it.

Originally from [Question Answering Corpus](https://github.com/deepmind/rc-data), had permission to translate dataset to another language.

Total size: 453 MB

#### [Gigawords](summarization/gigawords)

Consist of long texts and summary of it.

Total size: 450 MB

#### [Multinews](summarization/multinews)

Consist of long news and summary of it.

Total size: 680 MB

#### [Semisupervised](summarization/semisupervised)

Abstractive output from T5-base-bahasa summarized 100k local news.

Total size: 300 MB

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

## [Text similarity](text-similarity)

#### [Quora](text-similarity/quora)

Originally from [First Quora Dataset Release: Question Pairs](https://data.quora.com/First-Quora-Dataset-Release-Question-Pairs), protected by [Terms of Service](https://www.quora.com/about/tos), allowing for non-commercial use.

Total size: 60.8 MB

#### [SNLI](text-similarity/snli)

Translated from [The Stanford Natural Language Inference (SNLI) Corpus](https://nlp.stanford.edu/projects/snli/.)

Total size: 55 MB

## Suggestion

1. Feel free to contact me to request new dataset.
2. Feel free to open an issue if link to dataset is forbidden, sometime I forgot to make it open to public.

## Citation

1. Please citate the repository if use these corpus.

```
@misc{Malay-Dataset, We gather Bahasa Malaysia corpus!,
  author = {Husein, Zolkepli},
  title = {Malay-Dataset},
  year = {2018},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/huseinzol05/Malay-Dataset}}
}
```

2. Please at least email us first before distributing these data. Remember all these hard workings we want to give it for free.
3. What do you see just the data, but nobody can see how much we spent our cost to make it public.

## Donation

<a href="https://www.patreon.com/bePatron?u=7291337"><img src="https://static1.squarespace.com/static/54a1b506e4b097c5f153486a/t/58a722ec893fc0a0b7745b45/1487348853811/patreon+art.jpeg" width="40%"></a>

Or, One time donation without credit card hustle, **7053174643, CIMB Bank, Husein Zolkepli**
