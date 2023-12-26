knowledge-graph
===============

WN11
----

Originally from https://github.com/yao8839836/kg-bert/tree/master/data/WN11

ChatGPT KG generation
---------------------

download
~~~~~~~~

1. https://huggingface.co/datasets/mesolitica/chatgpt-kg-triplets/resolve/main/kg-astroawani.jsonl
2. https://huggingface.co/datasets/mesolitica/chatgpt-kg-triplets/resolve/main/kg-astroawani.translated.jsonl

ChatGPT KG generation
---------------------

download
~~~~~~~~

1. https://huggingface.co/datasets/mesolitica/chatgpt-kg-triplets/resolve/main/kg-paragraph-wikipedia.jsonl
2. https://huggingface.co/datasets/mesolitica/chatgpt-kg-triplets/resolve/main/kg-paragraph-wikipedia.translated.jsonl

CODEX
-----

Original website, https://github.com/tsafavi/codex

download
~~~~~~~~

1. https://f000.backblazeb2.com/file/malay-dataset/knowledge-graph/codex/codex-entities.json.translate
2. https://f000.backblazeb2.com/file/malay-dataset/knowledge-graph/codex/codex-relations.json.translate
3. https://f000.backblazeb2.com/file/malay-dataset/knowledge-graph/codex/codex-l.tar.gz
4. https://f000.backblazeb2.com/file/malay-dataset/knowledge-graph/codex/codex-m.tar.gz
5. https://f000.backblazeb2.com/file/malay-dataset/knowledge-graph/codex/codex-s.tar.gz

Citation
~~~~~~~~

.. code:: bibtex

   @misc{safavi2020codex,
   title={CoDEx: A Comprehensive Knowledge Graph Completion Benchmark},
   author={Tara Safavi and Danai Koutra},
   year={2020},
   eprint={2009.07810},
   archivePrefix={arXiv},
   primaryClass={cs.CL}
   }

DBpedia500
----------

Original website, https://github.com/tsafavi/codex

download
~~~~~~~~

1. https://f000.backblazeb2.com/file/malay-dataset/knowledge-graph/dbpedia500/dbpedia500.tar.gz

Citation
~~~~~~~~

.. code:: bibtex

   Shi, B., & Weninger, T. (2018). Open-World Knowledge Graph Completion. Proceedings of the AAAI Conference on Artificial Intelligence, 32(1). Retrieved from https://ojs.aaai.org/index.php/AAAI/article/view/11535

FB13
----

Originally from https://github.com/yao8839836/kg-bert/tree/master/data/FB13

FB15k
-----

Originally from https://github.com/yao8839836/kg-bert/tree/master/data/FB15K

KELM
----

Original website, https://github.com/google-research-datasets/KELM-corpus

Original paper, https://arxiv.org/abs/2010.12688

download
~~~~~~~~

Entire dataset can download at https://huggingface.co/datasets/mesolitica/translated-KELM/tree/main

Citation
~~~~~~~~

