import unittest

from challenges.string.source.count_and_say import count_and_say


class TestCountAndSay(unittest.TestCase):
    def test_count_and_say(self):
        self.assertEqual('112233442112', count_and_say('1223334444112'))
        self.assertEqual('11', count_and_say('1'))
        self.assertEqual('10', count_and_say('0'))
        self.assertEqual('303321', count_and_say('00033311'))
        self.assertEqual('1110', count_and_say('10'))
