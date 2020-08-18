'Creates lists of anagrams using the algorithm described in Programming Perls'

from typing import List, Iterable

AnagramsList = List[List[str]]


class Anagrams:
    def __init__(self, words: Iterable[str], min_word_len: int):
        self.min_word_len = min_word_len
        self.anagrams_list: AnagramsList = self._create_anagrams_list(words)
        self.longest_word_length: int = max((len(word[0]) for word in self.anagrams_list))
        self.lists_by_length: List[AnagramsList] = self._get_lists_by_length(min_word_len)

    def get_with_word_length(self, current_word_length) -> AnagramsList:
        list_index = current_word_length - self.min_word_len
        return self.lists_by_length[list_index]

    def _get_lists_by_length(self, min_word_len: int) -> List[AnagramsList]:
        return [self._anagrams_of_length(l) for l in range(min_word_len, self.longest_word_length + 1)]

    def _anagrams_of_length(self, word_length: int) -> AnagramsList:
        return [a for a in self.anagrams_list if len(a[0]) == word_length]

    @staticmethod
    def _create_anagrams_list(words) -> AnagramsList:
        anagram_lists_by_sorted_letters = {}
        for word in words:
            word_sorted = ''.join(sorted(word))
            anagram_list = anagram_lists_by_sorted_letters.get(word_sorted, [])
            anagram_list.append(word)
            anagram_lists_by_sorted_letters[word_sorted] = anagram_list
        return [word_list for word_list in anagram_lists_by_sorted_letters.values() if len(word_list) > 1]
