from unittest import TestCase

from anagrams import Anagrams


class TestAnagrams(TestCase):

    def setUp(self) -> None:
        all_words = ['abet', 'bate', 'beat', 'beta', 'abel', 'able', 'bale', 'abets', 'baste', 'bates', 'beast', 'beats']
        self.anagrams = Anagrams(all_words, all_words)

    def test_of(self):
        self.assertEqual(['able', 'bale'], self.anagrams.of('abel'))
        self.assertEqual([], self.anagrams.of('unknownword'))

    def test_words(self):
        self.assertEqual(12, len(self.anagrams.words))
