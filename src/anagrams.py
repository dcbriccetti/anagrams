'Creates lists of anagrams using the algorithm described in Programming Perls'

from typing import List, Iterable, Dict
from itertools import chain

AnagramGroup = List[str]
AnagramGroups = List[AnagramGroup]


class Anagrams:
    def __init__(self, words: Iterable[str], min_word_len: int):
        words_list = list(words)
        self.min_word_len = min_word_len
        self._create_anagrams_list(words_list)
        self.longest_word_length: int = max((len(word[0]) for word in self.anagram_groups))
        self.lists_by_length: List[AnagramGroups] = self._get_lists_by_length(min_word_len)

    def of_length(self, length) -> AnagramGroups:
        'Return groups where the words have the length given'
        list_index = length - self.min_word_len
        return self.lists_by_length[list_index]

    def of(self, word) -> AnagramGroup:
        'Return anagrams of the word given'
        sorted_letters = ''.join(sorted(word))
        ag: AnagramGroup = self.anagram_group_by_sorted_letters[sorted_letters]
        return [anagram for anagram in ag if anagram != word]

    def _get_lists_by_length(self, min_word_len: int) -> List[AnagramGroups]:
        return [self._anagrams_of_length(l) for l in range(min_word_len, self.longest_word_length + 1)]

    def _anagrams_of_length(self, word_length: int) -> AnagramGroups:
        return [a for a in self.anagram_groups if len(a[0]) == word_length]

    def _create_anagrams_list(self, words) -> None:
        self.anagram_group_by_sorted_letters: Dict[str, AnagramGroup] = {}
        for word in words:
            word_sorted = ''.join(sorted(word))
            anagram_list = self.anagram_group_by_sorted_letters.get(word_sorted, [])
            anagram_list.append(word)
            self.anagram_group_by_sorted_letters[word_sorted] = anagram_list
        self.anagram_groups: AnagramGroups = [word_list for word_list in self.anagram_group_by_sorted_letters.values()
                                              if len(word_list) > 1]
        self.words = set(chain.from_iterable((word for word in (ag for ag in self.anagram_groups))))


if __name__ == '__main__':
    anagrams = Anagrams(['abet', 'bate', 'beat', 'beta', 'abel', 'able', 'bale',
                         'abets', 'baste', 'bates', 'beast', 'beats'], 4)
