from unittest import TestCase

from anagrams import Anagrams


class TestAnagrams(TestCase):

    def setUp(self) -> None:
        self.anagrams = Anagrams(
            ['abet', 'bate', 'beat', 'beta', 'abel', 'able', 'bale', 'abets', 'baste', 'bates', 'beast', 'beats'])

    def test_of_length(self):
        self.assertEqual(2, len(self.anagrams.of_length(4)))
        self.assertEqual(1, len(self.anagrams.of_length(5)))

    def test_of(self):
        self.assertEqual(['able', 'bale'], self.anagrams.of('abel'))
        self.assertEqual([], self.anagrams.of('unknownword'))

    def test_words(self):
        self.assertEqual(12, len(self.anagrams.words))
