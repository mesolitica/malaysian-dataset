translation
===========

ChatGPT 3.5 Noisy Translation b.cari.com.my
-------------------------------------------

download
~~~~~~~~

1. https://huggingface.co/datasets/mesolitica/chatgpt-b.cari.com.my-translation/resolve/main/data.jsonl
2. https://huggingface.co/datasets/mesolitica/chatgpt-b.cari.com.my-translation/resolve/main/processed-b.cari.com.my.jsonl

ChatGPT 3.5 Noisy Translation c.cari.com.my
-------------------------------------------

download
~~~~~~~~

1. https://huggingface.co/datasets/mesolitica/chatgpt-c.cari.com.my-noisy-translation/resolve/main/filtered.jsonl
2. https://huggingface.co/datasets/mesolitica/chatgpt-c.cari.com.my-noisy-translation/resolve/main/processed-c.cari.com.my.jsonl

ChatGPT 3.5 Noisy Translation Facebook
--------------------------------------

download
~~~~~~~~

1. https://huggingface.co/datasets/mesolitica/chatgpt-noisy-facebook-translation/resolve/main/processed-facebook.jsonl

ChatGPT 3.5 Noisy Translation IIUM Confession
---------------------------------------------

download
~~~~~~~~

1. https://huggingface.co/datasets/mesolitica/chatgpt-iium-confession-noisy-translation/resolve/main/processed-iium-confession.jsonl

ChatGPT 3.5 Noisy Translation Manglish
--------------------------------------

download
~~~~~~~~

1. https://huggingface.co/datasets/mesolitica/chatgpt-manglish-noisy-translation/resolve/main/filtered-manglish.jsonl
2. https://huggingface.co/datasets/mesolitica/chatgpt-manglish-noisy-translation/resolve/main/process-manglish.jsonl

ChatGPT 3.5 NLLB Banjarese
--------------------------

download
~~~~~~~~

1. https://huggingface.co/datasets/mesolitica/chatgpt-bjn_Latn-translation/resolve/main/translated-bjn_Latn.json
2. https://huggingface.co/datasets/mesolitica/chatgpt-bjn_Latn-translation/resolve/main/process-bjn-Latn.jsonl

ChatGPT 3.5 Noisy Translation Twitter
-------------------------------------

download
~~~~~~~~

1. https://huggingface.co/datasets/mesolitica/chatgpt-twitter-noisy-translation/resolve/main/processed-twitter.jsonl

ChatGPT 4 Noisy Translation Twitter to local dialect
----------------------------------------------------

download
~~~~~~~~

1. https://huggingface.co/datasets/mesolitica/chatgpt4-noisy-translation-twitter-dialect/resolve/main/negeri-kelantan.jsonl
2. https://huggingface.co/datasets/mesolitica/chatgpt4-noisy-translation-twitter-dialect/resolve/main/negeri-utara.jsonl

Alignment
---------

Prepare alignment for EN-MS using `eflomal <https://github.com/robertostling/eflomal>`__.

Download
~~~~~~~~

1. EN, https://f000.backblazeb2.com/file/malay-dataset/translation/en-ms-alignment/EN
2. MS, https://f000.backblazeb2.com/file/malay-dataset/translation/en-ms-alignment/MS
3. fwd, https://f000.backblazeb2.com/file/malay-dataset/translation/en-ms-alignment/fwd
4. rev, https://f000.backblazeb2.com/file/malay-dataset/translation/en-ms-alignment/rev
5. align.priors, https://f000.backblazeb2.com/file/malay-dataset/translation/en-ms-alignment/align.priors

how-to
~~~~~~

1. Build https://github.com/robertostling/eflomal,

.. code:: bash

   make
   make INSTALLDIR=~/.local/bin install
   python3 setup.py install --user

2. Align EN-MS text,

.. code:: bash

   python3 test.py

FLORES-200 Evaluation set
-------------------------

Google Translate EN to MS
-------------------------

Translate using https://github.com/Songkeys/Translateer

download
~~~~~~~~

Full list at https://huggingface.co/datasets/mesolitica/google-translate-english-news/tree/main

Facebook
--------

Translate using https://github.com/Songkeys/Translateer

download
~~~~~~~~

Full list at https://huggingface.co/datasets/mesolitica/google-translate-malaysian-facebook

Google Translate filtered Common Crawl
--------------------------------------

Translate using https://github.com/Songkeys/Translateer

download
~~~~~~~~

Full list at https://huggingface.co/datasets/mesolitica/google-translate-filtered-common-crawl

Google Translate Malaysia Parliament
------------------------------------

Translate using https://github.com/Songkeys/Translateer

download
~~~~~~~~

