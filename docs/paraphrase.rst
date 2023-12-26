paraphrase
==========

Ayat Aktif to Ayat Pasif
------------------------

Generate using ChatGPT4, originally from https://soalanspm.com/ayat-aktif-dan-ayat-pasif/

download
~~~~~~~~

1. https://huggingface.co/datasets/mesolitica/ayat-aktif-pasif-instructions/resolve/main/synthetic-ayat-aktif-pasif.jsonl

Funpedia
--------

Extract from https://github.com/facebookresearch/ParlAI/tree/master/parlai/tasks/funpedia

Original paper, https://arxiv.org/abs/1705.06476

download
~~~~~~~~

1. https://huggingface.co/datasets/mesolitica/translated-funpedia/raw/main/funpedia-test.json
2. https://huggingface.co/datasets/mesolitica/translated-funpedia/resolve/main/funpedia-train.json
3. https://huggingface.co/datasets/mesolitica/translated-funpedia/raw/main/funpedia-valid.json

Citation
~~~~~~~~

.. code:: bibtex

   @misc{miller2018parlai,
   title={ParlAI: A Dialog Research Software Platform},
   author={Alexander H. Miller and Will Feng and Adam Fisch and Jiasen Lu and Dhruv Batra and Antoine Bordes and Devi Parikh and Jason Weston},
   year={2018},
   eprint={1705.06476},
   archivePrefix={arXiv},
   primaryClass={cs.CL}
   }

MSCOCO
------

Extract from MS COCO Captions, https://github.com/tensorflow/tensor2tensor/blob/master/tensor2tensor/data_generators/paraphrase_ms_coco.py

Original paper, http://arxiv.org/abs/1405.0312

download
~~~~~~~~

1. https://f000.backblazeb2.com/file/malay-dataset/paraphrase/translated-paraphrase.json

Citation
~~~~~~~~

.. code:: bibtex

   @article{DBLP:journals/corr/LinMBHPRDZ14,
   author    = {Tsung{-}Yi Lin and
   Michael Maire and
   Serge J. Belongie and
   Lubomir D. Bourdev and
   Ross B. Girshick and
   James Hays and
   Pietro Perona and
   Deva Ramanan and
   Piotr Doll{\'{a}}r and
   C. Lawrence Zitnick},
   title     = {Microsoft {COCO:} Common Objects in Context},
   journal   = {CoRR},
   volume    = {abs/1405.0312},
   year      = {2014},
   url       = {http://arxiv.org/abs/1405.0312},
   archivePrefix = {arXiv},
   eprint    = {1405.0312},
   timestamp = {Mon, 13 Aug 2018 16:48:13 +0200},
   biburl    = {https://dblp.org/rec/journals/corr/LinMBHPRDZ14.bib},
   bibsource = {dblp computer science bibliography, https://dblp.org}
   }

ParaSCI
-------

Original website, https://github.com/dqxiu/ParaSCI

Original paper, https://arxiv.org/abs/2101.08382

Download
~~~~~~~~

ParaSCI-ACL
^^^^^^^^^^^

1. https://huggingface.co/datasets/mesolitica/translated-paraSCI/raw/main/parasci-acl-test.json
2. https://huggingface.co/datasets/mesolitica/translated-paraSCI/resolve/main/parasci-acl-train.json
3. https://huggingface.co/datasets/mesolitica/translated-paraSCI/raw/main/parasci-acl-val.json

ParaSCI-arXiv
^^^^^^^^^^^^^

1. https://huggingface.co/datasets/mesolitica/translated-paraSCI/raw/main/parasci-arxiv-test.json
2. https://huggingface.co/datasets/mesolitica/translated-paraSCI/resolve/main/parasci-arxiv-train.json
3. https://huggingface.co/datasets/mesolitica/translated-paraSCI/raw/main/parasci-arxiv-val.json

Citation
~~~~~~~~

.. code:: bibtex

   @misc{dong2021parasci,
   title={ParaSCI: A Large Scientific Paraphrase Dataset for Longer Paraphrase Generation},
   author={Qingxiu Dong and Xiaojun Wan and Yue Cao},
   year={2021},
   eprint={2101.08382},
   archivePrefix={arXiv},
   primaryClass={cs.CL}
   }

PAWS
----

Original website, https://github.com/google-research-datasets/paws

Original paper, https://arxiv.org/abs/1904.01130

Download
~~~~~~~~

1. https://huggingface.co/datasets/mesolitica/translated-PAWS/raw/main/paws-dev.json
2. https://huggingface.co/datasets/mesolitica/translated-PAWS/raw/main/paws-test.json
3. https://huggingface.co/datasets/mesolitica/translated-PAWS/resolve/main/paws-train.json

Citation
~~~~~~~~

.. code:: bibtex

   @misc{zhang2019paws,
   title={PAWS: Paraphrase Adversaries from Word Scrambling},
   author={Yuan Zhang and Jason Baldridge and Luheng He},
   year={2019},
   eprint={1904.01130},
   archivePrefix={arXiv},
   primaryClass={cs.CL}
   }

Semisupervised Academia.edu
---------------------------

Use `Malaya T5-Base Paraphrase model <https://malaya.readthedocs.io/en/latest/Paraphrase.html#load-t5-models>`__ to paraphrase https://github.com/huseinzol05/Malay-Dataset#academia-pdf

download
~~~~~~~~

1. semisupervised-paraphrase-pdf.json, https://f000.backblazeb2.com/file/malay-dataset/paraphrase/semisupervised-paraphrase-pdf.json

Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Semisupervised Academia.edu Paraphrases using T5-Bahasa,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malay-dataset/tree/master/paraphrase/semisupervised-academia}}
   }

Semisupervised News
-------------------

Use `Malaya T5-Base Paraphrase model <https://malaya.readthedocs.io/en/latest/Paraphrase.html#load-t5-models>`__ to paraphrase https://github.com/huseinzol05/Malay-Dataset#crawled-news

download
~~~~~~~~

1. semisupervised-news-paraphrase.json, https://f000.backblazeb2.com/file/malay-dataset/paraphrase/semisupervised-news-paraphrase.json

Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Semisupervised Bahasa News Paraphrases using T5-Bahasa,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malay-dataset/tree/master/paraphrase/semisupervised-academia}}
   }

Semisupervised Wikipedia
------------------------

Use `Malaya T5-Base Paraphrase model <https://malaya.readthedocs.io/en/latest/Paraphrase.html#load-t5-models>`__ to paraphrase https://github.com/huseinzol05/Malay-Dataset#wikipedia

download
~~~~~~~~

1. semisupervised-wiki-paraphrase.json, https://f000.backblazeb2.com/file/malay-dataset/paraphrase/semisupervised-wiki-paraphrase.json

Citation
~~~~~~~~

.. code:: bibtex

   @misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Semisupervised Bahasa Wikipedia Paraphrases using T5-Bahasa,
   author = {Husein, Zolkepli},
   title = {Malay-Dataset},
   year = {2018},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/huseinzol05/malay-dataset/tree/master/paraphrase/semisupervised-academia}}
   }
