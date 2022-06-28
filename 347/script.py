from enum import Enum


class Hand(str, Enum):
    RIGHT = "right"
    LEFT = "left"
    BOTH = "both"


LEFT_HAND_CHARS = set("QWERTASDFGZXCVB")
RIGHT_HAND_CHARS = set("YUIOPHJKLNM")


def get_hand_for_word(word: str) -> Hand:
    """
    Use the LEFT_HAND_CHARS and RIGHT_HAND_CHARS sets to determine
    if the passed in word can be written with only the left or right
    hand, or if both hands are needed.
    """
    requires_left_hand = False
    requires_right_hand = False

    for l in LEFT_HAND_CHARS:
        if l.upper() in word.upper():
            requires_left_hand = True
            break

    for r in RIGHT_HAND_CHARS:
        if r.upper() in word.upper():
            requires_right_hand = True
            break

    if requires_left_hand and requires_right_hand:
        return Hand.BOTH
    elif requires_right_hand:
        return Hand.RIGHT
    elif requires_left_hand:
        return Hand.LEFT
    else:
        return None


print(get_hand_for_word("terret"))