1. https://huggingface.co/datasets/mesolitica/google-translate-malaysia-hansard/resolve/main/hansard.jsonl00.splitted.requested
2. https://huggingface.co/datasets/mesolitica/google-translate-malaysia-hansard/resolve/main/hansard.jsonl01.splitted.requested
3. https://huggingface.co/datasets/mesolitica/google-translate-malaysia-hansard/resolve/main/hansard.jsonl02.splitted.requested

Google Translate Malay News
---------------------------

download
~~~~~~~~

Full list at https://huggingface.co/datasets/mesolitica/google-translate-IIUM-confession/tree/main

Google Translate Malay News
---------------------------

download
~~~~~~~~

Full list at https://huggingface.co/datasets/mesolitica/google-translate-malay-news/tree/main

Google Translate Malaysian PDF
------------------------------

download
~~~~~~~~

1. https://huggingface.co/datasets/mesolitica/google-translate-malaysian-pdf/resolve/main/combine.jsonl

Google Translate MS-ID
----------------------

Translate using https://github.com/Songkeys/Translateer

download
~~~~~~~~

Full list at https://huggingface.co/datasets/mesolitica/google-translate-ms-id

Google Translate MS-JW
----------------------

Translate using https://github.com/Songkeys/Translateer

download
~~~~~~~~

Full list at https://huggingface.co/datasets/mesolitica/google-translate-ms-jw

Google Translate MS-PA
----------------------

Translate using https://github.com/Songkeys/Translateer

download
~~~~~~~~

Full list at https://huggingface.co/datasets/mesolitica/google-translate-ms-pa

Google Translate MS-TA
----------------------

Translate using https://github.com/Songkeys/Translateer

download
~~~~~~~~

Full list at https://huggingface.co/datasets/mesolitica/google-translate-ms-ta

Twitter
-------

Translate using https://github.com/Songkeys/Translateer

download
~~~~~~~~

Full list at https://huggingface.co/datasets/mesolitica/google-translate-malaysian-twitter/tree/main

IIUM-Confession
---------------

Translate using https://github.com/Songkeys/Translateer

download
~~~~~~~~

1. https://huggingface.co/datasets/mesolitica/google-translate-IIUM-confession/resolve/main/clean-iium00.splitted.requested
2. https://huggingface.co/datasets/mesolitica/google-translate-IIUM-confession/resolve/main/clean-iium01.splitted.requested
3. https://huggingface.co/datasets/mesolitica/google-translate-IIUM-confession/resolve/main/clean-iium02.splitted.requested
4. https://huggingface.co/datasets/mesolitica/google-translate-IIUM-confession/resolve/main/clean-iium03.splitted.requested
5. https://huggingface.co/datasets/mesolitica/google-translate-IIUM-confession/resolve/main/clean-iium04.splitted.requested
6. https://huggingface.co/datasets/mesolitica/google-translate-IIUM-confession/resolve/main/clean-iium05.splitted.requested
7. https://huggingface.co/datasets/mesolitica/google-translate-IIUM-confession/resolve/main/clean-iium06.splitted.requested
8. https://huggingface.co/datasets/mesolitica/google-translate-IIUM-confession/resolve/main/clean-iium07.splitted.requested
9. https://huggingface.co/datasets/mesolitica/google-translate-IIUM-confession/resolve/main/clean-iium08.splitted.requested

Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Google Translate IIUM Confession,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malay-dataset/tree/master/translation/iium-confession}}
   }

LASER for eng_Latn-zsm_Latn
---------------------------

Original dataset at https://github.com/facebookresearch/LASER/tree/main/data/nllb200#data

**Update, AllenNLP released NLLB dataset at https://huggingface.co/datasets/allenai/nllb, https://storage.googleapis.com/allennlp-data-bucket/nllb/eng_Latn-zsm_Latn.gz**.

how-to
~~~~~~

1. Install dependencies,

::

   sudo apt-get install libcurl4-openssl-dev
   git clone https://github.com/kpuatfb/preprocess.git
   cd preprocess
   git checkout wet
   mkdir build
   cd build
   git clone https://github.com/Cyan4973/xxHash
   mkdir xxHash/build
   cd xxHash/build
   cmake ../cmake_unofficial
   cmake --build .
   cd ../..
   cmake ..
   make -j4
   git clone https://github.com/facebookresearch/LASER.git
   cd LASER/utils
   pip3 install -e . --user
   cd ../..


2. Download dataset from https://github.com/facebookresearch/LASER/tree/main/data/nllb200#data, i choose `eng_Latn-zsm_Latn <https://dl.fbaipublicfiles.com/nllb/data/eng_Latn-zsm_Latn.meta.v1.xz>`__.

3. Run LASER,

.. code:: bash

   xzcat eng_Latn-zsm_Latn.meta.v1.xz | egrep ^crawl-data | ~/preprocess/build/bin/wet_lines | python3 ~/preprocess/build/LASER/utils/src/cleaner_splitter.py > eng_Latn-zsm_Latn

