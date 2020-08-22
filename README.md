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

## License

Malay-Dataset is available to download for research purposes under a Creative Commons Attribution 4.0 International License.

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

Only data tagged using this <img src="https://img.shields.io/badge/creative--common-green.svg"> is protected under this license, so feel free to use it for commercial purposes after certain extended permission.

## Non-commercial Usage

A lot of data here semisupervised / translated / tagged / decoded using third party software, example, Google Translate, Google Speech, so to avoid any future complication, it is better not use this data for commercial purposes but allow for certain research purposes.

Only data tagged using this <img src="https://img.shields.io/badge/third--party-red.svg"> is protected under these parties.

## Acknowledgement

Thanks to [Im Big](https://www.facebook.com/imbigofficial/), [LigBlou](https://www.facebook.com/ligblou), [Mesolitica](https://mesolitica.com/) and [KeyReply](https://www.keyreply.com/) for sponsoring AWS Google and private cloud to deploy distributed crawlers.

<img alt="logo" width="50%" src="https://malaya-dataset.s3-ap-southeast-1.amazonaws.com/ligblou-mesolitca-keyreply.png">

## Table of contents
  * [Chatbot](#chatbot)
    * [Wiki Wizard](#wiki-wizard)
    * [ConvAI2](#convai2)
    * [Blended Skill Talk](#blended-skill-talk)
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
    * [Iproperty](#iproperty)
  * [Dictionary](#dictionary)
    * [73k English-Malay](#73k-english-malay)
    * [200k English-Malay](#200k-english-malay)
    * [90k synonym](#90k-synonym)
    * [Dictionary, 24550 unique words](#dictionary-24550-unique-words)
    * [Dialect](#dialect)
    * [Ngrams](#ngrams)
  * [Document Ranking](#document-ranking)
    * [MSMARCO](#msmarco)
  * [Dumping](#dumping)
    * [Karangan sekolah](#karangan-sekolah)
    * [Wikipedia](#wikipedia-1)
    * [Instagram](#instagram)
    * [Twitter](#twitter)
    * [Public news](#public-news)
    * [Parliament](#parliament)
    * [Singlish text](#singlish-text)
    * [Singapore news](#singapore-news)
    * [Subtitle](#subtitle)
    * [Common-crawl](#common-crawl)
  * [Keyphrase](#keyphrase)
    * [kdd](#kdd)
    * [WWW](#www)
    * [OpenKP](#openkp)
  * [Lexicon](#lexicon)
    * [Sentiment](#sentiment)
    * [Emotion](#emotion)
  * [News](#news)
    * [Fake News](#fake-news)
    * [Crawled News](#crawled-news)
    * [30k News](#30k-news)
    * [Articles](#articles)
  * [Natural Language Query](#natural-language-query)
    * [SPIDER](#spider)
    * [COSQL](#cosql)
    * [SPARC](#sparc)
  * [Normalization](#normalization)
    * [IIUM](#iium)
    * [Twitter](#twitter-1)
    * [Normalize](#normalize)
    * [Stemmer](#stemmer)
  * [Optical Character Recognition](#optical-character-recognition)
    * [Malay-to-Jawi](#malay-to-jawi)
    * [Malay handwriting (Satisfy-Regular)](#malay-handwriting-satisfy-regular)
  * [Paraphrase](#paraphrase)
    * [General](#general)
    * [Funpedia](#funpedia)
  * [Parsing](#parsing)
    * [constituency](#constituency)
    * [dependency](#dependency)
  * [Question-Answer](#question-answer)
    * [General](#general)
    * [SQUAD](#squad)
    * [Natural Questions](#Natural-Questions)
  * [Sentiment](#sentiment-1)
    * [Local News](#local-news)
    * [Twitter](#twitter-2)
    * [Translated Twitter](#Translated-Twitter)
    * [Translated Multidomain](#Translated-Multidomain)
    * [Translated Polarity](#Translated-Polarity)
  * [Speech](#speech)
    * [IIUM](#iium-1)
    * [Tolong sebut](#tolong-sebut)
    * [Wikipedia](#wikipedia)
    * [Manglish](#manglish)
    * [Youtube](#youtube)
    * [Podcast](#podcast)
  * [Summarization](#summarization)
    * [CNN News](#cnn-news)
    * [Gigawords](#gigawords)
    * [Multinews](#multinews)
    * [Semisupervised](#semisupervised)
  * [Tagging](#tagging)
    * [Part-of-Speech](#part-of-speech)
    * [Entities](#entities-json)
  * [Text-similarity](#text-similarity)
    * [Quora](#quora)
    * [SNLI](#snli)
    * [MNLI](#mnli)
  * [Translation](#translation)
    * [IIUM-Confession](#iium-confession-1)
    * [Malay-English](#malay-english)
    * [Opus](#opus)
    * [Parliament](#parliament-1)
    * [Local Movies Subtitles](#local-movies-subtitles)
    * [English News](#english-news)
  * [Suggestion](#suggestion)
  * [Citation](#citation)
  * [Donation](#donation)

## [Chatbot](chatbot)

#### [Wiki Wizard](chatbot/wiki-wizard)

Total size: 275.0 MB

Reference: https://github.com/facebookresearch/ParlAI/tree/master/parlai/tasks/wizard_of_wikipedia

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [ConvAI2](chatbot/convai2)

Total size: 127.9 MB

Reference: https://github.com/facebookresearch/ParlAI/tree/master/parlai/tasks/convai_chitchat

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [Blended Skill Talk](chatbot/blended-skill-talk)

Total size: 31.2 MB

Reference: https://github.com/facebookresearch/ParlAI/blob/master/parlai/tasks/blended_skill_talk/build.py

<img src="https://img.shields.io/badge/third--party-red.svg">

## [Corpus](corpus)

#### [Audience Nationality](corpus/audience)

Total size: 246 KB

1. constituency
2. national

Reference: https://www.kaggle.com/crowdflower/political-social-media-posts

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [Translated Emotion](corpus/emotion/translate)

Total size: 7.2 MB

1. Anger
2. Fear
3. Joy
4. Love
5. Sadness
6. Surprise

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [Twitter Emotion](corpus/emotion/lexicon)

Total size: 27.4 MB

1. Anger, 108813 rows
2. Fear, 20316 rows
3. Happy, 30962 rows
4. love, 20783 rows
5. Sadness, 26468 rows
6. Surprise, 13107 rows

<img src="https://img.shields.io/badge/creative--common-green.svg">

#### [Gender](corpus/gender)

Total size: 2.2 MB

1. Unknown
2. Male
3. Female
4. Brand

Reference: https://www.kaggle.com/crowdflower/twitter-user-gender-classification

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [Insincere question](corpus/insincere-question)

Total size: 60.4 MB

1. Negative
2. Positive

Reference: https://www.kaggle.com/c/quora-insincere-questions-classification

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [Irony](corpus/irony)

Total size: 465 KB

1. Positive
2. Negative

Reference: https://www.kaggle.com/rtatman/ironic-corpus

<img src="https://img.shields.io/badge/third--party-red.svg">

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

<img src="https://img.shields.io/badge/creative--common-green.svg">

#### [Malaysia-entities](corpus/malaysia-entities)

Social media texts related to Malaysia entities.

Total size: 190.1 MB

<img src="https://img.shields.io/badge/creative--common-green.svg">

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

<img src="https://img.shields.io/badge/creative--common-green.svg">

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

Reference: https://www.kaggle.com/rmisra/news-headlines-dataset-for-sarcasm-detection

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [Subjectivity](corpus/subjectivity)

Total size: 1.4 MB

1. Positive
2. Negative

Reference: https://www.nltk.org/api/nltk.corpus.reader.html#module-nltk.corpus.reader.categorized_sents

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [Toxicity-small](corpus/toxicity-small)

Total size: 69 MB

Toxicity-small is multilabels and multiclasses, prefer to use sigmoid / logistic.

1. toxic
2. severe toxic
3. obscene
4. threat
5. insult
6. identity hate

Reference: https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge

<img src="https://img.shields.io/badge/third--party-red.svg">

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

Reference: https://www.kaggle.com/c/jigsaw-multilingual-toxic-comment-classification

<img src="https://img.shields.io/badge/third--party-red.svg">

But label 14, 29, 30, 31 under <img src="https://img.shields.io/badge/creative--common-green.svg"> .

#### [Political landscape](corpus/political-landscape)

Total size: 2 MB

1. Kerajaan (BN)
2. Pembangkang (PAS, DAP, PKR)

<img src="https://img.shields.io/badge/creative--common-green.svg">

## [Crawl](crawl)

**The copyright data remains with the original owners of the data, do not use this data for commercial purpose.**

#### [Foodpanda](crawl/foodpanda)

**The copyright data remains with the original owners of the data, do not use this data for commercial purpose.**

Crawled up to 9547 restaurants registered in https://www.foodpanda.my/.

Contain location, restaurant name, star rating, characteristics, delivery methods, food descriptions and so much more.

Total size: 482.4 MB

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [Klook](crawl/klook)

**The copyright data remains with the original owners of the data, do not use this data for commercial purpose, https://www.klook.com/policy/**

Crawled up to 200 interesting locations from MY and SG klook.

Total size: 10.3 MB

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [IIUM-Confession](crawl/iium-confession)

**The copyright data remains with the original owners of the data, do not use this data for commercial purpose.**

Crawled up to 20k confession posts.

Total size: 75.1 MB

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [Wattpad](crawl/wattpad)

**The copyright data remains with the original owners of the data, do not use this data for commercial purpose, https://support.wattpad.com/hc/en-us/articles/216192503-Copyright-FAQ**

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

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [Academia PDF](crawl/pdf)

**The copyright data remains with the original owners of the data, do not use this data for commercial purpose, https://www.academia.edu/copyright**

Crawled up to 224 pdfs related to,

1. melayu
2. sejarah
3. etnik
4. bahasa
5. politik
6. makanan
7. idealogi

Total size: 50 MB

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [ticket2u](crawl/ticket2u)

**The copyright data remains with the original owners of the data, do not use this data for commercial purpose, https://www.ticket2u.com.my/copyright**

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

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [Iproperty](crawl/iproperty)

**The copyright data remains with the original owners of the data, do not use this data for commercial purpose, https://www.iproperty.com.my/terms-of-use/**

crawled up to 16 states on sales residential, sales commercial, rent residential, rent commercial.

Total size: 1329 MB

<img src="https://img.shields.io/badge/third--party-red.svg">

## [Dictionary](dictionary)

**_Not an official released from Dewan Bahasa._**

#### 73k English-Malay

Total size: 1.1 MB

Reference: https://dl.fbaipublicfiles.com/arrival/dictionaries/en-ms.txt

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [200k English-Malay](dictionary/200k-english-malay)

Total size: 6.9 MB

Reference: Google Translate

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [90k synonym](dictionary/synonym)

Total size: 4.7 MB

Reference: Google Translate

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [Dictionary, 24550 unique words](dictionary/dictionary)

Total size: 428 KB

Reference: https://github.com/fakhrullah/MalayLanguage

<img src="https://img.shields.io/badge/third--party-red.svg">

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

<img src="https://img.shields.io/badge/creative--common-green.svg">

#### [Ngrams](dictionary/ngram)

Total size: 92 MB

Unigram and Bigram collected from news, structure,
```python
{'saya': 1000}
```

<img src="https://img.shields.io/badge/creative--common-green.svg">

## [Document Ranking](document-ranking)

#### [MSMARCO](document-ranking/msmarco)

Total size: 1.5 GB

Reference: https://microsoft.github.io/msmarco/

<img src="https://img.shields.io/badge/third--party-red.svg">

## [Dumping](dumping)

#### [Karangan sekolah](dumping/karangan-sekolah)

Total size: 221 KB

<img src="https://img.shields.io/badge/creative--common-green.svg">

#### Wikipedia

Total size: 240.2 MB, 1663373 sentences, [download link](https://huseinhouse-storage.s3-ap-southeast-1.amazonaws.com/bert-bahasa/dumping-wiki-6-july-2019.json).

Total size: 255.1 MB, 1303844 sentences, [download link](https://huseinhouse-storage.s3-ap-southeast-1.amazonaws.com/bert-bahasa/dumping-wiki-20-july-2019.json).

**RAW**, Total size: 243.2 MB, 1748387 sentences, [download link](https://malaya-dataset.s3-ap-southeast-1.amazonaws.com/wikidump1-raw.json)

<img src="https://img.shields.io/badge/creative--common-green.svg">

#### Instagram

Total size: 418.2 MB, 695571 sentences, [download link](https://huseinhouse-storage.s3-ap-southeast-1.amazonaws.com/bert-bahasa/dumping-instagram-6-july-2019.json).

<img src="https://img.shields.io/badge/creative--common-green.svg">

#### [Twitter](dumping/twitter)

Total size: 3764.7 MB

<img src="https://img.shields.io/badge/creative--common-green.svg">

#### Public news

Total size: 57.7 MB, 399251 sentences, [download link](https://huseinhouse-storage.s3-ap-southeast-1.amazonaws.com/bert-bahasa/dumping-news-6-july-2019.json).

<img src="https://img.shields.io/badge/creative--common-green.svg">

#### Parliament

Total size: 46.7 MB, 252095 sentences, [download link](https://huseinhouse-storage.s3-ap-southeast-1.amazonaws.com/bert-bahasa/dumping-parliament-7-july-2019.json).

<img src="https://img.shields.io/badge/creative--common-green.svg">

#### Singlish text

Singlish is a mix of Chinese, Bahasa, Tamil and majority English, singaporean slang.

Random crawled from different singaporean websites and blogs.

Total size: 1.2 GB, 19870766 sentences, [download link](https://huseinhouse-storage.s3-ap-southeast-1.amazonaws.com/bert-bahasa/singlish.txt).

Contributed by [brytjy](https://github.com/brytjy).

<img src="https://img.shields.io/badge/creative--common-green.svg">

#### Singapore news

Total size: 213.1 MB, 1760382 sentences, [download link](https://huseinhouse-storage.s3-ap-southeast-1.amazonaws.com/bert-bahasa/sg-news.txt).

Contributed by [brytjy](https://github.com/brytjy).

<img src="https://img.shields.io/badge/creative--common-green.svg">

#### [Subtitle](dumping/subtitle)

Total size: 1.5 MB

<img src="https://img.shields.io/badge/creative--common-green.svg">

#### [Common-crawl](dumping/common-crawl)

List of `mse` language websites only. 

Total index size: 25.6 MB

Total website size: ~7.0 GB

Total text extracted size: 1.7 GB

<img src="https://img.shields.io/badge/creative--common-green.svg">

## [Keyphrase](keyphrase)

#### [kdd](keyphrase/kdd)

Total size: 3 MB

Reference: https://github.com/boudinfl/ake-datasets

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [WWW](keyphrase/www)

Total size: 2.7 MB

Reference: https://github.com/boudinfl/ake-datasets

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [OpenKP](keyphrase/openkp)

Total size: 574.7 MB

Reference: https://github.com/microsoft/OpenKP

<img src="https://img.shields.io/badge/third--party-red.svg">

## [Lexicon](lexicon)

Malaya provided lexicon generator to induce new lexicons, https://malaya.readthedocs.io/en/latest/Lexicon.html

#### [sentiment](lexicon/sentiment.json)

```python
{'negative': ['str1','str2'], 'positive': ['str3','str4']}
```

<img src="https://img.shields.io/badge/creative--common-green.svg">

#### [emotion](lexicon/emotion.json)

```python
{'anger': ['str1'], 'fear': ['str2'], 'joy': ['str3'], 'love': ['str4'], 'sadness': ['str5'], 'surprise': ['str6']}
```

<img src="https://img.shields.io/badge/creative--common-green.svg">

## [News](news)

#### [Fake News](news/fake-news)

Total size: 122.2 MB

1. Negative
2. Positive

<img src="https://img.shields.io/badge/third--party-red.svg">

Malaysia fake news, contributed by [syazanihussin](https://github.com/syazanihussin/FLUX/tree/master/data), <img src="https://img.shields.io/badge/creative--common-green.svg">

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

<img src="https://img.shields.io/badge/creative--common-green.svg">

#### [Crawled News](news/news-new)

Total size: 622.2 MB

<img src="https://img.shields.io/badge/creative--common-green.svg">

<details><summary>Complete list (860 news)</summary>

1. Perayaan Cahaya
2. Perayaan Ponggal
3. Tahun Baru Hindu
4. agama sesat
5. angkat berat
6. anjing
7. antarabangsa
8. aplikasi malaysia
9. arnab
10. aset digital
11. atlet
12. babi
13. baca buku
14. badak sumbu
15. bahasa jawa
16. bahasa kebangsaan
17. bahasa melayu
18. banjir
19. bankrap
20. belimbing
21. berenang
22. bina badan
23. bola baling
24. bola jaring
25. bola keranjang
26. boling padang
27. buaya
28. bulan
29. bunian
30. burung
31. cempedak
32. coklat
33. dakwah islam
34. diktator
35. disinfeksi
36. dunia islam
37. ekonomi islam
38. gajah
39. galaksi
40. ganti rugi
41. gaya baju
42. gaya fashion
43. gaya jaket
44. gaya kasut
45. gaya rambut
46. gaya rantai
47. gaya raya
48. gaya seluar
49. gaya topi
50. gelandangan
51. godam
52. gula
53. hantu bungkus
54. hantu melayu
55. hantu raya
56. harga rumah
57. hari krismas
58. harimau
59. hartanah
60. hilang kawalan
61. hilang kerja
62. hoki padang
63. hujan lebat
64. hujan
65. hukum babi
66. hutang peribadi
67. ikan
68. industri buku
69. industri pertanian
70. industri
71. isi k-pop
72. islam nusantara
73. isu 1mdb
74. isu Suku Bagahak
75. isu Suku Bajau
76. isu Suku Brunei
77. isu Suku Iban
78. isu Suku Idahan
79. isu Suku Iranun
80. isu Suku Kadazandusun
81. isu Suku Lundayeh
82. isu Suku Murut
83. isu Suku Suluk
84. isu Suku Tidong
85. isu afghanistan
86. isu afrika
87. isu agama islam
88. isu agama
89. isu agensi kelayakan malaysia
90. isu agensi nuklear malaysia
91. isu agensi penguatkuasaan maritim malaysia
92. isu ahli dewan undangan negeri
93. isu air
94. isu airasia
95. isu akta pilihan raya
96. isu akuakultur malaysia
97. isu alam sekitar
98. isu alkohol
99. isu amerika
100. isu anggota ambulans
101. isu anggota bomba
102. isu anggota polis
103. isu angkatan tentera laut
104. isu angkatan tentera malaysia
105. isu angkatan tentera udara
106. isu anthony loke siew fook
107. isu anwar ibrahim
108. isu apple
109. isu arab
110. isu arak
111. isu argentina
112. isu ariff md yusof
113. isu artificial intelligence
114. isu artis korea selatan
115. isu artis kpop
116. isu arul kanda
117. isu asean football organization
118. isu ask me a question
119. isu askar
120. isu australia
121. isu axiata
122. isu ayah pin
123. isu ayam penyet
124. isu ayam
125. isu baba dan nyonya
126. isu bahagian hal ehwal undang-undang
127. isu bahagian kabinet perlembangan perhubungan antara kerajaan
128. isu bahagian kemajuan wilayah persekutuan perancangan lembah klang
129. isu bahagian keselamatan negara
130. isu bahagian pengurusan hartanah
131. isu bahagian pengurusan perkhidmatan sumber manusia
132. isu bahagian penyelidikan
133. isu bahasa pengaturcaraan
134. isu baling botol
135. isu bangkai
136. isu bangladesh
137. isu bank kerjasama rakyat malaysia
138. isu bank malaysia
139. isu bank negara
140. isu bank pertanian
141. isu barisan nasional
142. isu bebas tahanan
143. isu berjaya group
144. isu bernama
145. isu bersatu
146. isu big bang
147. isu big data
148. isu bihun sup
149. isu bintulu airport
150. isu biro bantuan guaman
151. isu biro pengaduan awam
152. isu biro tatanegara
153. isu biseksual
154. isu blackpink
155. isu bmw
156. isu bola sepak
157. isu boling
158. isu brazil
159. isu brunei
160. isu bts
161. isu bumi
162. isu bumiputera
163. isu bung mokhtar
164. isu bursa malaysia
165. isu cambodia
166. isu cambridge analytica
167. isu celcom
168. isu chinese new year
169. isu cikgu
170. isu cimb
171. isu colombia
172. isu costa Rica
173. isu counter strike global-offensive
174. isu covid
175. isu cucms
176. isu cukai
177. isu daging
178. isu dato vida
179. isu datuk johari abdul
180. isu datuk seri abdul hadi awang
181. isu datuk seri azmin ali
182. isu deepavali
183. isu democratic action party
184. isu denmark
185. isu dewan bahasa pustaka
186. isu dewan bandaraya kuala lumpur
187. isu dewan rakyat
188. isu diabetes
189. isu digi
190. isu doktor
191. isu donald trump
192. isu dota2
193. isu e-sport
194. isu ekonomi
195. isu eropah
196. isu euro 2020
197. isu ewallet
198. isu exo
199. isu facebook
200. isu felcra
201. isu felda
202. isu fifa
203. isu finland
204. isu foodpanda
205. isu futsal
206. isu gaji median
207. isu gaji menteri
208. isu gaji minimum
209. isu gamuda berhad
210. isu ganja
211. isu gay
212. isu gejala sosial
213. isu german
214. isu gimnastik
215. isu girl generation
216. isu golf
217. isu google
218. isu grab
219. isu grabfood
220. isu gst
221. isu halal
222. isu harga minyak
223. isu hari raya aidiladha
224. isu hari raya aidilfitri
225. isu harimau malaya
226. isu hassan merican
227. isu highway tol
228. isu hockey
229. isu honda
230. isu hortikultur malaysia
231. isu humanoid
232. isu hutang negara
233. isu hutang
234. isu ibm
235. isu icerd
236. isu idealogi
237. isu ikan
238. isu ikatan relawan rakyat malaysia
239. isu ikea
240. isu india
241. isu individu penjara
242. isu indonesia
243. isu industri 4.0
244. isu infrastruktur
245. isu inisiatif peduli rakyat
246. isu insitut kanser negara
247. isu instafamous
248. isu instagram
249. isu institut diplomasi hal ehwal luar negeri
250. isu institut diraja
251. isu institut jantung negara
252. isu institut kefahaman islam malaysia
253. isu institut latihan kehakiman perundangan
254. isu institut pendidikan guru malaysia
255. isu institut penyelidikan kemajuan pertanian malaysia
256. isu institut penyelidikan teknologi nuklear malaysia
257. isu institut tadbiran awam negara
258. isu institut terjemahan negara malaysia
259. isu internet
260. isu iran
261. isu iraq
262. isu israel
263. isu istana negara
264. isu isu badminton
265. isu isu bmf
266. isu isu china
267. isu isu dadah
268. isu isu diesel
269. isu isu ecrl
270. isu isu gaza
271. isu isu kemiskinan
272. isu isu kerugian
273. isu isu kuil
274. isu isu lynas
275. isu isu masjid
276. isu isu palestin
277. isu isu plastik
278. isu isu rohingya
279. isu isu saudi arabia
280. isu isu singapura
281. isu isu sosma
282. isu isu syria
283. isu isu tanah
284. isu isu tiket
285. isu isu wanita
286. isu isu yaman
287. isu isytihar darurat
288. isu itali
289. isu jabatan agama islam wilayah persekutuan
290. isu jabatan audit negara malaysia
291. isu jabatan bekalan air
292. isu jabatan bomba penyelamat malaysia
293. isu jabatan bubar
294. isu jabatan imigresen malaysia
295. isu jabatan kebajikan masyarakat malaysia
296. isu jabatan kemajuan islam (jakim) department of islamic development
297. isu jabatan kerajaan tempatan
298. isu jabatan kerja raya malaysia
299. isu jabatan keselamatan jalan raya
300. isu jabatan kimia malaysia
301. isu jabatan landskap negara
302. isu jabatan laut malaysia
303. isu jabatan meteorologi malaysia
304. isu jabatan parlimen malaysia
305. isu jabatan peguam negara
306. isu jabatan pelancongan malaysia
307. isu jabatan pendaftaran negara malaysia
308. isu jabatan penerangan malaysia
309. isu jabatan penerbangan awam
310. isu jabatan pengairan saliran
311. isu jabatan pengangkutan jalan
312. isu jabatan pengurusan sisa pepejal negara
313. isu jabatan penjara malaysia
314. isu jabatan perancangan bandar desa semenanjung malaysia
315. isu jabatan perancangan bandar desa
316. isu jabatan perdana menteri malaysia
317. isu jabatan perikanan
318. isu jabatan perkhidmatan awam malaysia
319. isu jabatan perkhidmatan awam
320. isu jabatan perkhidmatan pembetungan
321. isu jabatan perkhidmatan veterinar
322. isu jabatan perlindungan hidupan liar taman negara
323. isu jabatan pertahanan awam malaysia
324. isu jabatan pertanian malaysia
325. isu jabatan perumahan negara
326. isu jabatan tanah galian wilayah persekutuan
327. isu jabatan tenaga kerja semenanjung malaysia
328. isu jepun
329. isu jho low
330. isu jordan
331. isu judi
332. isu k-pop
333. isu kadir jasin
334. isu kahwin
335. isu kapitalisme
336. isu kaum cina
337. isu kaum india
338. isu kaum melayu
339. isu kecerdasan buatan
340. isu kecurian kereta
341. isu kecurian motosikal
342. isu kejora
343. isu keluar parlimen
344. isu keluar parti
345. isu kemalangan maut
346. isu kemalangan penumpang cedera
347. isu kematian wabak
348. isu kementerian dalam negeri malaysia
349. isu kementerian kerja raya malaysia
350. isu kementerian kesihatan malaysia
351. isu kementerian kewangan malaysia
352. isu kementerian komunikasi multimedia malaysia
353. isu kementerian luar negeri malaysia
354. isu kementerian pelancongan kebudayaan malaysia
355. isu kementerian pembangunan luar bandar
356. isu kementerian pembangunan wanita keluarga masyarakat malaysia
357. isu kementerian pendidikan malaysia
358. isu kementerian pengangkutan malaysia
359. isu kementerian perdagangan antarabangsa industri
360. isu kementerian perdagangan dalam negeri hal ehwal pengguna malaysia
361. isu kementerian pertahanan malaysia
362. isu kementerian pertanian industri asas tani
363. isu kementerian perumahan kerajaan tempatan malaysia
364. isu kementerian perusahaan perladangan komoditi
365. isu kementerian sains teknologi inovasi malaysia
366. isu kementerian sumber asli alam sekitar malaysia
367. isu kementerian sumber manusia malaysia
368. isu kementerian tenaga teknologi hijau air malaysia
369. isu kementerian wilayah persekutuan malaysia
370. isu keracunan
371. isu kereta
372. isu kertas undi
373. isu kes bawah umur
374. isu kes buang bayi
375. isu kes cabul
376. isu kes lemas
377. isu kes luar nikah
378. isu kes pecah rumah
379. isu kes ragut
380. isu kes rasuah
381. isu kes rogol
382. isu kes rompakan
383. isu kes tangkap basah
384. isu kesihatan
385. isu kewangan dan perniagaan
386. isu kfc
387. isu khazanah
388. isu klinik 1malaysia
389. isu kokain
390. isu korea selatan
391. isu korea utara
392. isu kos sara hidup
393. isu kota kinabalu airport
394. isu kotak undi
395. isu kpop
396. isu ks jomo
397. isu kuala lumpur international airport
398. isu kuching airport
399. isu kumpulan pengganas asing
400. isu kumpulan pengganas tempatan
401. isu kuota haji
402. isu kwsp
403. isu labuan airport
404. isu lahad datu airport
405. isu laksa
406. isu langkawi airport
407. isu laos
408. isu lazada sells
409. isu lembaga jurutera malaysia
410. isu lembaga kemajuan ikan malaysia
411. isu lembaga kemajuan pertanian kemubu
412. isu lembaga kemajuan pertanian muda
413. isu lembaga lebuhraya malaysia
414. isu lembaga minyak sawit malaysia
415. isu lembaga pelabuhan johor
416. isu lembaga pelabuhan klang
417. isu lembaga pelabuhan kuantan
418. isu lembaga pelabuhan pulau pinang
419. isu lembaga pemasaran pertanian persekutuan
420. isu lembaga pembangunan industri pembinaan
421. isu lembaga pembangunan pelaburan malaysia
422. isu lembaga penapisan filem
423. isu lembaga perindustrian nanas malaysia
424. isu lembaga pertubuhan peladang
425. isu lembaga tabung haji
426. isu lesbian
427. isu letupan bom
428. isu lgbt
429. isu lhdn
430. isu liberalisme
431. isu mabuk
432. isu mahathir
433. isu mahkamah persekutuan
434. isu mahkamah syariah wilayah persekutuan
435. isu majlis agama islam wilayah persekutuan
436. isu majlis pakatan harapan
437. isu majlis penasihat
438. isu majlis tindakan ekonomik negara
439. isu makanan malaysia
440. isu makro-ekonomi
441. isu maktab koperasi malaysia
442. isu maktab rendah sains mara
443. isu malacca airport
444. isu malaysia airlines
445. isu malaysia airport
446. isu malaysia baru
447. isu malaysia-indonesia
448. isu malaysian green technology corporation
449. isu malware
450. isu masalah air
451. isu masjid negara
452. isu masyarakat
453. isu mati dipukul
454. isu maybank
455. isu mca
456. isu mcdonald
457. isu media prima
458. isu memorandum
459. isu menteri belia dan sukan
460. isu menteri besar johor
461. isu menteri besar kedah
462. isu menteri besar kelantan
463. isu menteri besar negeri sembilan
464. isu menteri besar perak
465. isu menteri besar perlis
466. isu menteri besar selangor
467. isu menteri besar terengganu
468. isu menteri dalam negeri
469. isu menteri kewangan
470. isu menteri pertahanan
471. isu menyiasat skandal
472. isu mercedes
473. isu mesir
474. isu mexico
475. isu mh370
476. isu mic
477. isu microsoft
478. isu mikro-ekonomi
479. isu minyak
480. isu miri airport
481. isu mmu
482. isu motogp
483. isu motosikal
484. isu mrsm
485. isu muhyiddin
486. isu murtabak
487. isu musim durian
488. isu mutiara
489. isu myanmar
490. isu mydin
491. isu najib razak
492. isu nasa
493. isu nasi dagang
494. isu nasi kandar
495. isu nasi kerabu
496. isu nasi
497. isu negeri
498. isu nepal
499. isu new zealand
500. isu nilai ringgit jatuh
501. isu novel
502. isu nurul izzah
503. isu orang asli
504. isu paedophilia
505. isu pakatan harapan
506. isu pakistan
507. isu palestin
508. isu parkir
509. isu parlimen
510. isu parti amanah
511. isu parti islam semalaysia
512. isu parti keadilan rakyat
513. isu parti pribumi bersatu malaysia
514. isu pasaran saham malaysia
515. isu pdrm
516. isu pejabat ketua pegawai keselamatan kerajaan malaysia
517. isu pejabat ketua setiausaha negara
518. isu pejabat perdana menteri
519. isu pejabat setiausaha persekutuan sabah
520. isu pejabat setiausaha persekutuan sarawak
521. isu pelancongan malaysia
522. isu pemilihan agong
523. isu penang airport
524. isu penasihat sains
525. isu pendapatan negara
526. isu pendidikan
527. isu pengangkutan awam
528. isu pengedar dadah
529. isu perabot
530. isu perancis
531. isu perbadanan harta intelek malaysia
532. isu perbadanan labuan
533. isu perbadanan nasional berhad
534. isu perbadanan pengurusan sisa pepejal pembersihan awam
535. isu perbadanan putrajaya
536. isu perbadanan tabung pendidikan tinggi nasional
537. isu perbendaharaan malaysia
538. isu perdana menteri
539. isu perkahwinan kanak-kanak
540. isu perkasa
541. isu perkhidmatan am persekutuan
542. isu perkhidmatan awam
543. isu perkhidmatan kehakiman
544. isu perlembagaan malaysia
545. isu perodua
546. isu perpustakaan kuala lumpur
547. isu pertanian durian
548. isu pertanian getah
549. isu pertanian kelapa sawit
550. isu pertanian malaysia
551. isu pertanian nenas
552. isu pertanian padi
553. isu pertanian pisang
554. isu petrol
555. isu petronas
556. isu pewdiepie
557. isu piala thomas
558. isu pilihan raya kecil
559. isu pilihan raya umum
560. isu ping pong
561. isu plus
562. isu polis diraja malaysia
563. isu polis
564. isu portugal
565. isu pos laju
566. isu pos malaysia
567. isu pos
568. isu ppbm
569. isu prasarana
570. isu privasi
571. isu produk berbahaya
572. isu program latihan khidmat negara
573. isu projek mega
574. isu ptptn
575. isu pusat daerah mangundi
576. isu pusat sains negara
577. isu pusat transformasi bandar
578. isu racist
579. isu radio televisyen malaysia
580. isu rafizi ramli
581. isu rais yatim
582. isu rasuah
583. isu reformasi
584. isu rhb
585. isu risda
586. isu robert kuok
587. isu rohingya
588. isu rosmah mansur
589. isu roti canai
590. isu roti
591. isu royalti minyak
592. isu rumah mampu milik
593. isu rusia
594. isu sabotaj parti
595. isu saham dan komoditi
596. isu sahur
597. isu sains data
598. isu sampah
599. isu sandakan airport
600. isu saudi
601. isu sekolah
602. isu sepak takraw
603. isu shafie apdal
604. isu shopee sells
605. isu sibu airport
606. isu sime darby
607. isu sirim
608. isu siti kasim
609. isu skim peduli sihat
610. isu sosco
611. isu sosial media
612. isu sosial
613. isu srikandi
614. isu ssm
615. isu sst
616. isu starbucks
617. isu subsidi kerajaan
618. isu sultan abdul halim airport
619. isu sultan azlan shah airport
620. isu sultan haji ahmad shah airport
621. isu sultan ismail petra airport
622. isu sultan johor
623. isu sultan kedah
624. isu sultan kelantan
625. isu sultan mahmud airport
626. isu sultan negeri sembilan
627. isu sultan perlis
628. isu sultan selangor
629. isu sultan terengganu
630. isu sumbat
631. isu sumber asli
632. isu sungai
633. isu sunway
634. isu surau
635. isu suruhanjaya komunikasi multimedia malaysia
636. isu suruhanjaya koperasi malaysia
637. isu suruhanjaya pencegahan rasuah malaysia
638. isu suruhanjaya pengankutan awam darat
639. isu suruhanjaya perdagangan komoditi
640. isu suruhanjaya perkhidmatan air negara
641. isu suruhanjaya perkhidmatan awam
642. isu suruhanjaya perkhidmatan pendidikan
643. isu suruhanjaya persaingan malaysia
644. isu suruhanjaya pilihan raya malaysia
645. isu suruhanjaya pilihan raya
646. isu suruhanjaya syarikat malaysia
647. isu suruhanjaya tenaga
648. isu survei institut darul ehsan
649. isu susu
650. isu sweden
651. isu syarikat permulaan
652. isu syarikat
653. isu syed saddiq
654. isu syria
655. isu tabung ekonomi kumpulan usaha niaga
656. isu tabung haji
657. isu tabung harapan
658. isu taekwondo
659. isu tan sri dr rais yatim
660. isu tan sri mokhzani mahathir
661. isu taska
662. isu tawau airport
663. isu teknologi
664. isu telefon
665. isu telegram
666. isu telekom malaysia
667. isu tengku razaleigh hamzah
668. isu tenis
669. isu tentera darat malaysia
670. isu tentera laut diraja malaysia
671. isu tentera malaysia
672. isu tentera udara diraja malaysia
673. isu thai cave
674. isu tiga penjuru
675. isu timbalan perdana menteri
676. isu tioman airport
677. isu tng
678. isu touch n go
679. isu toyota
680. isu transeksual
681. isu transgender
682. isu tribunal perkhidmatan awam
683. isu tribunal perumahan pengurusan strata
684. isu trojan
685. isu tsunami fitnah
686. isu tsunami
687. isu tuhan
688. isu tun daim zainuddin
689. isu tunku ismail idris
690. isu turki
691. isu twitter
692. isu u mobile
693. isu uem
694. isu uia
695. isu uitm
696. isu ukm
697. isu ulama
698. isu ulamak
699. isu um
700. isu umno
701. isu undi pos
702. isu undi rosak
703. isu unifi
704. isu unikl
705. isu unimas
706. isu unit khas teknologi tinggi
707. isu unit pemodenan tadbiran perancangan pengurusan malaysia
708. isu unit penyelarasan pelaksanaan
709. isu unit perancang ekonomi
710. isu united kingdom
711. isu universiti
712. isu upm
713. isu usm
714. isu ustaz
715. isu ustazah
716. isu utp
717. isu vaksin
718. isu valve corporation
719. isu vietnam
720. isu wan azizah
721. isu whatsapp
722. isu wisma
723. isu world cup
724. isu yaman
725. isu yang di-pertuan agong
726. isu yayasan hijau malaysia
727. isu youtube rewind
728. isu youtube
729. isu ytl
730. isu zakir naik
731. isu zeti aziz
732. jambu
733. jiwa
734. jururawat
735. jurutera
736. kacau
737. kambing
738. kampus
739. kanak kanak
740. kapitalis
741. kecerdasan buatan
742. kelahiran jesus
743. kelaparan
744. kelawar
745. kemalangan
746. kemarau
747. kerajaan adil
748. kerajaan prihatin
749. kerajaan sayang
750. kerajaan zalim
751. kes dera
752. kes positif
753. ketupat
754. kewangan islam
755. komunis
756. komunisme
757. kopi
758. kosmetik
759. kubur
760. kucing
761. kuda
762. kuliah
763. kurang mampu
764. landak
765. langsuir
766. lapangan terbang
767. lebuh rajaya
768. lelaki
769. lemang
770. lembu
771. lohong hitam
772. lontong
773. lumba basikal
774. lumba kuda
775. makanan segera
776. mata air
777. mata wang digital
778. mata wang kripto
779. mata wang malaysia
780. mata wang
781. memanah
782. menembak
783. menganggur
784. monyet
785. muflis
786. musang
787. nangka
788. nasional berhad
789. olahraga
790. orang gila
791. orang minyak
792. parti bersatu
793. pelesit
794. peluang pekerjaan
795. pembalakan kelantan
796. pembalakan
797. pembaziran
798. pencemaran air
799. pencemaran udara
800. penganggur
801. pengaturcaraan
802. pensyarah
803. perahu layar
804. perayaan Hari Gawai
805. perempuan
806. permainan
807. pesawat
808. piala dunia
809. pinjaman bank
810. pinjaman islam
811. pinjaman peribadi
812. pocong
813. pontianak
814. ragbi
815. rambutan
816. rasuah 1mdb
817. rasuah afrika
818. rasuah amerika
819. rasuah anwar
820. rasuah arab
821. rasuah barisan nasional
822. rasuah donald trump
823. rasuah israel
824. rasuah johor
825. rasuah kelantan
826. rasuah mahathir
827. rasuah najib
828. rasuah pas
829. rasuah penang
830. rasuah perlis
831. rasuah pkr
832. rasuah rosmah
833. rasuah singapore
834. rasuah thailand
835. rasuah umno
836. rendang
837. rumah tangga
838. rusa
839. saham syarikat
840. sanitasi
841. sejarah islam
842. sejarah nabi
843. silat
844. singa
845. skandal boyband
846. skandal kpop
847. sosialis
848. strategi bisnes
849. strategi perniagaan
850. suara wanita
851. sukan elektronik
852. swasta
853. tanda kiamat
854. tebu
855. tenaga nasional
856. tinju
857. toyol
858. trafik
859. tunggang agama
860. zirafah

</details>

#### [Articles](news/articles)

Total size: 3.1 MB

1. Filem
2. Kerajaan
3. Pembelajaran
4. Pendidikan
5. Sekolah

<img src="https://img.shields.io/badge/creative--common-green.svg">

## [Natural Language Query](nlq)

#### [SPIDER](nlq/spider)

Total size: 99.4 MB

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

Reference: https://github.com/taoyds/spider

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [COSQL](nlq/cosql)

Total size: 105.5 MB

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

Reference: https://yale-lily.github.io/cosql

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [SPARC](nlq/sparc)

Total size: 100.3 MB

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

Reference: https://yale-lily.github.io/sparc

<img src="https://img.shields.io/badge/third--party-red.svg">

## [Normalization](normalization)

#### [IIUM](normalization/iium)

Total size: 314 KB

<img src="https://img.shields.io/badge/creative--common-green.svg">

#### [Twitter](normalization/twitter)

Total size: 73 KB

<img src="https://img.shields.io/badge/creative--common-green.svg">

#### [Normalize](normalization/normalize)

Total size: 1.0 MB

<img src="https://img.shields.io/badge/creative--common-green.svg">

#### [Stemmer](normalization/stemmer)

Total size: 6.5 MB

1. News stemming
2. Wikipedia stemming

<img src="https://img.shields.io/badge/creative--common-green.svg">

## [Optical Character Recognition](ocr)

#### Malay-to-Jawi

Total size: 445.3 MB

Dataset is simple, malay label can get from the name [idola.png](ocr/idola.png).

![alt text](ocr/idola.png)

<img src="https://img.shields.io/badge/creative--common-green.svg">

#### Malay handwriting (Satisfy-Regular)

Total size: 194.4 MB

Dataset is simple, malay label can get from the name [syarif.png](ocr/syarif.png).

![alt text](ocr/syarif.png)

<img src="https://img.shields.io/badge/creative--common-green.svg">

## [Paraphrase](paraphrase)

#### [General](paraphrase/general)

Total size: 31.0 MB

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [Funpedia](paraphrase/funpedia)

Total size: 68.8 MB

Reference: https://github.com/facebookresearch/ParlAI/tree/master/parlai/tasks/funpedia

<img src="https://img.shields.io/badge/third--party-red.svg">

## [Parsing](parsing)

#### [Constituency](parsing/constituency)

Total size: 3.5 MB

Reference: https://github.com/ialfina/kethu

<img src="https://img.shields.io/badge/third--party-red.svg">

Augmentation, <img src="https://img.shields.io/badge/creative--common-green.svg">

#### [Dependency](parsing/dependency)

Total size: 24.1 MB

Reference: https://github.com/UniversalDependencies/UD_Indonesian-GSD

<img src="https://img.shields.io/badge/third--party-red.svg">

Augmentation, <img src="https://img.shields.io/badge/creative--common-green.svg">

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

<img src="https://img.shields.io/badge/creative--common-green.svg">

#### [SQUAD](question-answer/squad)

Total size: 129.1MB

**Translating still in progress**.

Originally from [SQUAD (Stanford Question Answering Dataset)](https://rajpurkar.github.io/SQuAD-explorer/).

Allow to translate to different language, [stated here](https://groups.google.com/forum/#!searchin/squad-stanford-qa/translate%7Csort:date/squad-stanford-qa/tLNlhhMZIFM/x9il9aF2CgAJ), and distributed under the [CC BY-SA 4.0 license](http://creativecommons.org/licenses/by-sa/4.0/legalcode).

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [Natural Questions](question-answer/natural-questions)

Total size: 8MB

Reference: https://ai.google.com/research/NaturalQuestions/

<img src="https://img.shields.io/badge/third--party-red.svg">

## [Sentiment](sentiment)

#### [Local News](sentiment/news-sentiment)

Total size: 496 KB

1. Positive
2. Negative

<img src="https://img.shields.io/badge/creative--common-green.svg">

#### [Twitter](sentiment/semi-supervised/twitter)

Total size: 519.4 MB

1. Positive, 1085719 sentences
2. Negative, 3463771 sentences

<img src="https://img.shields.io/badge/creative--common-green.svg">

#### [Translated Twitter](sentiment/translate/twitter-sentiment)

Total size: 50.6 MB

1. Positive
2. Negative

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [Translated Multidomain](sentiment/translate/multidomain-sentiment)

Total size: 159 KB

1. Amazon review, Positive and Negative
2. IMDB review, Positive and Negative
3. Yelp review, Positive and Negative

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [Translated Polarity](sentiment/translate/polarity)

Total size: 1.3 MB

1. Positive
2. Negative

<img src="https://img.shields.io/badge/third--party-red.svg">

## [Speech](speech)

#### [IIUM](speech/iium)

Read texts from IIUM confession.

Total size: 838.4 MB

**Voices contributed by**,

1. voices by [Husein Zolkepli](https://www.linkedin.com/in/husein-zolkepli/)
2. voices by [Shafiqah Idayu](https://www.facebook.com/shafiqah.ayu)

<img src="https://img.shields.io/badge/creative--common-green.svg">

#### [Tolong sebut](speech/sebut-perkataan)

Read random words from malay dictionary started with 'tolong sebut <word>'.

Total size: 276 MB

**Voices contributed by**,

1. `sebut-perkataan-man` voices by [Husein Zolkepli](https://www.linkedin.com/in/husein-zolkepli/)
2. `tolong-sebut` voices by [Khalil Nooh](https://www.linkedin.com/in/khalilnooh/)
3. `sebut-perkataan-woman` voices by [Mas Aisyah Ahmad](https://www.linkedin.com/in/mas-aisyah-ahmad-b46508a9/)

<img src="https://img.shields.io/badge/creative--common-green.svg">

#### [Wikipedia](speech/wikipedia)

Read texts from wikipedia.

Total size: 1.08 GB

**Voices contributed by**,

1. voices by [Husein Zolkepli](https://www.linkedin.com/in/husein-zolkepli/)

<img src="https://img.shields.io/badge/creative--common-green.svg">

#### [Manglish](speech/manglish)

Read texts from random manglish texts. Publicly contributed.

Total size: 1.9 GB

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [Youtube](speech/youtube)

Semi-supervised using Google Speech on bahasa youtube videos.

Total size: 48.1 GB

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [Podcast](speech/podcast)

Semi-supervised using Google Speech on https://www.aiskacang.com.my/

Total size: 112 GB

<img src="https://img.shields.io/badge/third--party-red.svg">

## [Summarization](summarization)

#### [CNN News](summarization/cnn-news)

Consist of long news and summary of it.

Originally from [Question Answering Corpus](https://github.com/deepmind/rc-data), had permission to translate dataset to another language.

Total size: 453 MB

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [Gigawords](summarization/gigawords)

Consist of long texts and summary of it.

Total size: 450 MB

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [Multinews](summarization/multinews)

Consist of long news and summary of it.

Total size: 680 MB

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [Semisupervised](summarization/semisupervised)

Abstractive output from T5-base-bahasa summarized 100k local news.

Total size: 300 MB

<img src="https://img.shields.io/badge/creative--common-green.svg">

## [Tagging](tagging)

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

Reference: https://github.com/UniversalDependencies/UD_Indonesian-GSD

<img src="https://img.shields.io/badge/third--party-red.svg">

Augmentation, <img src="https://img.shields.io/badge/creative--common-green.svg">

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

Reference: https://github.com/yusufsyaifudin/indonesia-ner

<img src="https://img.shields.io/badge/third--party-red.svg">

Augmentation, <img src="https://img.shields.io/badge/creative--common-green.svg">

## [Text similarity](text-similarity)

#### [Quora](text-similarity/quora)

Originally from [First Quora Dataset Release: Question Pairs](https://data.quora.com/First-Quora-Dataset-Release-Question-Pairs), protected by [Terms of Service](https://www.quora.com/about/tos), allowing for non-commercial use.

Total size: 60.8 MB

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [SNLI](text-similarity/snli)

Translated from [The Stanford Natural Language Inference (SNLI) Corpus](https://nlp.stanford.edu/projects/snli/.)

Total size: 55 MB

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [MNLI](text-similarity/mnli)

Total size: 92.5 MB

<img src="https://img.shields.io/badge/third--party-red.svg">

## [Translation](translation)

#### [IIUM-Confession](translation/iium-confession)

Malay to English.

Total size: 562 KB

<img src="https://img.shields.io/badge/creative--common-green.svg">

#### [Malay-English](translation/malay-english)

Total size: 935.3 MB

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [Opus](translation/opus)

Parsed from http://opus.nlpl.eu/, ms (Malay) -> en (English)

Total size: 262.6 MB

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [Parliament](translation/parliament)

Parsed from Malaysia parliament text, and translate to English.

Total size: 47.6 MB

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [Local Movies Subtitles](translation/local-movies-subtitle)

Total size: 11.4 MB

<img src="https://img.shields.io/badge/third--party-red.svg">

#### [English News](translation/english-news)

English to Malay.

Total size: 2.5 GB

<img src="https://img.shields.io/badge/third--party-red.svg">

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

<a href="https://www.buymeacoffee.com/huseinzolkepli" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

Or, One time donation without credit card hustle, **7053174643, CIMB Bank, Husein Zolkepli**
