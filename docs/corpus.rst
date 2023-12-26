corpus
======

Audience
--------

Original website, https://www.kaggle.com/crowdflower/political-social-media-posts

Citation
~~~~~~~~

Auto generated using https://www.bibme.org/bibtex/website-citation,

.. code:: bibtex

   @misc{eight_2016, title={Political Social Media Posts}, url={https://www.kaggle.com/crowdflower/political-social-media-posts}, journal={Kaggle}, author={Eight, Figure}, year={2016}, month={Nov}}

Emotion
-------

Gathered emotion dataset using lexicon, all steps in `notebook <notebook>`__.

download
~~~~~~~~

1. https://f000.backblazeb2.com/file/malay-dataset/emotion/emotion-twitter-lexicon.json

::

   anger 108813
   fear 20316
   happy 30962
   love 20783
   sadness 26468
   surprise 13107


Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Semi-Supervised Emotion dataset,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malay-dataset/tree/master/corpus/emotion}}
   }

Gender
------

Original website, https://www.kaggle.com/crowdflower/twitter-user-gender-classification

Citation
~~~~~~~~

Auto generated using https://www.bibme.org/bibtex/website-citation,

.. code:: bibtex

   @misc{eight_2016, title={Twitter User Gender Classification}, url={https://www.kaggle.com/crowdflower/twitter-user-gender-classification}, journal={Kaggle}, author={Eight, Figure}, year={2016}, month={Nov}}

GoEmotions
----------

Original website, https://github.com/google-research/google-research/tree/master/goemotions

Download
~~~~~~~~

1. https://f000.backblazeb2.com/file/malay-dataset/corpus/goemotions/goemotions_1.translated.csv
2. https://f000.backblazeb2.com/file/malay-dataset/corpus/goemotions/goemotions_2.translated.csv
3. https://f000.backblazeb2.com/file/malay-dataset/corpus/goemotions/goemotions_3.translated.csv

Citation
~~~~~~~~

.. code:: bibtex

   @article{DBLP:journals/corr/abs-2005-00547,
   author    = {Dorottya Demszky and
   Dana Movshovitz{-}Attias and
   Jeongwoo Ko and
   Alan S. Cowen and
   Gaurav Nemade and
   Sujith Ravi},
   title     = {GoEmotions: {A} Dataset of Fine-Grained Emotions},
   journal   = {CoRR},
   volume    = {abs/2005.00547},
   year      = {2020},
   url       = {https://arxiv.org/abs/2005.00547},
   eprinttype = {arXiv},
   eprint    = {2005.00547},
   timestamp = {Fri, 08 May 2020 15:04:04 +0200},
   biburl    = {https://dblp.org/rec/journals/corr/abs-2005-00547.bib},
   bibsource = {dblp computer science bibliography, https://dblp.org}
   }

Insincere Question
------------------

Original website, https://www.kaggle.com/c/quora-insincere-questions-classification

Citation
~~~~~~~~

Auto generated using https://www.bibme.org/bibtex/website-citation,

.. code:: bibtex

   @misc{kaggle, title={Quora Insincere Questions Classification}, url={https://www.kaggle.com/c/quora-insincere-questions-classification}, journal={Kaggle}}

Irony
-----

Original website, https://www.kaggle.com/rtatman/ironic-corpus

Citation
~~~~~~~~

Auto generated using https://www.bibme.org/bibtex/website-citation,

.. code:: bibtex

   @misc{tatman_2017, title={Ironic Corpus}, url={https://www.kaggle.com/rtatman/ironic-corpus}, journal={Kaggle}, author={Tatman, Rachael}, year={2017}, month={Jul}}

Language Detection
------------------

Gathered language detection dataset using lexicon, all steps in `notebook <notebook>`__.

download
~~~~~~~~

- Download dataset from here, https://huggingface.co/datasets/mesolitica/language-detection/resolve/main/train-test.json

Splitted 80% to train and 20% to test.

Labels,

1. english, 2215975, 553739
2. malay, 7202654, 1800649
3. indonesia, 2295708, 576059
4. rojak, 757559, 189678
5. manglish, 726678, 181442
6. others, 5720022, 1428083

- Download dataset from here, https://huggingface.co/datasets/mesolitica/language-detection/resolve/main/sublanguages.json

Labels,

1. malay 7179851
2. kedah 14071
3. johor 2172
4. melaka 7714
5. terengganu 4436
6. sarawak 6429
7. negeri-sembilan 7717
8. kelantan 2305
9. pahang 3647
10. perak 1307
11. sabah 1253

Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Lexicon based Language Detection dataset,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malay-dataset/tree/master/corpus/language-detection}}
   }

Malaysia Entities
-----------------

Social media texts related to Malaysia entities using lexicon.

List
~~~~

.. raw:: html

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

.. raw:: html

   </details>


Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Lexicon based Malaysia Entities dataset,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malay-dataset/tree/master/corpus/malaysia-entities}}
   }

Malaysia Topics
---------------

Social media texts related to Malaysia topics using lexicon.

List
~~~~

.. raw:: html

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

.. raw:: html

   </details>


download
~~~~~~~~

1. Download dataset from here, https://huggingface.co/datasets/mesolitica/malaysian-twitter-by-topics/resolve/main/malaysia-topics.zip

Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Lexicon based Malaysia Topics dataset,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malay-dataset/tree/master/corpus/malaysia-topics}}
   }