how-to distribute
~~~~~~~~~~~~~~~~~

**Required redis**.

1. filter metadata,

::

   xzcat eng_Latn-zsm_Latn.meta.v1.xz | egrep ^crawl-data > eng_Latn-zsm_Latn.meta
   mkdir splitted
   cd splitted
   split -l 1000000 -d --additional-suffix=.split ../eng_Latn-zsm_Latn.meta eng_Latn-zsm_Latn.meta


2. Groupby sha1 and parapgraphs, `gather-warc.ipynb <gather-warc.ipynb>`__.

3. Split JSONL,

.. code:: bash

   mkdir splitted-jsonl
   cd splitted-jsonl
   split -l 200000 -d --additional-suffix=.split ../warcs-eng_Latn-zsm_Latn.jsonl warcs-eng_Latn-zsm_Latn.jsonl

4. Run `distribute-laser-nllb200.ipynb <distribute-laser-nllb200.ipynb>`__ for each splitted files.

download
~~~~~~~~

Filtered if laser score >= 1.07, `prepare-eng_Latn-zsm_Latn.ipynb <prepare-eng_Latn-zsm_Latn>`__.

1. https://huggingface.co/datasets/mesolitica/filtered-eng_Latn-zsm_Latn/resolve/main/eng_Latn-zsm_Latn.left
2. https://huggingface.co/datasets/mesolitica/filtered-eng_Latn-zsm_Latn/resolve/main/eng_Latn-zsm_Latn.right

Citation
~~~~~~~~

.. code:: bibtex

   @article{DBLP:journals/corr/abs-1812-10464,
   author    = {Mikel Artetxe and
   Holger Schwenk},
   title     = {Massively Multilingual Sentence Embeddings for Zero-Shot Cross-Lingual
   Transfer and Beyond},
   journal   = {CoRR},
   volume    = {abs/1812.10464},
   year      = {2018},
   url       = {http://arxiv.org/abs/1812.10464},
   eprinttype = {arXiv},
   eprint    = {1812.10464},
   timestamp = {Wed, 02 Jan 2019 14:40:18 +0100},
   biburl    = {https://dblp.org/rec/journals/corr/abs-1812-10464.bib},
   bibsource = {dblp computer science bibliography, https://dblp.org}
   }

Local EN to MS Subtitles
------------------------

Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Local EN to MS Subtitles,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malay-dataset/tree/master/translation/local-movies-subtitle}}
   }

Google Translate EN to MS for longer texts
------------------------------------------

how-to
~~~~~~

prefix, https://f000.backblazeb2.com/file/malay-dataset/translation/long-text/

1. long-text-0.json.translated.json
2. long-text-100000.json.translated.json
3. long-text-1000000.json.translated.json
4. long-text-200000.json.translated.json
5. long-text-300000.json.translated.json
6. long-text-400000.json.translated.json
7. long-text-500000.json.translated.json
8. long-text-600000.json.translated.json
9. long-text-700000.json.translated.json
10. long-text-800000.json.translated.json
11. long-text-900000.json.translated.json
12. long-text-1100000.json.translated.json
13. long-text-1200000.json.translated.json
14. long-text-1300000.json.translated.json
15. long-text-1400000.json.translated.json
16. long-text-1500000.json.translated.json
17. long-text-1600000.json.translated.json

Alignment
---------

Prepare alignment for MS-EN using `eflomal <https://github.com/robertostling/eflomal>`__.

Download
~~~~~~~~

1. fwd, https://f000.backblazeb2.com/file/malay-dataset/ms-en-alignment/fwd
2. rev, https://f000.backblazeb2.com/file/malay-dataset/ms-en-alignment/rev
3. align.priors, https://f000.backblazeb2.com/file/malay-dataset/ms-en-alignment/align.priors

how-to
~~~~~~

1. Build https://github.com/robertostling/eflomal,

.. code:: bash

   make
   make INSTALLDIR=~/.local/bin install
   python3 setup.py install --user

2. Align MS-EN text, `prepare-ms-en-fwd-rev.ipynb <prepare-ms-en-fwd-rev.ipynb>`__.

NLLB EN-MS
----------

Original page, https://github.com/facebookresearch/LASER/tree/main/data/nllb200

Apply filter on NLLB ``eng_Latn-zsm_Latn`` NLLB pair dataset.

download
~~~~~~~~

1. https://huggingface.co/datasets/mesolitica/filtered-eng_Latn-zsm_Latn/resolve/main/eng_Latn-zsm_Latn.left
2. https://huggingface.co/datasets/mesolitica/filtered-eng_Latn-zsm_Latn/resolve/main/eng_Latn-zsm_Latn.right

Citation
~~~~~~~~

