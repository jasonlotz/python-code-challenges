from string import printable


def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    result = []
    p = printable
    for word in text.split(' '):
        for letter in word:
            if letter not in p and word not in result:
                result.append(word)

    return result
