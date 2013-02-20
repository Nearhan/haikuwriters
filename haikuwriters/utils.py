import string

punkt_table = str.maketrans(string.punctuation, " " * len(string.punctuation))
def convert_punctuation_to_space(text):
    return text.translate(punkt_table)


def remove_punctuation(words):
    """
    Filter all words that are punctuation.
    """
    for word in words:
        if convert_punctuation_to_space(word) != " ":
            yield word