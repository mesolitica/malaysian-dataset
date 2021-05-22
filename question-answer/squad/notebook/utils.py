import requests
import subprocess
import json
import os
import tempfile
from sacremoses import MosesTokenizer, MosesDetokenizer
from collections import defaultdict
from nltk import sent_tokenize

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

# PROCESSING TEXT
tokenizer_en = MosesTokenizer(lang = 'en')
detokenizer_en = MosesDetokenizer(lang = 'en')
tokenizer_es = MosesTokenizer(lang = 'ms')
detokenizer_es = MosesDetokenizer(lang = 'ms')

MAX_NUM_TOKENS = 10
SPLIT_DELIMITER = ';'
LANGUAGE_ISO_MAP = {'en': 'english', 'ms': 'english'}


def tokenize(text, lang, return_str = True):
    if lang == 'en':
        text_tok = tokenizer_en.tokenize(
            text, return_str = return_str, escape = False
        )
        return text_tok
    elif lang == 'ms':
        text_tok = tokenizer_es.tokenize(
            text, return_str = return_str, escape = False
        )
        return text_tok


def de_tokenize(text, lang):
    if not isinstance(text, list):
        text = text.split()

    if lang == 'en':
        text_detok = detokenizer_en.detokenize(text, return_str = True)
        return text_detok
    elif lang == 'ms':
        text_detok = detokenizer_es.detokenize(text, return_str = True)
        return text_detok


# Chunk sentences longer than a maximum number of words/tokens based on a delimiter character.
# This option is used only for very long sentences to avoid shorter translation than the
# original source length.
# Note that the delimiter can't be a trailing character
def split_sentences(
    text,
    lang,
    delimiter = SPLIT_DELIMITER,
    max_size = MAX_NUM_TOKENS,
    tokenized = True,
):
    text_len = (
        len(tokenize(text, lang, return_str = True).split())
        if tokenized
        else len(text.split())
    )
    if text_len >= max_size:
        delimiter_match = delimiter + ' '
        text_chunks = [
            chunk.strip() for chunk in text.split(delimiter_match) if chunk
        ]
        # Add the delimiter lost during chunking
        text_chunks = [chunk + delimiter for chunk in text_chunks[:-1]] + [
            text_chunks[-1]
        ]
        return text_chunks
    return [text]


def tokenize_sentences(text, lang):
    sentences = [
        chunk
        for sentence in sent_tokenize(text, LANGUAGE_ISO_MAP[lang])
        for chunk in split_sentences(sentence, lang)
    ]
    return sentences


# SQUAD paragraphs contains line breaks that we have to remove
def remove_line_breaks(text):
    text = text.replace('\n', '')
    text = text.replace('\r', '')
    return text


# Remove trailing punctuation from the answers retrieved from alignment
def remove_extra_punct(source, translation):
    periods_commas = '.,;:'
    brackets = [['(', ')'], ['[', ']'], ['{', '}']]
    exclamation = '¡!'
    quotation = '"'
    if len(translation) != 1:
        # Remove extra periods or commas
        if source[-1] in periods_commas and translation[-1] in periods_commas:
            translation = translation
        else:
            if (
                source[-1] in periods_commas
                and translation[-1] not in periods_commas
            ):
                translation = translation + source[-1]
            elif (
                source[-1] not in periods_commas
                and translation[-1] in periods_commas
            ):
                translation = translation.strip(translation[-1])
        # remove brackets
        if translation[-1] in [b[1] for b in brackets] and any(
            c for c in translation if c in [b[0] for b in brackets]
        ):
            translation = translation
        else:
            for bracket in brackets:
                if (
                    translation[-1] in bracket[1]
                    and translation[0] not in bracket[0]
                ):
                    translation = translation[:-1]
                elif (
                    translation[-1] not in bracket[1]
                    and translation[0] in bracket[0]
                ):
                    translation = translation[1:]
        # Complete exclamation mark
        if translation[-1] in exclamation and translation[0] in exclamation:
            translation = translation
        else:
            if (
                translation[-1] in exclamation
                and translation[0] not in exclamation
            ):
                translation = exclamation[0] + translation
            elif (
                translation[-1] not in exclamation
                and translation[0] in exclamation
            ):
                translation = translation + exclamation[1]
        # Complete quotation
        if translation[-1] in quotation and translation[0] in quotation:
            translation = translation
        else:
            if translation[-1] in quotation and translation[0] not in quotation:
                translation = quotation + translation
            elif (
                translation[-1] not in quotation and translation[0] in quotation
            ):
                translation = translation + quotation
        return translation
    else:
        return translation


