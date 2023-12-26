normalization
=============

IIUM Confession
---------------

text -> google translate EN -> google translate MS.

download
~~~~~~~~

1. https://huggingface.co/datasets/mesolitica/IIUM-Confession-abstractive-normalization/resolve/main/clean-iium00.splitted.requested.ms-requested
2. https://huggingface.co/datasets/mesolitica/IIUM-Confession-abstractive-normalization/resolve/main/clean-iium01.splitted.requested.ms-requested
3. https://huggingface.co/datasets/mesolitica/IIUM-Confession-abstractive-normalization/resolve/main/clean-iium02.splitted.requested.ms-requested
4. https://huggingface.co/datasets/mesolitica/IIUM-Confession-abstractive-normalization/resolve/main/clean-iium03.splitted.requested.ms-requested
5. https://huggingface.co/datasets/mesolitica/IIUM-Confession-abstractive-normalization/resolve/main/clean-iium04.splitted.requested.ms-requested
6. https://huggingface.co/datasets/mesolitica/IIUM-Confession-abstractive-normalization/resolve/main/clean-iium05.splitted.requested.ms-requested
7. https://huggingface.co/datasets/mesolitica/IIUM-Confession-abstractive-normalization/resolve/main/clean-iium06.splitted.requested.ms-requested
8. https://huggingface.co/datasets/mesolitica/IIUM-Confession-abstractive-normalization/resolve/main/clean-iium07.splitted.requested.ms-requested
9. https://huggingface.co/datasets/mesolitica/IIUM-Confession-abstractive-normalization/resolve/main/clean-iium07.splitted.requested.ms-requested

Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, IIUM Confession abstractive normalization using Google Translate,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malay-dataset/tree/master/normalization/iium-confession}}
   }

Rumi-to-Jawi
------------

Originally from https://www.ejawi.net/converterV2.php?go=rumi

download
~~~~~~~~

1. Wikipedia, single words, https://f000.backblazeb2.com/file/malay-dataset/normalization/rumi-jawi/wikipedia-1word.json

2. Wikipedia, random windows between 2-6 words, https://huggingface.co/datasets/mesolitica/rumi-jawi/resolve/main/wikipedia-windows.json

3. News, random windows between 2-6 words, https://huggingface.co/datasets/mesolitica/rumi-jawi/resolve/main/news-windows.json

4. Full news, random windows between 10-20 words, train set, JSONL format, https://huggingface.co/datasets/mesolitica/rumi-jawi/resolve/main/jawi-rumi-news-full.train

5. Full news, random windows between 10-20 words, test set, JSONL format, https://huggingface.co/datasets/mesolitica/rumi-jawi/resolve/main/jawi-rumi-news-full.test

Wikipedia
^^^^^^^^^

Slide random between 20 and 200 words.

1. https://huggingface.co/datasets/mesolitica/rumi-jawi/resolve/main/wiki-rumi-jawi-0.jsonl
2. https://huggingface.co/datasets/mesolitica/rumi-jawi/resolve/main/wiki-rumi-jawi-1.jsonl
3. https://huggingface.co/datasets/mesolitica/rumi-jawi/resolve/main/wiki-rumi-jawi-2.jsonl
4. https://huggingface.co/datasets/mesolitica/rumi-jawi/resolve/main/wiki-rumi-jawi-3.jsonl
5. https://huggingface.co/datasets/mesolitica/rumi-jawi/resolve/main/wiki-rumi-jawi-4.jsonl
6. https://huggingface.co/datasets/mesolitica/rumi-jawi/resolve/main/wiki-rumi-jawi-5.jsonl
7. https://huggingface.co/datasets/mesolitica/rumi-jawi/resolve/main/wiki-rumi-jawi-6.jsonl
8. https://huggingface.co/datasets/mesolitica/rumi-jawi/resolve/main/wiki-rumi-jawi-7.jsonl
9. https://huggingface.co/datasets/mesolitica/rumi-jawi/resolve/main/wiki-rumi-jawi-8.jsonl
10. https://huggingface.co/datasets/mesolitica/rumi-jawi/resolve/main/wiki-rumi-jawi-9.jsonl

Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Rumi-to-Jawi Dataset,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malay-dataset/tree/master/normalization/rumi-jawi}}
   }

Stemming and Lemmatization
--------------------------

download
~~~~~~~~

1. `stem.zip <stem.zip>`__
2. https://f000.backblazeb2.com/file/malay-dataset/wiki-stem.json
3. https://huggingface.co/datasets/mesolitica/stemming/resolve/main/train_stem.json
4. https://huggingface.co/datasets/mesolitica/stemming/resolve/main/test_stem.json
5. https://huggingface.co/datasets/mesolitica/stemming/resolve/main/train_noisy_stem.json
6. https://huggingface.co/datasets/mesolitica/stemming/resolve/main/test_noisy_stem.json

Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Stemming and Lemmatization Dataset,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malay-dataset/tree/master/normalization/stemmer}}
   }

Normalization Twitter
---------------------

Normalize twitter using malaya normalization lexicon based.

Download
~~~~~~~~

1. https://f000.backblazeb2.com/file/malay-dataset/normalization/twitter/normalized.json
