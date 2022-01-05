'Creates lists of anagrams using the algorithm described in Programming Perls'
from itertools import chain
from random import randint, choice
from typing import List, Iterable, Dict, Set

AnagramGroup   = List[str]                  # ['eat', 'tea']
AnagramGroups  = List[AnagramGroup]         # [['eat', 'tea'], ['pot', 'opt', 'top']]
GroupsBySorted = Dict[str, AnagramGroup]    # { 'aet': ['eat', 'tea'] }
MIN_WORD_LEN = 3


class Anagrams:
    common_set: set[str]
    min_word_len: int
    groups_by_sorted_letters: GroupsBySorted
    groups: AnagramGroups
    words: set[str]
    longest_word_length: int
    lists_by_length: List[AnagramGroups]

    def __init__(self, many_words: Iterable[str], common_words: Iterable[str]):
        words_list = list(many_words)
        self.common_set = set(common_words)
        self.min_word_len = MIN_WORD_LEN
        self.groups_by_sorted_letters = self._create_groups_by_sorted_letters(words_list)
        self.groups = [word_list for word_list in self.groups_by_sorted_letters.values()
                       if len([word for word in word_list if word in self.common_set]) > 1]
        self.words = self._create_word_set()
        self.longest_word_length = max((len(word[0]) for word in self.groups))
        self.lists_by_length = self._get_lists_by_length(MIN_WORD_LEN)

    def of(self, word) -> AnagramGroup:
        'Return anagrams of the word given'
        sorted_letters = ''.join(sorted(word))
        group: AnagramGroup = self.groups_by_sorted_letters.get(sorted_letters, [])
        return [anagram for anagram in group if anagram != word]

    def randomly_select_group(self, length=None) -> (str, List[str]):
        groups: AnagramGroups = self.lists_by_length[length - MIN_WORD_LEN] if length else self.groups
        index = randint(0, len(groups) - 1)
        group = groups.pop(index)
        indexes_of_common = [i for i in range(len(group)) if group[i] in self.common_set]
        return group.pop(choice(indexes_of_common)), group

    def _get_lists_by_length(self, min_word_len: int) -> List[AnagramGroups]:
        return [self._anagrams_of_length(length) for length in range(min_word_len, self.longest_word_length + 1)]

    def _anagrams_of_length(self, word_length: int) -> AnagramGroups:
        return [a for a in self.groups if len(a[0]) == word_length]

    @staticmethod
    def _create_groups_by_sorted_letters(words):
        groups: Dict[str, AnagramGroup] = {}
        for word in words:
            word_sorted = ''.join(sorted(word))
            anagram_list = groups.get(word_sorted, [])
            anagram_list.append(word)
            groups[word_sorted] = anagram_list
        return groups

    def _create_word_set(self) -> Set[str]:
        groups_of_words: Iterable[AnagramGroup] = (word for word in (group for group in self.groups))
        return set(chain.from_iterable(groups_of_words))
