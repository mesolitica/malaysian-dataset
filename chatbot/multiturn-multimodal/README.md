# Multiturn Multimodal

We want to generate synthetic data that able to understand position and relationship between multi-images and mulit-audio, example as below,

## multi-images

```python
{'filename': ['00370/003705168.jpg', '00611/006111738.jpg'],
 'filename_description': ['paco man edp gift set',
  "raspberry lemonade is a must in new york's famous cocktail scene"],
 'instruction': 'What is related between picture 1 and picture 2',
 'answer': "There is no direct relation between Picture 1 (Paco Rabanne 1 Million Edp Gift Set) and Picture 2 (Raspberry Lemonade being a must in New York's famous cocktail scene). Both are unrelated to each other. The first picture is an image of a perfume gift set, while the second picture is a depiction of a popular cocktail in New York City."}
```

## multi-images multi-audio

```python
{'filename': ['output-audio/3-2648-47.mp3', '00180/001805101.jpg'],
 'filename_description': ['Saya mahu muka mereka terlihat beras, anda tahu apa yang saya maksudkan. Dan sanitizer. Dan kemudian ini adalah earphone. Sama-sama kalau airpod saya, anda tahu, hilang bateri. Saya tidak pasti jika saya patut membawa tripod saya kerana saya mungkin. Adakah saya akan melakukan TikTok di kafe? Saya tidak tahu tetapi tidak menyakiti untuk membawanya. Maksud saya, ia tidak begitu keras. Saya perlu membawa krim tangan saya. Dan kemudian bumbu. Dan lip balm. Dan kemudian kita siap untuk pergi.',
  'a water wheel with moss growing on the wheels metal print by randall white'],
 'instruction': 'What is related between audio 1 and picture 1',
 'answer': "The audio and picture do not have a direct relation to each other. The audio is about preparing items for an outing, including sanitizer, earphones, a tripod, and various other personal items. The picture is a print of a water wheel with moss growing on it by Randall White. There is no connection between the audio's content and the picture's subject matter."}
```

## multi-audio

```python
{'filename': ['output-audio/3-2080-38.mp3', 'output-audio/0-2823-0.mp3'],
 'filename_description': ['Terima kasih Menteri. Saya jemput soalan tambahan yang kedua. Bagan Serai. Terima kasih Tuan Speaker. Berapakah jumlah kemalangan yang menyebabkan kematian disebabkan oleh pengaruh handphone, penggunaan handphone semasa mandu. Kerana guna handphone mandu ini dia macam mabuk lebih Tuan Speaker. Dan dia hilang orientasi. Dia tak tahu di mana traffic light, dia tak tahu dia di mana berada dan tiba-tiba dah sampai. Jadi apa kerajaan nak buat untuk menurunkan tabiat buruk menggunakan handphone semasa mandu.',
  'dalam video tu saya dah kitamkan kening lah sebab benda tu kita mencuba so at least kita dah mencuba kita kan nak mencuba kan masa ni lah mencuba kan janganlah pula usia macam aku dah 50 pun nak cuba kenapa masa buat lagu raya cover tu tak boleh hijau sebab dia nak image ketupat macam Aina Abdul juga dia ketupat kita bawa image rambut tu warna hijau ketupat juga kan tapi dah habis raya after this memang nak reveal jugalah kan habis ni memang saya akan kekalkan image yang very very formal je lah'],
 'instruction': 'What is related between audio 1 and audio 2',
 'answer': 'Audio 1 and Audio 2 are unrelated as they discuss different topics. In Audio 1, the speaker is discussing the issue of using handphones while driving and its contribution to accidents. In Audio 2, the speaker is talking about making a cover song for Raya and the challenges they faced in creating the image for the video.'}
```