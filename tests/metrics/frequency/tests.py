from unittest import TestCase
from haikuwriters.metrics.frequency import FrequencyMetrics

class FrequencyMetricsTests(TestCase):
    def test_len_bigrams(self):
        metrics = FrequencyMetrics(100)
        self.assertEqual(100, len(metrics.bigrams))

    def test_bigram_frequency_not_found(self):
        # create a bigram that doesn't exist in the top N bigrams
        # call a bigram_frequency method on metrics
        # assert that you get 0 (or some reasonable result of your choice)
        pass

    def test_bigram_frequency_range(self):
        # create a bigram that exists in the top N bigrams
        # call a method on metrics
        # assert that the output is between -1 and 1
        pass
    