import re


def count_indents(text: str) -> int:
    """
    Count and return the number of leading white space characters (' ').
    """
    match = re.search(r"^ *", text)

    return 0 if not match else match.end()
