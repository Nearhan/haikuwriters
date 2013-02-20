import string
from unittest import TestCase
from haikuwriters.utils import remove_punctuation


class TestRemovePunctuation(TestCase):

    def test_all_punctuation(self):
        # Convert the punctuation characters into a tuple of single characters
        punctuation = tuple(string.punctuation)
        actual = list(remove_punctuation(punctuation))
        self.assertEqual([], actual)

    def test_words_and_punctuation(self):
        words_and_punct = ["I", "am", "a", "(", "silly", ")", "sentence", "."]
        actual = list(remove_punctuation(words_and_punct))
        self.assertEqual(["I", "am", "a", "silly", "sentence"], actual)
