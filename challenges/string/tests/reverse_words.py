import unittest

from challenges.string.source.reverse_words import reverse_words, reverse_words_v1, reverse_words_v2


class TestReverseWordsInSentence(unittest.TestCase):

    def test_reverse_sentence(self):
        ip = "Hello World!"
        exp = "World! Hello"
        self.assertEqual(exp, reverse_words(ip))

        ip = "Hello World!"
        exp = "World! Hello"
        self.assertEqual(exp, reverse_words_v1(ip))

        ip = "Hello World!"
        exp = "World! Hello"
        self.assertEqual(exp, reverse_words_v2(ip))