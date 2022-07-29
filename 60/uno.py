from collections import namedtuple

SUITS = 'Red Green Yellow Blue'.split()

UnoCard = namedtuple('UnoCard', 'suit name')


def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""
    singles = [0]
    doubles = list(range(1, 10)) * 2
    special = ['Draw Two', 'Skip', 'Reverse'] * 2

    cards_suit = singles + doubles + special

    all_suits = [UnoCard(suit, str(card))
                 for suit in SUITS
                 for card in cards_suit]

    wilds = [UnoCard(suit=None, name=name)
             for name in ['Wild', 'Wild Draw Four'] * 4]

    return all_suits + wilds
