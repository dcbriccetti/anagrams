import itertools
from typing import Iterable, Dict, List, Iterator


def words_from_file(filename: str, comment_char='#') -> Iterator[str]:
    '''
    Return all words in a file, ignoring file lines that start with comment_char

    :param filename: the name of the file from which to read the words
    :param comment_char: a character which, if present at the start of a line in the file, causes the line to be ignored
    :return: the words read from the file
    '''
    with open(filename) as file:
        for line in file:
            if not line.startswith(comment_char):
                yield line.strip().lower()


def words_by_length(words: Iterable[str]) -> Dict[int, List[str]]:
    '''
    Given a list of words, return those words grouped by word length

    :param words: the words to group
    :return: a dictionary mapping from word length to the words of that length
    '''
    sorted_words = list(words)
    sorted_words.sort(key=lambda word: len(word))
    return {k: list(v) for k, v in itertools.groupby(sorted_words, lambda word: len(word))}
