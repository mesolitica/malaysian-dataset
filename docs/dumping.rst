dumping
=======

Filter C4
---------

Original repository at https://huggingface.co/datasets/c4

download
~~~~~~~~

1. https://huggingface.co/datasets/malaysia-ai/dedup-text-dataset/resolve/main/c4-filtered.jsonl

CC-100
------

Originally from https://data.statmt.org/cc-100/

download
~~~~~~~~

1. https://huggingface.co/datasets/mesolitica/cc-100-ms-dedup/resolve/main/dedup.jsonl

Common Crawl
------------

download
~~~~~~~~

1. download website indices, 25.6 MB, https://f000.backblazeb2.com/file/malay-dataset/dumping/common-crawl/mse-index.zip
2. download dumped, 9.6 GB, https://f000.backblazeb2.com/file/malay-dataset/dumping/common-crawl/feather.zip
3. download cleaned pure text, 2.93 GB, https://f000.backblazeb2.com/file/malay-dataset/dumping/common-crawl/cleaned-common-crawl.txt
4. dedup, https://huggingface.co/datasets/mesolitica/common-crawl-dedup/resolve/main/dedup.jsonl

download 2022-49
~~~~~~~~~~~~~~~~

1. website indices, https://huggingface.co/datasets/mesolitica/common-crawl-2022-49/tree/main

Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Common Crawl,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malay-dataset/tree/master/dumping/singlish-text}}
   }

facebook
--------

Crawl facebook using https://github.com/kevinzg/facebook-scraper

download
~~~~~~~~

1. https://huggingface.co/datasets/mesolitica/fb-malaysian-pages/raw/main/anwar-ibrahim.json
2. https://huggingface.co/datasets/mesolitica/fb-malaysian-pages/resolve/main/najib-razak.json
3. https://huggingface.co/datasets/mesolitica/fb-malaysian-pages/resolve/main/pakatan-harapan.json
4. https://huggingface.co/datasets/mesolitica/fb-malaysian-pages/resolve/main/rafizi-ramli.json
5. https://huggingface.co/datasets/mesolitica/fb-malaysian-pages/resolve/main/sanusi.json
6. https://huggingface.co/datasets/mesolitica/fb-malaysian-pages/resolve/main/mygag.json
7. https://huggingface.co/datasets/mesolitica/fb-malaysian-pages/resolve/main/Ayahanda-Abdul-Rani-Kulup-1753773051575006.json
8. https://huggingface.co/datasets/mesolitica/fb-malaysian-pages/resolve/main/groups-1098480360644592.json
9. https://huggingface.co/datasets/mesolitica/fb-malaysian-pages/resolve/main/groups-1483603055330698.json
10. https://huggingface.co/datasets/mesolitica/fb-malaysian-pages/resolve/main/groups-2025865557592801.json
11. https://huggingface.co/datasets/mesolitica/fb-malaysian-pages/resolve/main/groups-392252305221999.json
12. dedup, https://huggingface.co/datasets/mesolitica/fb-malaysian-pages/resolve/main/dedup.jsonl

Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Malaysian Facebook pages,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malay-dataset/tree/master/dumping/facebook}}
   }

IMDA transcription
------------------

Extracted from IMDA dataset, https://www.imda.gov.sg/

download
~~~~~~~~

Total size: 181 MB, 3312135 sentences, https://f000.backblazeb2.com/file/malay-dataset/dumping/imda/singlish-text.json

Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Singlish Texts,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malay-dataset/tree/master/dumping/singlish-text}}
   }

Instagram
---------

Gathered from crawlers.

download
~~~~~~~~

Total size: 418.2 MB, 695571 sentences, https://f000.backblazeb2.com/file/malay-dataset/dumping/instagram/dumping-instagram-6-july-2019.json

Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Bahasa Instagram,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malay-dataset/tree/master/dumping/instagram}}
   }

Karangan Sekolah
----------------

Gathered from Google Search.

Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Karangan Sekolah,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malay-dataset/tree/master/dumping/karangan-sekolah}}
   }

Manglish Twitter
----------------

Gathered from Twitter Streaming.

download
~~~~~~~~

