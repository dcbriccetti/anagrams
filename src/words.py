import itertools
from typing import Iterable, Dict, List, Iterator


def words_from_file(filename: str, comment_char='#') -> Iterator[str]:
    with open(filename) as file:
        for line in file:
            if not line.startswith(comment_char):
                yield line.strip().lower()


def words_by_length(words: Iterable[str]) -> Dict[int, List[str]]:
    sorted_words = list(words)
    sorted_words.sort(key=lambda word: len(word))
    return {k: list(v) for k, v in itertools.groupby(sorted_words, lambda word: len(word))}
