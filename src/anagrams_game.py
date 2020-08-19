'A game where you find anagrams for words, starting easy and getting harder'

from random import randint
from typing import List, Dict

from anagrams import Anagrams, AnagramGroup
from words import words_from_file, words_by_length

anagrams = Anagrams(words_from_file('resources/many-words.txt'))
common_words = (word for word in words_from_file('resources/common-words.txt') if word in anagrams.words)
common_words_by_length: Dict[int, List[str]] = words_by_length(common_words)

current_word_length = anagrams.min_word_len
correct_answers = 0

print('''
Hello! I will give you words, and you will give me an anagram for each word.
The words I give you come from a list of 3,000 common words. The anagrams you
provide must be in my larger list of 50,000 words. We'll start easy and get harder.
''')

while True:
    words_of_current_length: List[str] = common_words_by_length[current_word_length]
    random_word_index: int = randint(0, len(words_of_current_length) - 1)
    chosen_word: str = words_of_current_length.pop(random_word_index)
    anagrams_of_chosen_word: AnagramGroup = anagrams.of(chosen_word)
    answer = input(f'{chosen_word}? ')
    if answer in anagrams_of_chosen_word:
        correct_answers += 1
        print(f'{correct_answers} right. ', end='')
        if correct_answers % 5 == 0 and current_word_length < anagrams.longest_word_length:
            current_word_length += 1
    else:
        print(f'Oops. {", ".join(anagrams_of_chosen_word)}. ', end='')