1. Download from here, https://f000.backblazeb2.com/file/malay-dataset/dumping/twitter/manglish.json

Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Manglish Twitter,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malay-dataset/tree/master/dumping/manglish}}
   }

NLLB
----

download
~~~~~~~~

1. Filter and dedup, https://huggingface.co/datasets/mesolitica/NLLB-zsm_Latn-dedup/resolve/main/dedup-eng_Latn-zsm_Latn.jsonl

how-to
~~~~~~

Total size: 57.7 MB, 399251 sentences, `download link <https://f000.backblazeb2.com/file/malay-dataset/dumping/news/dumping-news-6-july-2019.json>`__.

Reddit
------

Malaysian and Singaporean subreddit.

download
~~~~~~~~

1. https://f000.backblazeb2.com/file/malay-dataset/dumping/reddit/r-MalaysiaPolitics
2. https://f000.backblazeb2.com/file/malay-dataset/dumping/reddit/r-MalaysianFood
3. https://f000.backblazeb2.com/file/malay-dataset/dumping/reddit/r-MalaysianPF
4. https://f000.backblazeb2.com/file/malay-dataset/dumping/reddit/r-SingaporeRaw
5. https://f000.backblazeb2.com/file/malay-dataset/dumping/reddit/r-malaysia
6. https://f000.backblazeb2.com/file/malay-dataset/dumping/reddit/r-malaysians
7. https://f000.backblazeb2.com/file/malay-dataset/dumping/reddit/r-singapore
8. combined and dedup, https://huggingface.co/datasets/mesolitica/reddit/resolve/main/dedup.jsonl

Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Reddit,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malay-dataset/tree/master/dumping/reddit}}
   }

Singapore News
--------------

Contributed by `brytjy <https://github.com/brytjy>`__.

download
~~~~~~~~

Total size: 213.1 MB, 1760382 sentences, https://f000.backblazeb2.com/file/malay-dataset/dumping/singlish/sg-news.txt

Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Singapore News,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malay-dataset/tree/master/dumping/singapore-news}}
   }

Manglish Text
-------------

Singlish is a mix of Chinese, Bahasa, Tamil and majority English, singaporean slang.

Random crawled from different singaporean websites and blogs.

Total size: 1.2 GB, 19870766 sentences.

Contributed by `brytjy <https://github.com/brytjy>`__.

download
~~~~~~~~

Total size: 1.2 GB, 19870766 sentences, https://f000.backblazeb2.com/file/malay-dataset/dumping/singlish/singlish.txt

Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Singlish Texts,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malay-dataset/tree/master/dumping/singlish-text}}
   }

Filter The Pile dedup
---------------------

Original repository at https://huggingface.co/datasets/EleutherAI/the_pile_deduplicated

download
~~~~~~~~

1. https://huggingface.co/datasets/malaysia-ai/dedup-text-dataset/resolve/main/the-pile-filtered.jsonl

Twitter Bahasa
--------------

Contact me personally to get full data.

Download
~~~~~~~~

1. last year,

577.5 MB, 10172726 sentences, https://f000.backblazeb2.com/file/malay-dataset/dumping/twitter/dumping-twitter-6-july-2019.json

2. 2020-02-22,

english, 136MB, https://f000.backblazeb2.com/file/malay-dataset/dumping/twitter/2020-02-22-twitter-dump-en.json

bahasa, 332MB, https://f000.backblazeb2.com/file/malay-dataset/dumping/twitter/2020-02-22-twitter-dump-in.json

3. 2020-02-22 - 2020-02-08,

english, 138MB, https://f000.backblazeb2.com/file/malay-dataset/dumping/twitter/2020-03-08-twitter-dump-en.json

bahasa, 357MB, https://f000.backblazeb2.com/file/malay-dataset/dumping/twitter/2020-03-08-twitter-dump-in.json

4. 2020-02-08, 2020-03-28,

english, 96MB, https://f000.backblazeb2.com/file/malay-dataset/dumping/twitter/2020-03-28-twitter-dump-en.json

bahasa, 261MB, https://f000.backblazeb2.com/file/malay-dataset/dumping/twitter/2020-03-28-twitter-dump-in.json

5. 2020-03-28 - 2020-04-12

english, 108.1MB, https://f000.backblazeb2.com/file/malay-dataset/dumping/twitter/2020-04-12-twitter-dump-en.json

