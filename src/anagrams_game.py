'A game where you find anagrams for words, starting easy and getting harder'

from random import choice
from typing import List
from anagrams import Anagrams, AnagramsList
from words import words_from_file

MIN_WORD_LEN = 3
anagrams = Anagrams(words_from_file('resources/many-words.txt'), MIN_WORD_LEN)
common_words = set(words_from_file('resources/common-words.txt'))

current_word_length = MIN_WORD_LEN
correct_answers = 0

print('''
Hello! I will give you words, and you will give me an anagram for each word.
The words I give you come from a list of 3,000 common words. The anagrams you
provide must be in my larger list of 50,000 words. We'll start easy and get harder.
''')

while True:
    anagram_lists: AnagramsList = anagrams.get_with_word_length(current_word_length)
    chosen_anagrams: List[str] = choice(anagram_lists)
    chosen_word: str = choice(chosen_anagrams)
    if chosen_word not in common_words: continue
    anagrams_of_chosen_word = [word for word in chosen_anagrams if word != chosen_word]
    answer = input(f'{chosen_word}? ')
    if answer in anagrams_of_chosen_word:
        correct_answers += 1
        print(f'{correct_answers} right. ', end='')
        if correct_answers % 5 == 0 and current_word_length < anagrams.longest_word_length:
            current_word_length += 1
    else:
        print(f'Oops. {", ".join(anagrams_of_chosen_word)}. ', end='')
