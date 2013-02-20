from nltk import BigramAssocMeasures, BigramCollocationFinder
from nltk.corpus import shakespeare
from haikuwriters.utils import remove_punctuation

bigram_measures = BigramAssocMeasures()

class FrequencyMetrics:

    def __init__(self, limit=1000):
        # TODO: Read all of shakespeare into words?
        fileid = shakespeare.fileids()[0]
        words = remove_punctuation(shakespeare.words(fileid))
        self.finder = BigramCollocationFinder.from_words(words)
        self.bigrams = self.finder.nbest(bigram_measures.raw_freq, limit)

    def bigram_frequency(self, bigram):
        pass