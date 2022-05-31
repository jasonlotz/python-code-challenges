PYBITES = "pybites"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""

    # Alternative one liner
    # return ''.join(c.swapcase() if c.lower() in PYBITES.lower() else c for c in text)
    result = ''

    for char in text:
        if char.lower() in PYBITES:
            result += char.swapcase()
        else:
            result += char

    return result
