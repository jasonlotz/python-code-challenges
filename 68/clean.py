import string

def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    exclude = set(string.punctuation)
    return ''.join(ch for ch in input_string if ch not in exclude)