# NLP-Dataset
POS, Entity and Text for Sentiment, Emotion, Polarity, Subjectivity, Bias, Irony, Gender, Audience data-set

## Big thanks, and what you can do,
1. Clean English Twitter dataset included Python script. Got more than 2 million of labelled tweets
2. Unlabelled Bahasa dataset from twitter and local news
3. Labelled emotion-classes consist 11 different type of emotions (I am not suggested you guys take this dataset for do any training)
4. Labelled emotion-text/word-6classes consist 6 type of emotions (These one are better!, you can use SVM, SGD or Naive Bayes to do classification)

### *Any .p you can unpickle using python pickle*
```python
with open('pickle.p', 'rb') as fopen:
    file = pickle.load(fopen)
```

### Every folder got:
1. data, text data-set, cleaned
2. pos, speech tagging, only select NOUNS and VERBS
3. token, tokenize for POS
4. entity, PERSON / ORG in the text
5. vocabulary, unique words
6. dictionary, word map with position frequency
7. reverse dictionary, position frequency map with word

#### Sentiment
1. negative
2. positive

#### Audience
1. constituency
2. national

#### Bias
1. neutral
2. partisan

#### Emotion
1. anger
2. fear
3. joy
4. love
5. sadness
6. surprise

#### Gender
1. brand
2. female
3. male
4. unknown

#### Irony
1. negative
2. positive

#### Message
1. attack
2. constituency
3. information
4. media
5. mobilization
6. other
7. personal
8. policy
9. support

#### Polarity
1. negative
2. positive

#### Subjectivity
1. negative
2. positive

#### From twitter-negative
```text
hopeless for tmr :(
Everything in the kids section of IKEA is so cute. Shame I'm nearly 19 in 2 months :(
That heart sliding into the waste basket. :(
```

#### From twitter-positive
```text
omg its already 7:30 :O
Juuuuuuuuuuuuuuuuussssst Chillin!!
handed in my uniform today . i miss you already
```

## Unlabelled bahasa dataset

#### Filem articles
```text
Namanya juga mula meniti dalam dunia hiburan tanah air menerusi filem Cinta Kita bergandingan dengan Datin Sofia Jane pada 1995.
Sejak filem itu, anak kelahiran Kuala Kangsar, Perak yang juga bergelar pengarah ini terus berkecimpung dalam bidang seni hingga sekarang.
Pada usia 50 tahun, Aman masih aktif berlakon. Antara drama popular lakonannya ialah 7 Hari Mencintaiku di TV3 sebelum ini.
```

#### Kerajaan articles
```text
Sebelum ini, belanjawan universiti awam tempatan juga dipotong kerana kekangan kewangan kerajaan yang semakin meruncing menyebabkan kontrak para profesor yang berpengalaman tidak disambung.
```

#### Pembelajaran articles
```text
Pada 1999, sebagai menyambut pembaharuan di dalam pembelajaran kepolisan, SLCK dipindahkan ke Maktab Pegawai Kanan Polis Kuala Lumpur dan ditukar nama kepada Pusat Pengajian Sains Perisikan dan Kajian Strategik. Pusat pengajian ini melaksanakan kursus yang berhubung kait dengan pengurusan perisikan keselamatan negara dan keselamatan orang kenamaan.
D. Pusat Pengajian Sains Pengurusan Krisis Dan Bencana
```

#### Pendidikan articles
```text
Hasil sokongan padu Guru Besar sekolah berkenaan, Susie Khor Siew Lee, beliau juga berjaya membawa delegasi murid menyertai pelbagai festival seni dan kebudayaan di luar negara.
```

#### Sekolah articles
```text
Namun karena banyaknya siswa yang mendaftar, Dinas Pendidikan Kota Malang menambah pagu penerimaan siswa baru untuk SMPN 12 Kota Malang.
Syamsul tidak menyebutkan berapa tambahan pagu dari Dinas Pendidikan itu. Hanya saja, setelah dikurangi oleh siswa anak berkebutuhan khusus (ABK) yang berjumlah empat orang, tambahan pagu itu hanya tersisa dua kursi.
Pada saat yang bersamaan, Jaringan Kemanusiaan Jawa Timur melalui Dinas Pendidikan Kota Malang bermaksud memasukkan siswa ke sekolah tersebut.
```

#### Subtitle-Dataset
Trained Text dataset for out chatbot, all in Bahasa

1. 8Mile
2. Beautiful Mind
3. Avatar
4. Avengers
5. Batman VS Superman
6. Beauty and Beast
7. Cinderella Man
8. Fight Club
9. I am Legend
10. Inside Man
11. I Origins
12. I Robot
13. Iron Man
14. Law Abiding Citizen
15. Pirates of the Carribbean
16. Point Break
17. Seven
18. Shawshack Redemption
19. The Curious Base of Benjamin
20. The Imitation Game
21. The Pursuit of Happiness
22. Truman Show
23. War of the World
24. Colossal
25. Dark-Knight
26. Death-Note
27. Ghost in the Shell
28. Hacker
29. Kungfu Yoga
30. Mine 2016
31. Nautanki Saala
32. Prison Break whole session 4
33. The Flash Whole session 3
34. The Guardian
35. Tunnels
36. World Trade Center
37. XXX

### Big thanks to Subscene and all the crews that willing to translate into our native language.