# Keep the first part when the answer translation come across
# two sentences or when there are extra commas with words
def remove_extra_text(source, translation, lang = 'ms'):
    translation = sent_tokenize(translation, LANGUAGE_ISO_MAP[lang])[0]
    if ', ' in translation and ', ' not in source:
        translation = translation.split(', ')[0]
    return translation


# This function post-process the retrieved answer translation
# Note that the logic is applied on language-specific punctuation
# that means might not be generalize to every language
# TODO: generalize this logic to all the languages
def post_process_answers_translated(source, translation):
    # Keep the original answer when it is translation-invariant
    # like dates or proper names
    if len(source) > 1 and source in translation:
        translation = source
    # Post-process the answer translated
    else:
        translation = translation.strip()
        translation = remove_extra_text(source, translation)
        translation = remove_extra_punct(source, translation)

    return translation


# ALIGNMENT INDEX MANIPULATION
# Shift index in an alignment by a given amount in a give direction
def shift_value_index_alignment(value_index, alignment, direction = 'right'):
    # Remove duplicates while keeping the order of occurrence
    value_indexes = sorted(
        set(alignment.values()), key = list(alignment.values()).index
    )
    if direction == 'right':
        next_value_index = value_indexes.index(value_index) + 1
        if next_value_index != len(value_indexes):
            return value_indexes[next_value_index]
        else:
            return -1
    else:
        next_value_index = value_indexes.index(value_index) - 1
        if next_value_index != 0:
            return value_indexes[next_value_index]
        else:
            return 0


# Get the closest left or right index in a list given a certain number
def get_left_right_close_index(indexes, number, type):
    if indexes:
        indexes_list = list(indexes)
        # The >= condition is necessary to return exactly the same number if is in the list
        if type == 'left':
            if number > min(indexes_list):
                left_indexes = [
                    idx for idx in indexes_list if (number - idx) >= 0
                ]
                left_close_index = min(
                    left_indexes, key = lambda x: abs(number - x)
                )
                return left_close_index
            else:
                return min(indexes_list)

        elif type == 'right':
            if number < max(indexes_list):
                right_indexes = [
                    idx for idx in indexes_list if (number - idx) <= 0
                ]
                right_close_index = min(
                    right_indexes, key = lambda x: abs(number - x)
                )
                return right_close_index
            else:
                return max(indexes_list)
    else:
        return number


# Compute alignment between character indexes and token indexes, and conversely
def tok2char_map(text_raw, text_tok):
    # First, compute the token to white-spaced token indexes map (many-to-one map)
    # tok --> ws_tok
    tok2ws_tok = dict()
    ws_tokens = text_raw.split()
    idx_wst = 0
    merge_tok = ''
    for idx_t, t in enumerate(text_tok.split()):
        merge_tok += t
        tok2ws_tok[idx_t] = idx_wst
        if merge_tok == ws_tokens[idx_wst]:
            idx_wst += 1
            merge_tok = ''

    # Second, compute white-spaced token to character indexes map (one-to-one map):
    # ws_tok  --> char
    ws_tok2char = dict()
    for ws_tok_idx, ws_tok in enumerate(text_raw.split()):
        if ws_tok_idx == 0:
            char_idx = 0
            ws_tok2char[ws_tok_idx] = char_idx
        elif ws_tok_idx > 0:
            char_idx = len(' '.join(text_raw.split()[:ws_tok_idx])) + 1
            ws_tok2char[ws_tok_idx] = char_idx

    # Finally, compute the token to character map (one-to-one)
    tok2char = {
        tok_idx: ws_tok2char[tok2ws_tok[tok_idx]]
        for tok_idx, _ in enumerate(text_tok.split())
    }

    return tok2char