bahasa, 323.3MB, https://f000.backblazeb2.com/file/malay-dataset/dumping/twitter/2020-04-12-twitter-dump-in.json

5. 2020-04-12 - 2020-04-22

english, 72.5MB, https://f000.backblazeb2.com/file/malay-dataset/dumping/twitter/2020-04-22-twitter-dump-en.json

bahasa, 261MB, https://f000.backblazeb2.com/file/malay-dataset/dumping/twitter/2020-04-22-twitter-dump-in.json

6. 2020-04-22 - 2020-05-02

english, 73.6MB, https://f000.backblazeb2.com/file/malay-dataset/dumping/twitter/2020-05-02-twitter-dump-en.json

bahasa, 219.2MB, https://f000.backblazeb2.com/file/malay-dataset/dumping/twitter/2020-05-02-twitter-dump-in.json

7. 2020-05-02 - 2020-05-11

english, 67.9MB, https://f000.backblazeb2.com/file/malay-dataset/dumping/twitter/2020-05-11-twitter-dump-en.json

bahasa, 213.4MB, https://f000.backblazeb2.com/file/malay-dataset/dumping/twitter/2020-05-11-twitter-dump-in.json

8. 2020-05-11 - 2020-05-31

english, 142.2MB, https://f000.backblazeb2.com/file/malay-dataset/dumping/twitter/2020-05-31-twitter-dump-en.json

bahasa, 386.6MB, https://f000.backblazeb2.com/file/malay-dataset/dumping/twitter/2020-05-31-twitter-dump-in.json

9. 2021-03-06 - 2021-04-21

bahasa, 533MB, https://f000.backblazeb2.com/file/malay-dataset/dumping/twitter/compiled-2021-03-06-twitter.tar

10. 2021-04-21 - 2021-06-06

bahasa, 778MB, https://f000.backblazeb2.com/file/malay-dataset/dumping/twitter/compiled-2021-04-21-twitter.tar

11. 2021-06-06 - 2021-07-23

bahasa, 1.3GB, https://f000.backblazeb2.com/file/malay-dataset/dumping/twitter/compiled-2021-06-06-twitter.tar

12. 2021-07-23 - 2022-06-08

bahasa, 593MB, https://f000.backblazeb2.com/file/malay-dataset/dumping/twitter/compiled-2022-06-08-twitter.tar

13. last snapshot, https://huggingface.co/mesolitica/snapshot-twitter-2022-09-03

- minimum timestamp, 2022-04-17T16:30:07.000Z
- maximum timestamp, 2022-09-03T09:23:52.000Z
- 7075025 rows
- full attributes

