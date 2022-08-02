# This Bite focusses on the use of itertools. To that extend you complete get_possible_dict_words and _get_permutations_draw to get all valid dictionary words for a random draw of 7 letters.
# This is fed into the tests that calculate the word with maximum value (work previously done for Bite 3) and there you go: you have a Scrabble cheat tool (Scrabble fans, pay attention or maybe skip this Bite!).
# For example a draw of letters G, A, R, Y, T, E, V would give highest valued word GARVEY (13 points).


import itertools
import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
    DICTIONARY
)


with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    permutations = map(''.join, _get_permutations_draw(draw))
    return set(permutations) & dictionary


def _get_permutations_draw(draw):
    lowered = ''.join(draw).lower()
    for i in range(1, len(draw) + 1):
        yield from itertools.permutations(lowered, i)