# Convert a token-level alignment into a char-level alignment
# Can be white-spaced tokens or normal tokens, the important thing is the one-to-one mapping
def get_src2tran_alignment_char(alignment, source, translation):
    source_tok = tokenize(source, 'en')
    translation_tok = tokenize(translation, 'ms')
    src_tok2char = tok2char_map(source, source_tok)
    tran_tok2char = tok2char_map(translation, translation_tok)

    # Get token index to char index translation map for both source and target
    src2tran_alignment_char = defaultdict(list)
    # Prevent
    try:
        for src_tran in alignment.split():
            src_tok_idx = int(src_tran.split('-')[0])
            tran_tok_idx = int(src_tran.split('-')[1])
            src_char_idx = src_tok2char[src_tok_idx]
            tran_char_idx = tran_tok2char[tran_tok_idx]
            src2tran_alignment_char[src_char_idx].append(tran_char_idx)
    except KeyError:
        pass
    # Define a one-to-one mapping left-oriented by keeping the minimum key value
    src2tran_alignment_char_min_tran_index = {
        k: min(v) for k, v in src2tran_alignment_char.items()
    }

    return src2tran_alignment_char_min_tran_index


# Convert a set of sentence alignments into one document alignment
def compute_context_alignment(sentence_alignments):
    if isinstance(sentence_alignments, list) and len(sentence_alignments) > 1:

        def get_max_src_tgt_token_index(sentence_alignment):
            src_token_index = [
                int(src_tgt_idx.split('-')[0])
                for src_tgt_idx in sentence_alignment.split()
            ]
            tran_token_index = [
                int(src_tran_idx.split('-')[1])
                for src_tran_idx in sentence_alignment.split()
            ]
            shift_source = max(src_token_index) + 1
            shift_translation = max(tran_token_index) + 1
            return shift_source, shift_translation

        def shift_alignment(alignment, shift_source, shift_translation):
            shifted_alignment = ' '.join(
                [
                    '{}-{}'.format(
                        (int(src_tgt_idx.split('-')[0]) + shift_source),
                        (int(src_tgt_idx.split('-')[1]) + shift_translation),
                    )
                    for src_tgt_idx in alignment.split()
                ]
            ).strip()
            return shifted_alignment

        # Add shift for source and target token index only to the alignments for the second-to-last sentences.
        # Also, the shift value increase while looping over the sentence alignments
        context_alignment = ''
        for idx_alignment, sent_alignment in enumerate(sentence_alignments):
            if idx_alignment == 0:
                shift_src, shift_tran = 0, 0
                context_alignment += shift_alignment(
                    sent_alignment, shift_src, shift_tran
                )
            elif idx_alignment > 0:
                shift_src, shift_tran = get_max_src_tgt_token_index(
                    context_alignment
                )
                context_alignment += ' ' + shift_alignment(
                    sent_alignment, shift_src, shift_tran
                )
        context_alignment = context_alignment.strip()
    else:
        # Convert to string
        context_alignment = ''.join(sentence_alignments).strip()
    return context_alignment