.. code:: json

   {
   "datetime": "2022-04-18T05:57:04",
   "datetime_gmt8": "2022-04-18T13:57:04",
   "data_text": "kekal halal kak https://t.co/YHKqszqPnS",
   "body": "kekal halal kak https://t.co/YHKqszqPnS",
   "screen_name": "Luke_Sebastian2",
   "followers_count": 10413,
   "friends_count": 72,
   "listed_count": 6,
   "favourites_count": 1494,
   "statuses_count": 948,
   "quoted_status_text": "NULL",
   "lang": "in",
   "retweet": "false",
   "retweet_text": "NULL",
   "retweet_text_full": "NULL",
   "retweet_count": 0,
   "retweet_detail": {},
   "quote_count": 0,
   "favorite_count": 0,
   "reply_count": 0,
   "id_str": "1515932406368202753",
   "tweet": {
   "created_at": "Mon Apr 18 05:57:04 +0000 2022",
   "id": 1515932406368202800,
   "id_str": "1515932406368202753",
   "text": "kekal halal kak😏🤫 https://t.co/YHKqszqPnS",
   "display_text_range": [
   0,
   17
   ],
   "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
   "truncated": false,
   "in_reply_to_status_id": null,
   "in_reply_to_status_id_str": null,
   "in_reply_to_user_id": null,
   "in_reply_to_user_id_str": null,
   "in_reply_to_screen_name": null,
   "user": {
   "id": 1431086333024374800,
   "id_str": "1431086333024374792",
   "name": "☄ʟᴜᴋᴇ",
   "screen_name": "Luke_Sebastian2",
   "location": "Malaysia",
   "url": "http://t.me/Luke_Alqamara",
   "description": "|𝟮𝟬🍰|⚤|📚𝗧𝗼𝗽|🇮🇩|📌🇲🇾|Law Student💼|•𝐤𝐞𝐤𝐚𝐬𝐢𝐡𝐤𝐮:@Trevor_Louise1•|Dm me for endorsement/Collab and rates also📩!|•don't forget to smile😊•",
   "translator_type": "none",
   "protected": false,
   "verified": false,
   "followers_count": 10413,
   "friends_count": 72,
   "listed_count": 6,
   "favourites_count": 1494,
   "statuses_count": 948,
   "created_at": "Fri Aug 27 02:49:28 +0000 2021",
   "utc_offset": null,
   "time_zone": null,
   "geo_enabled": true,
   "lang": null,
   "contributors_enabled": false,
   "is_translator": false,
   "profile_background_color": "F5F8FA",
   "profile_background_image_url": "",
   "profile_background_image_url_https": "",
   "profile_background_tile": false,
   "profile_link_color": "1DA1F2",
   "profile_sidebar_border_color": "C0DEED",
   "profile_sidebar_fill_color": "DDEEF6",
   "profile_text_color": "333333",
   "profile_use_background_image": true,
   "profile_image_url": "http://pbs.twimg.com/profile_images/1500850780823494658/snCdyeen_normal.jpg",
   "profile_image_url_https": "https://pbs.twimg.com/profile_images/1500850780823494658/snCdyeen_normal.jpg",
   "profile_banner_url": "https://pbs.twimg.com/profile_banners/1431086333024374792/1647061513",
   "default_profile": true,
   "default_profile_image": false,
   "following": null,
   "follow_request_sent": null,
   "notifications": null,
   "withheld_in_countries": []
   },
   "geo": null,
   "coordinates": null,
   "place": {
   "id": "7b02fbddf4d9f2c6",
   "url": "https://api.twitter.com/1.1/geo/id/7b02fbddf4d9f2c6.json",
   "place_type": "city",
   "name": "Kuala Lumpur City",
   "full_name": "Kuala Lumpur City, Kuala Lumpur Federal Territory",
   "country_code": "MY",
   "country": "Malaysia",
   "bounding_box": {
   "type": "Polygon",
   "coordinates": [
   [
   [
   101.668232,
   3.104906
   ],
   [
   101.668232,
   3.192155
   ],
   [
   101.742378,
   3.192155
   ],
   [
   101.742378,
   3.104906
   ]
   ]
   ]
   },
   "attributes": {}
   },
   "contributors": null,
   "is_quote_status": false,
   "quote_count": 0,
   "reply_count": 0,
   "retweet_count": 0,
   "favorite_count": 0,
   "entities": {
   "hashtags": [],
   "urls": [],
   "user_mentions": [],
   "symbols": [],
   "media": [
   {
   "id": 1515932334612107300,
   "id_str": "1515932334612107268",
   "indices": [
   18,
   41
   ],
   "additional_media_info": {
   "monetizable": false
   },
   "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1515932334612107268/pu/img/ak2K23DgNDDV-UCC.jpg",
   "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1515932334612107268/pu/img/ak2K23DgNDDV-UCC.jpg",
   "url": "https://t.co/YHKqszqPnS",
   "display_url": "pic.twitter.com/YHKqszqPnS",
   "expanded_url": "https://twitter.com/Luke_Sebastian2/status/1515932406368202753/video/1",
   "type": "photo",
   "sizes": {
   "thumb": {
   "w": 150,
   "h": 150,
   "resize": "crop"
   },
   "medium": {
   "w": 540,
   "h": 960,
   "resize": "fit"
   },
   "small": {
   "w": 383,
   "h": 680,
   "resize": "fit"
   },
   "large": {
   "w": 540,
   "h": 960,
   "resize": "fit"
   }
   }
   }
   ]
   },
   "extended_entities": {
   "media": [
   {
   "id": 1515932334612107300,
   "id_str": "1515932334612107268",
   "indices": [
   18,
   41
   ],
   "additional_media_info": {
   "monetizable": false
   },
   "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1515932334612107268/pu/img/ak2K23DgNDDV-UCC.jpg",
   "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1515932334612107268/pu/img/ak2K23DgNDDV-UCC.jpg",
   "url": "https://t.co/YHKqszqPnS",
   "display_url": "pic.twitter.com/YHKqszqPnS",
   "expanded_url": "https://twitter.com/Luke_Sebastian2/status/1515932406368202753/video/1",
   "type": "video",
   "video_info": {
   "aspect_ratio": [
   9,
   16
   ],
   "duration_millis": 15232,
   "variants": [
   {
   "bitrate": 632000,
   "content_type": "video/mp4",
   "url": "https://video.twimg.com/ext_tw_video/1515932334612107268/pu/vid/320x568/3gN3Udy0BrbU8HFr.mp4?tag=12"
   },
   {
   "content_type": "application/x-mpegURL",
   "url": "https://video.twimg.com/ext_tw_video/1515932334612107268/pu/pl/V6UZr3a49tZHwoia.m3u8?tag=12&container=fmp4"
   },
   {
   "bitrate": 950000,
   "content_type": "video/mp4",
   "url": "https://video.twimg.com/ext_tw_video/1515932334612107268/pu/vid/480x852/CpA6Jht3IZjzh75X.mp4?tag=12"
   },
   {
   "bitrate": 2176000,
   "content_type": "video/mp4",
   "url": "https://video.twimg.com/ext_tw_video/1515932334612107268/pu/vid/540x960/EdWN9mo8jIbA5PDM.mp4?tag=12"
   }
   ]
   },
   "sizes": {
   "thumb": {
   "w": 150,
   "h": 150,
   "resize": "crop"
   },
   "medium": {
   "w": 540,
   "h": 960,
   "resize": "fit"
   },
   "small": {
   "w": 383,
   "h": 680,
   "resize": "fit"
   },
   "large": {
   "w": 540,
   "h": 960,
   "resize": "fit"
   }
   }
   }
   ]
   },
   "favorited": false,
   "retweeted": false,
   "possibly_sensitive": false,
   "filter_level": "low",
   "lang": "in",
   "timestamp_ms": "1650261424997",
   "ignore_lang": true
   },
   "type": "search"
   }