Amazon Review Data
------------------

Originally from https://nijianmo.github.io/amazon/

download
~~~~~~~~

1. 

Citation
~~~~~~~~

.. code:: bibtex

   Justifying recommendations using distantly-labeled reviews and fined-grained aspects
   Jianmo Ni, Jiacheng Li, Julian McAuley
   Empirical Methods in Natural Language Processing (EMNLP), 2019

NSFW
----

Gathered NSFW dataset using lexicon, all steps in [notebook].

download
~~~~~~~~

1. download at, https://f000.backblazeb2.com/file/malay-dataset/nsfw/nsfw.json

Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Lexicon based NSFW Detection dataset,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malay-dataset/tree/master/corpus/nsfw}}
   }

The Pile
--------

Translating The Pile using Malaya EN-MS model.

Original paper, https://arxiv.org/abs/2101.00027

Original website, https://pile.eleuther.ai/

download
~~~~~~~~

jsonl format, check `download.txt <download.txt>`__.

Citation
~~~~~~~~

.. code:: bibtex

   @article{DBLP:journals/corr/abs-2101-00027,
   author    = {Leo Gao and
   Stella Biderman and
   Sid Black and
   Laurence Golding and
   Travis Hoppe and
   Charles Foster and
   Jason Phang and
   Horace He and
   Anish Thite and
   Noa Nabeshima and
   Shawn Presser and
   Connor Leahy},
   title     = {The Pile: An 800GB Dataset of Diverse Text for Language Modeling},
   journal   = {CoRR},
   volume    = {abs/2101.00027},
   year      = {2021},
   url       = {https://arxiv.org/abs/2101.00027},
   archivePrefix = {arXiv},
   eprint    = {2101.00027},
   timestamp = {Thu, 21 Jan 2021 14:42:30 +0100},
   biburl    = {https://dblp.org/rec/journals/corr/abs-2101-00027.bib},
   bibsource = {dblp computer science bibliography, https://dblp.org}
   }

Political Landscape
-------------------

**Deprecated, will update soon**.

Political Landscape detection dataset using lexicon.

Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Lexicon based Political Landscape Detection dataset,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malay-dataset/tree/master/corpus/political-landscape}}
   }

News Headlines Dataset For Sarcasm Detection
--------------------------------------------

Original website, https://www.kaggle.com/rmisra/news-headlines-dataset-for-sarcasm-detection

Citation
~~~~~~~~