# ANSWER EXTRACTION FROM CONTEXT
# This function extract the answer translated from the context translated only using context alignment.
# A series of heuristics are applied in order to extract the answer
def extract_answer_translated_from_alignment(
    answer_text,
    answer_start,
    context,
    context_translated,
    context_alignment,
    max_len_difference = 10,
):
    # Get the corresponding start and end char of the answer_translated in the context translated
    # First, get all the index positions for each word in the answer
    answer_words_positions = [answer_start]
    for word in answer_text.split():
        pos = answer_start + len(word) + 1
        answer_words_positions.append(pos)

    # Second, get all the corresponding index positions in the answer translated
    answer_translated_words_positions = []
    for idx, pos in enumerate(answer_words_positions):
        pos = get_left_right_close_index(
            context_alignment.keys(), pos, type = 'left'
        )
        answer_translated_words_positions.append(context_alignment[pos])

    # Then, detect the start and end position in the answer translated
    start, end = (
        min(answer_translated_words_positions),
        max(answer_translated_words_positions),
    )
    answer_translated_start = start
    answer_translated_end = end

    # Also, get the next start position to retrieve the answer until that index
    answer_next_start = answer_start + len(answer_text) + 1
    answer_next_start = get_left_right_close_index(
        context_alignment.keys(), answer_next_start, type = 'right'
    )
    answer_translated_next_start = context_alignment[answer_next_start]

    # Check if the answer_translated next start index is smaller than the and answer_translated_end index.
    # If so move to the next right index until is greater than the answer_translated_end
    while answer_translated_next_start <= answer_translated_end:
        answer_translated_next_start = shift_value_index_alignment(
            answer_translated_next_start, context_alignment
        )
        # If the maximum index is at the end of the alignment map, change its value to the last character
        if answer_translated_next_start == -1:
            answer_translated_next_start = len(context_translated)

    # Extract answer translated from context translated with answer_start and answer_next_start
    # the answer_translated is a span from the min to max char index (
    answer_translated = context_translated[
        answer_translated_start:answer_translated_next_start
    ]
    return answer_translated, answer_translated_start


# This function extract the answer from a given context
def extract_answer_translated(
    answer,
    answer_translated,
    context,
    context_translated,
    context_alignment_tok,
    retrieve_answers_from_alignment,
):
    # First, compute the src2tran_alignment_char
    context_alignment_char = get_src2tran_alignment_char(
        context_alignment_tok, context, context_translated
    )

    # 1.1)
    # Match the answer_translated in the context_translated starting from the left-close char index
    # of the answer_start in the context_alignment. When the answer_start is present in the
    # context_alignment the closest index is exactly the answer_start index
    answer_text = answer['text']
    answer_start = answer['answer_start']
    answer_start = get_left_right_close_index(
        list(context_alignment_char.keys()), answer_start, type = 'left'
    )
    try:
        answer_translated_start = context_alignment_char[answer_start]
    except KeyError:
        answer_translated, answer_translated_start = '', -1
    # Find answer_start in the translated context by looking close to the answer_translated_char_start
    # I am shifting the index by an additional 20 chars to the left in the case
    # the alignment is not precise enough (20 chars is more or less 2/3 words).
    # If the shifted answer_start is smaller than 0, we set it as zero to matching errors
    shift_index = -20
    answer_translated_start_shifted = answer_translated_start + shift_index
    if answer_translated_start_shifted < 0:
        answer_translated_start_shifted = 0

    if (
        context_translated.lower().find(
            answer_translated.lower(), answer_translated_start_shifted
        )
        != -1
    ):

        answer_translated_start = context_translated.lower().find(
            answer_translated.lower(), answer_translated_start_shifted
        )
        answer_translated_end = answer_translated_start + len(answer_translated)
        answer_translated = context_translated[
            answer_translated_start:answer_translated_end
        ]

    # 1.2) Find the answer_translated in the context_translated from the beginning of the text
    elif (
        context_translated.lower().find(
            answer_translated.lower(), answer_translated_start
        )
        == -1
    ):
        if context_translated.lower().find(answer_translated.lower()) != -1:

            answer_translated_start = context_translated.lower().find(
                answer_translated.lower()
            )
            answer_translated_end = answer_translated_start + len(
                answer_translated
            )
            answer_translated = context_translated[
                answer_translated_start:answer_translated_end
            ]

        # 2) Retrieve the answer from the context translated using the
        # answer start and answer end provided by the alignment
        else:
            if retrieve_answers_from_alignment:
                answer_translated, answer_translated_start = extract_answer_translated_from_alignment(
                    answer_text,
                    answer_start,
                    context,
                    context_translated,
                    context_alignment_char,
                )
            else:
                answer_translated = ''
                answer_translated_start = -1

    # No answer translated found
    else:
        answer_translated = ''
        answer_translated_start = -1

    # Post-process if the answer is not empty
    if answer_translated:
        answer_translated = post_process_answers_translated(
            answer_text, answer_translated
        )

    return answer_translated, answer_translated_start