.. code:: bibtex

   @misc{https://doi.org/10.48550/arxiv.2207.04672,
   doi = {10.48550/ARXIV.2207.04672},

   url = {https://arxiv.org/abs/2207.04672},

   author = {{NLLB Team} and Costa-jussà, Marta R. and Cross, James and Çelebi, Onur and Elbayad, Maha and Heafield, Kenneth and Heffernan, Kevin and Kalbassi, Elahe and Lam, Janice and Licht, Daniel and Maillard, Jean and Sun, Anna and Wang, Skyler and Wenzek, Guillaume and Youngblood, Al and Akula, Bapi and Barrault, Loic and Gonzalez, Gabriel Mejia and Hansanti, Prangthip and Hoffman, John and Jarrett, Semarley and Sadagopan, Kaushik Ram and Rowe, Dirk and Spruit, Shannon and Tran, Chau and Andrews, Pierre and Ayan, Necip Fazil and Bhosale, Shruti and Edunov, Sergey and Fan, Angela and Gao, Cynthia and Goswami, Vedanuj and Guzmán, Francisco and Koehn, Philipp and Mourachko, Alexandre and Ropers, Christophe and Saleem, Safiyyah and Schwenk, Holger and Wang, Jeff},

   keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences, I.2.7, 68T50},

   title = {No Language Left Behind: Scaling Human-Centered Machine Translation},

   publisher = {arXiv},

   year = {2022},

   copyright = {Creative Commons Attribution Share Alike 4.0 International}
   }

Noisy EN-MS augmentation
~~~~~~~~~~~~~~~~~~~~~~~~

Augment EN-MS dataset.

download
~~~~~~~~

1. https://huggingface.co/datasets/mesolitica/noisy-en-ms-augmentation/resolve/main/augmented-en-ms-v1.json
2. https://huggingface.co/datasets/mesolitica/noisy-en-ms-augmentation/resolve/main/augmented-en-ms-v2.json
3. https://huggingface.co/datasets/mesolitica/noisy-en-ms-augmentation/resolve/main/augmented-en-ms-v2-part2.json
4. https://huggingface.co/datasets/mesolitica/noisy-en-ms-augmentation/resolve/main/augmented-en-ms-v2-part3.json 5.https://huggingface.co/datasets/mesolitica/noisy-en-ms-augmentation/resolve/main/augmented-en-ms-v3.json

Noisy MS-EN augmentation
~~~~~~~~~~~~~~~~~~~~~~~~

Augment MS-EN dataset.

download
~~~~~~~~

1. https://huggingface.co/datasets/mesolitica/noisy-ms-en-augmentation/resolve/main/augmented-ms-en-1.json
2. https://huggingface.co/datasets/mesolitica/noisy-ms-en-augmentation/resolve/main/augmented-ms-en-2.json
3. https://huggingface.co/datasets/mesolitica/noisy-ms-en-augmentation/resolve/main/augmented-ms-en-3.json
4. https://huggingface.co/datasets/mesolitica/noisy-ms-en-augmentation/resolve/main/augmented-ms-en-v2.json
5. https://huggingface.co/datasets/mesolitica/noisy-ms-en-augmentation/resolve/main/augmented-ms-en-v3.json
6. https://huggingface.co/datasets/mesolitica/noisy-ms-en-augmentation/resolve/main/augmented-ms-en-test.json

OPUS
----

download
~~~~~~~~

1. gnome, https://f000.backblazeb2.com/file/malay-dataset/translation/opus/gnome-ms-en.json
2. kde4, https://f000.backblazeb2.com/file/malay-dataset/translation/opus/kde4-ms-en.json
3. opensubtitle, https://f000.backblazeb2.com/file/malay-dataset/translation/opus/opensubtitle-ms-en.json
4. qed, https://f000.backblazeb2.com/file/malay-dataset/translation/opus/qed-ms-en.json
5. tanzil, https://f000.backblazeb2.com/file/malay-dataset/translation/opus/tanzil-ms-en.json
6. ubuntu, https://f000.backblazeb2.com/file/malay-dataset/translation/opus/ubuntu-ms-en.json

Citation
~~~~~~~~

.. code:: bibtex

   @InProceedings{TIEDEMANN12.463,
   author = {Jörg Tiedemann},
   title = {Parallel Data, Tools and Interfaces in OPUS},
   booktitle = {Proceedings of the Eight International Conference on Language Resources and Evaluation (LREC'12)},
   year = {2012},
   month = {may},
   date = {23-25},
   address = {Istanbul, Turkey},
   editor = {Nicoletta Calzolari (Conference Chair) and Khalid Choukri and Thierry Declerck and Mehmet Ugur Dogan and Bente Maegaard and Joseph Mariani and Jan Odijk and Stelios Piperidis},
   publisher = {European Language Resources Association (ELRA)},
   isbn = {978-2-9517408-7-7},
   language = {english}
   }
