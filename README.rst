.. raw:: html

    <p align="center">
        <a href="#readme">
            <img alt="logo" width="60%" src="https://i.imgur.com/Qm0eQ2v.png">
        </a>
    </p>

=========

**Malaysian-Dataset**, We gather Malaysian dataset! 

Most of the folders are lack of README, so it is better to read from https://huggingface.co/mesolitica

Documentation
--------------

Proper documentation is available at https://malaysian-dataset.readthedocs.io

How we gather dataset?
----------------------

Crawling
~~~~~~~~~~~~

Contributors heavily crawled Malaysian websites, you can check out the full list of crawled websites at https://github.com/users/huseinzol05/projects/1

Social media
~~~~~~~~~~~~

1. We catch most of live data from Twitter, Facebook and Instagram using
   crawlers, So we just search using Elasticsearch query.

Translation
~~~~~~~~~~~

1. We use Google Translate.
2. We use LLM, including ChatGPT3.5, ChatGPT4, Mixtral, LLama3 70B.
3. We use Malaya translation, https://huggingface.co/mesolitica/translation-t5-small-standard-bahasa-cased-v2

Semisupervised
~~~~~~~~~~~~~~

Teacher-student
^^^^^^^^^^^^^^^

1. Supervised small samples and then trained a base model.
2. Trained base model predict larger samples, retrain next student
   models on high confident labelled data.
3. Repeat.

LLM
~~~

1. Generate using ChatGPT3.5, ChatGPT4, Mixtral, LLama3 70B.

Notes
-----

1. Any missing ``mp.py``, get it at https://gist.github.com/huseinzol05/98974ae8c6c7a65d4bc0af9f5003786a
2. Any missing python scripts, please contact me ASAP or create an issue.
3. Please at least email us first before distributing these data. Remember all these hard workings we want to give it for free.
4. What do you see just the data, but nobody can see how much we spent our cost to make it public.

Suggestion
----------

1. Feel free to contact me to request new dataset.
2. Feel free to open an issue if the link to dataset is forbidden, sometime I forgot to make it open to public.

Non-commercial Usage
--------------------

A lot of data here semisupervised / translated / tagged / decoded using
third party software, example, Google Translate, Google Speech, so to
avoid any future complication, it is better not use this data for
commercial purposes but allow for certain research purposes.

Acknowledgement
---------------

Thanks to `Im Big <https://www.facebook.com/imbigofficial/>`__,
`LigBlou <https://www.facebook.com/ligblou>`__,
`Mesolitica <https://mesolitica.com/>`__ and
`KeyReply <https://www.keyreply.com/>`__ for sponsoring AWS Google and
private cloud to deploy distributed crawlers.