# TRANSLATING
# Translate text using the OpenNMT-py script
PUNCTUATION = ['.', ',', '?', '!', '¿', '¡', ')', '(', ']', '[']


# Remove extra punctuation when the translations come from a very short text
# Handle exceptions in case the translation in just one word length
def post_process_translation(source, translation, punctuation = PUNCTUATION):
    try:
        # Avoid translations where the same token is repeated
        if set(translation.split()) == translation.split()[0]:
            translation = translation[0]
        if source[0].isupper():
            translation = translation[0].upper() + translation[1:]
        if source[0].islower() and len(translation) > 1:
            translation = translation[0].lower() + translation[1:]
        if source[-1] == '.':
            if translation[-1] in punctuation:
                translation = translation[:-1] + '.'
            else:
                translation += '.'
        if source[-1] == ',':
            if translation[-1] in punctuation:
                translation = translation[:-1] + ','
            else:
                translation += ','
        if translation[0] in punctuation and len(translation) > 1:
            translation = translation[1:]
        return translation
    except IndexError:
        return translation


# Translate via the OpenNMT-py script
def translate(source_sentences, file, output_dir, batch_size):
    filename = os.path.basename(file)
    source_filename = os.path.join(
        output_dir, '{}_source_translate'.format(filename)
    )
    with open(source_filename, 'w') as sf:
        sf.writelines('\n'.join(s for s in source_sentences))

    translation_filename = os.path.join(
        output_dir, '{}_target_translated'.format(filename)
    )
    en2es_translate_cmd = (
        SCRIPT_DIR
        + '/../nmt/en2es_translate.sh {} {} {}'.format(
            source_filename, translation_filename, batch_size
        )
    )
    subprocess.run(en2es_translate_cmd.split())

    with open(translation_filename) as tf:
        translated_sentences = [s.strip() for s in tf.readlines()]

    os.remove(source_filename)
    os.remove(translation_filename)

    return translated_sentences


# COMPUTE ALIGNMENT
# Compute alignment between source and target sentences
def compute_alignment(
    source_sentences,
    source_lang,
    translated_sentences,
    target_lang,
    alignment_type,
    file,
    output_dir,
):
    filename = os.path.basename(file)
    source_sentences = [
        tokenize(sentence, source_lang) for sentence in source_sentences
    ]
    translated_sentences = [
        tokenize(sentence, target_lang) for sentence in translated_sentences
    ]

    source_filename = os.path.join(
        output_dir, '{}_source_align'.format(filename)
    )
    with open(source_filename, 'w') as sf:
        sf.writelines('\n'.join(s for s in source_sentences))

    translation_filename = os.path.join(
        output_dir, '{}_target_align'.format(filename)
    )
    with open(translation_filename, 'w') as tf:
        tf.writelines('\n'.join(s for s in translated_sentences))

    alignment_filename = os.path.join(output_dir, 'alignment')
    efolmal_cmd = SCRIPT_DIR + '/compute_alignment.sh {} {} {} {} {} {}'.format(
        source_filename,
        source_lang,
        translation_filename,
        target_lang,
        alignment_type,
        alignment_filename,
    )
    subprocess.run(efolmal_cmd.split())

    with open(alignment_filename) as af:
        alignments = [a.strip() for a in af.readlines()]

    os.remove(source_filename)
    os.remove(translation_filename)
    os.remove(alignment_filename)
    return alignments
