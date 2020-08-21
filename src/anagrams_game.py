'A game where you find anagrams for words, starting easy and getting harder'

from anagrams import Anagrams
from words import words_from_file

anagrams = Anagrams(words_from_file('resources/many-words.txt'), words_from_file('resources/common-words.txt'))

current_word_length = anagrams.min_word_len
correct_answers = 0

print('''
Hello! I will give you words, and you will give me an anagram for each word.
The words I give you come from a list of 3,000 common words. The anagrams you
provide must be in my larger list of 50,000 words. We'll start easy and get harder.
''')

while True:
    chosen_word, anagrams_of_chosen_word = anagrams.randomly_select_group(current_word_length)
    answer = input(f'{chosen_word}? ')
    if answer in anagrams_of_chosen_word:
        correct_answers += 1
        print(f'{correct_answers} right. ', end='')
        if correct_answers % 5 == 0 and current_word_length < anagrams.longest_word_length:
            current_word_length += 1
    else:
        print(f'Oops. {", ".join(anagrams_of_chosen_word)}. ', end='')