.. code:: bibtex

   @misc{misra_2019, title={News Headlines Dataset For Sarcasm Detection}, url={https://www.kaggle.com/rmisra/news-headlines-dataset-for-sarcasm-detection}, journal={Kaggle}, author={Misra, Rishabh}, year={2019}, month={Jul}}

Subjectivity
------------

Original website, http://www.cs.cornell.edu/people/pabo/movie-review-data/

.. code:: bibtex

   @InProceedings{Pang+Lee:04a,
   author =       {Bo Pang and Lillian Lee},
   title =        {A Sentimental Education: Sentiment Analysis Using Subjectivity Summarization Based on Minimum Cuts},
   booktitle =    "Proceedings of the ACL",
   year =         2004
   }

Substring language detection
----------------------------

Only available ``['MS', 'EN', 'OTHERS', 'CAPITAL', 'NOT_LANG']``.

download
~~~~~~~~

1. https://huggingface.co/datasets/mesolitica/substring-language-detection/resolve/main/en-substrings.json
2. https://huggingface.co/datasets/mesolitica/substring-language-detection/resolve/main/ms-substrings.json
3. https://huggingface.co/datasets/mesolitica/substring-language-detection/resolve/main/en-ms-substrings.json
4. https://huggingface.co/datasets/mesolitica/substring-language-detection/resolve/main/en-ms-substrings-v2.json
5. https://huggingface.co/datasets/mesolitica/substring-language-detection/resolve/main/ms-en-substrings.json
6. https://huggingface.co/datasets/mesolitica/substring-language-detection/resolve/main/ms-en-substrings-v2.json

Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Substring language detection,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malay-dataset/tree/master/corpus/substring-language-detection}}
   }

Toxicity Large
--------------

Original website, https://www.kaggle.com/c/jigsaw-multilingual-toxic-comment-classification

Added a few local toxicity keywords using lexicon, all steps in `notebook <notebook>`__.

download
~~~~~~~~

url, https://f000.backblazeb2.com/file/malay-dataset/toxicity/

1. translated-0.json
2. translated-1000000.json
3. translated-1050000.json
4. translated-1100000.json
5. translated-1150000.json
6. translated-1200000.json
7. translated-1450000.json
8. translated-150000.json
9. translated-1500000.json
10. translated-1550000.json
11. translated-1600000.json
12. translated-1650000.json
13. translated-1700000.json
14. translated-1750000.json
15. translated-1800000.json
16. translated-250000.json
17. translated-300000.json
18. translated-350000.json
19. translated-400000.json
20. translated-450000.json
21. translated-50000.json
22. translated-500000.json
23. translated-550000.json
24. translated-600000.json
25. translated-650000.json
26. translated-700000.json
27. translated-750000.json
28. translated-850000.json
29. translated-900000.json
30. translated-950000.json

chinese, malay and indian labels from local tweets, https://f000.backblazeb2.com/file/malay-dataset/toxicity/kaum.json

Weak learning score using BERT Base for chinese, malay and indian labels, https://f000.backblazeb2.com/file/malay-dataset/toxicity/weak-learning-toxicity.json

Citation
~~~~~~~~

.. code:: bibtex

   @misc{kaggle, title={Jigsaw Multilingual Toxic Comment Classification}, url={https://www.kaggle.com/c/jigsaw-multilingual-toxic-comment-classification}, journal={Kaggle}}

Toxicity Small
--------------

Original website, https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge

download
~~~~~~~~

1. part 1, https://f000.backblazeb2.com/file/malay-dataset/toxicity-small/toxic0.json
2. part 2, https://f000.backblazeb2.com/file/malay-dataset/toxicity-small/toxic1.json
3. part 3, https://f000.backblazeb2.com/file/malay-dataset/toxicity-small/toxic2.json
4. part 4, https://f000.backblazeb2.com/file/malay-dataset/toxicity-small/toxic3.json
5. part 5, https://f000.backblazeb2.com/file/malay-dataset/toxicity-small/toxic4.json
6. part 6, https://f000.backblazeb2.com/file/malay-dataset/toxicity-small/toxic5.json
7. part 7, https://f000.backblazeb2.com/file/malay-dataset/toxicity-small/toxic6.json
8. part 8, https://f000.backblazeb2.com/file/malay-dataset/toxicity-small/toxic7.json

Citation
~~~~~~~~

.. code:: bibtex

   @misc{kaggle, title={Toxic Comment Classification Challenge}, url={https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge}, journal={Kaggle}}
