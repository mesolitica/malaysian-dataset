import os

os.environ['CUDA_VISIBLE_DEVICES'] = ''

from glob import glob
import malaya
import json

split_sentences = malaya.text.function.split_into_sentences
transformer = malaya.translation.en_ms.transformer()

batch_size = 16
cnn = glob('dailymail/stories/*')

DM_SINGLE_CLOSE_QUOTE = u'\u2019'  # unicode
DM_DOUBLE_CLOSE_QUOTE = u'\u201d'
# acceptable ways to end a sentence
END_TOKENS = [
    '.',
    '!',
    '?',
    '...',
    "'",
    '`',
    '"',
    DM_SINGLE_CLOSE_QUOTE,
    DM_DOUBLE_CLOSE_QUOTE,
    ')',
]


def _read_text_file(text_file):
    lines = []
    with open(text_file, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def _get_art_abs(story_file):
    """Get abstract (highlights) and article from a story file path."""
    # Based on https://github.com/abisee/cnn-dailymail/blob/master/
    #     make_datafiles.py

    lines = _read_text_file(story_file)

    # The github code lowercase the text and we removed it in 3.0.0.

    # Put periods on the ends of lines that are missing them
    # (this is a problem in the dataset because many image captions don't end in
    # periods; consequently they end up in the body of the article as run-on
    # sentences)
    def fix_missing_period(line):
        """Adds a period to a line that is missing a period."""
        if '@highlight' in line:
            return line
        if not line:
            return line
        if line[-1] in END_TOKENS:
            return line
        return line + ' .'

    lines = [fix_missing_period(line) for line in lines]

    # Separate out article and abstract sentences
    article_lines = []
    highlights = []
    next_is_highlight = False
    for line in lines:
        if not line:
            continue  # empty line
        elif line.startswith('@highlight'):
            next_is_highlight = True
        elif next_is_highlight:
            highlights.append(line)
        else:
            article_lines.append(line)

    # Make article into a single string
    article = ' '.join(article_lines)
    abstract = '\n'.join(highlights)

    return article, abstract


from tqdm import tqdm

results = []
for i in tqdm(range(len(cnn))):
    article, abstract = _get_art_abs(cnn[i])
    splitted_article = split_sentences(article, minimum_length = 2)
    translated_article = []
    for i in range(0, len(splitted_article), batch_size):
        translated_article.extend(
            transformer.greedy_decoder(splitted_article[i : i + batch_size])
        )

    splitted_abstract = split_sentences(abstract, minimum_length = 2)
    translated_abstract = []
    for i in range(0, len(splitted_abstract), batch_size):
        translated_abstract.extend(
            transformer.greedy_decoder(splitted_abstract[i : i + batch_size])
        )
    results.append(
        {
            'en_article': splitted_article,
            'ms_article': translated_article,
            'en_abstract': splitted_abstract,
            'ms_abstract': translated_abstract,
        }
    )


with open('translated-dailymail.json', 'w') as fopen:
    json.dump(results, fopen)