.. code:: bibtex

   @article{DBLP:journals/corr/abs-2010-12688,
   author    = {Oshin Agarwal and
   Heming Ge and
   Siamak Shakeri and
   Rami Al{-}Rfou},
   title     = {Large Scale Knowledge Graph Based Synthetic Corpus Generation for
   Knowledge-Enhanced Language Model Pre-training},
   journal   = {CoRR},
   volume    = {abs/2010.12688},
   year      = {2020},
   url       = {https://arxiv.org/abs/2010.12688},
   archivePrefix = {arXiv},
   eprint    = {2010.12688},
   timestamp = {Mon, 02 Nov 2020 18:17:09 +0100},
   biburl    = {https://dblp.org/rec/journals/corr/abs-2010-12688.bib},
   bibsource = {dblp computer science bibliography, https://dblp.org}
   }

REBEL
-----

Original website, https://github.com/Babelscape/rebel

Original paper, https://github.com/Babelscape/rebel/blob/main/docs/EMNLP_2021_REBEL__Camera_Ready_.pdf

download
~~~~~~~~

Entire dataset can download at https://huggingface.co/datasets/mesolitica/translated-REBEL/tree/main

Citation
~~~~~~~~

.. code:: bibtex

   @inproceedings{huguet-cabot-navigli-2021-rebel-relation,
   title = "{REBEL}: Relation Extraction By End-to-end Language generation",
   author = "Huguet Cabot, Pere-Llu{\'\i}s  and
   Navigli, Roberto",
   booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2021",
   month = nov,
   year = "2021",
   address = "Punta Cana, Dominican Republic",
   publisher = "Association for Computational Linguistics",
   url = "https://aclanthology.org/2021.findings-emnlp.204",
   pages = "2370--2381",
   abstract = "Extracting relation triplets from raw text is a crucial task in Information Extraction, enabling multiple applications such as populating or validating knowledge bases, factchecking, and other downstream tasks. However, it usually involves multiple-step pipelines that propagate errors or are limited to a small number of relation types. To overcome these issues, we propose the use of autoregressive seq2seq models. Such models have previously been shown to perform well not only in language generation, but also in NLU tasks such as Entity Linking, thanks to their framing as seq2seq tasks. In this paper, we show how Relation Extraction can be simplified by expressing triplets as a sequence of text and we present REBEL, a seq2seq model based on BART that performs end-to-end relation extraction for more than 200 different relation types. We show our model{'}s flexibility by fine-tuning it on an array of Relation Extraction and Relation Classification benchmarks, with it attaining state-of-the-art performance in most of them.",
   }

TEKGEN
------

Original website, https://github.com/google-research-datasets/KELM-corpus

Original paper, https://arxiv.org/abs/2010.12688

download
~~~~~~~~

1. quadruples-validation.jsonl, https://f000.backblazeb2.com/file/malay-dataset/knowledge-graph/tekgen/quadruples-validation.jsonl
2. quadruples-test.jsonl, https://f000.backblazeb2.com/file/malay-dataset/knowledge-graph/tekgen/quadruples-test.jsonl
3. splitted-quadruples-train.tsv00.translated, https://f000.backblazeb2.com/file/malay-dataset/knowledge-graph/tekgen/splitted-quadruples-train.tsv00.translated
4. splitted-quadruples-train.tsv01.translated, https://f000.backblazeb2.com/file/malay-dataset/knowledge-graph/tekgen/splitted-quadruples-train.tsv01.translated
5. splitted-quadruples-train.tsv02.translated, https://f000.backblazeb2.com/file/malay-dataset/knowledge-graph/tekgen/splitted-quadruples-train.tsv02.translated
6. splitted-quadruples-train.tsv03.translated, https://f000.backblazeb2.com/file/malay-dataset/knowledge-graph/tekgen/splitted-quadruples-train.tsv03.translated
7. splitted-quadruples-train.tsv04.translated, https://f000.backblazeb2.com/file/malay-dataset/knowledge-graph/tekgen/splitted-quadruples-train.tsv04.translated
8. splitted-quadruples-train.tsv05.translated, https://f000.backblazeb2.com/file/malay-dataset/knowledge-graph/tekgen/splitted-quadruples-train.tsv05.translated
9. splitted-quadruples-train.tsv06.translated, https://f000.backblazeb2.com/file/malay-dataset/knowledge-graph/tekgen/splitted-quadruples-train.tsv06.translated

Citation
~~~~~~~~

.. code:: bibtex

   @article{DBLP:journals/corr/abs-2010-12688,
   author    = {Oshin Agarwal and
   Heming Ge and
   Siamak Shakeri and
   Rami Al{-}Rfou},
   title     = {Large Scale Knowledge Graph Based Synthetic Corpus Generation for
   Knowledge-Enhanced Language Model Pre-training},
   journal   = {CoRR},
   volume    = {abs/2010.12688},
   year      = {2020},
   url       = {https://arxiv.org/abs/2010.12688},
   archivePrefix = {arXiv},
   eprint    = {2010.12688},
   timestamp = {Mon, 02 Nov 2020 18:17:09 +0100},
   biburl    = {https://dblp.org/rec/journals/corr/abs-2010-12688.bib},
   bibsource = {dblp computer science bibliography, https://dblp.org}
   }

Wikidata5M
----------

Original website, https://deepgraphlearning.github.io/project/wikidata5m

download
~~~~~~~~

1. https://f000.backblazeb2.com/file/malay-dataset/knowledge-graph/wikidata5m/wikidata5m.tar.gz
2. https://f000.backblazeb2.com/file/malay-dataset/knowledge-graph/wikidata5m/wikidata5m_entity.txt-0.translated
3. https://f000.backblazeb2.com/file/malay-dataset/knowledge-graph/wikidata5m/wikidata5m_entity.txt-1.translated
4. https://f000.backblazeb2.com/file/malay-dataset/knowledge-graph/wikidata5m/wikidata5m_entity.txt-2.translated
5. https://f000.backblazeb2.com/file/malay-dataset/knowledge-graph/wikidata5m/wikidata5m_entity.txt-3.translated
6. https://f000.backblazeb2.com/file/malay-dataset/knowledge-graph/wikidata5m/wikidata5m_entity.txt-4.translated
7. https://f000.backblazeb2.com/file/malay-dataset/knowledge-graph/wikidata5m/wikidata5m_entity.txt-5.translated
8. https://f000.backblazeb2.com/file/malay-dataset/knowledge-graph/wikidata5m/wikidata5m_entity.txt-6.translated
9. https://f000.backblazeb2.com/file/malay-dataset/knowledge-graph/wikidata5m/wikidata5m_entity.txt-7.translated
10. https://f000.backblazeb2.com/file/malay-dataset/knowledge-graph/wikidata5m/wikidata5m_entity.txt-8.translated
11. https://f000.backblazeb2.com/file/malay-dataset/knowledge-graph/wikidata5m/wikidata5m_entity.txt-9.translated

Citation
~~~~~~~~

.. code:: bibtex

   @article{wang2019kepler,
   title={KEPLER: A Unified Model for Knowledge Embedding and Pre-trained Language Representation},
   author={Wang, Xiaozhi and Gao, Tianyu and Zhu, Zhaocheng and Liu, Zhiyuan and Li, Juanzi and Tang, Jian},
   journal={arXiv preprint arXiv:1911.06136},
   year={2019}
   }