- stream filtered by geo boundary,

::

   stream.filter(
   locations=[
   99.8568959909,
   0.8232449017,
   119.5213933664,
   7.2037547089,
   ]
   )


14. dedup, https://huggingface.co/datasets/mesolitica/twitter-dedup/resolve/main/dedup-twitter.jsonl

MS Wikipedia
------------

Script to download from wikipedia at https://huggingface.co/datasets/mesolitica/ms-wiki.

Simple preprocessing script at https://github.com/huseinzol05/malay-dataset/blob/master/pure-text/preprocessing-wiki.ipynb

download
~~~~~~~~

1. processed, last update 2019-07-06, 1663373 sentences, https://f000.backblazeb2.com/file/malay-dataset/dumping/wikipedia/dumping-wiki-6-july-2019.json

2. processed, last update 2019-07-20, 1303844 sentences, https://f000.backblazeb2.com/file/malay-dataset/dumping/wikipedia/dumping-wiki-20-july-2019.json

3. raw, last update 2020-03-06, 1748387 sentences, https://f000.backblazeb2.com/file/malay-dataset/wikidump1-raw.json

4. raw, last update 2022-05-22, from http://dumps.wikimedia.org/mswiki/latest/mswiki-latest-pages-articles.xml.bz2, https://huggingface.co/datasets/mesolitica/ms-wiki/resolve/main/wiki-2022-05-22-pages.tar

5. raw, last update 2022-05-22, from https://dumps.wikimedia.org/mswiki/latest/mswiki-latest-pages-meta-history.xml.bz2, https://f000.backblazeb2.com/file/malay-dataset/dumping/wikipedia/wiki-2022-05-22-meta.tar

6. raw + dedup, last update 2023-06-10, from http://dumps.wikimedia.org/mswiki/latest/mswiki-latest-pages-articles.xml.bz2, https://huggingface.co/datasets/mesolitica/wikipedia/resolve/main/wikipedia-2023-06-10.jsonl
