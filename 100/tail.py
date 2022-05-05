from pathlib import Path
from typing import List


def tail(filepath: Path, n: int) -> List[str]:
    """
    Similate Unix' "tail -n" command:
    - Read in the file ("filepath").
    - Parse it into a list of lines, stripping trailing newlines.
    - Return the last "n" lines.
    """
    result = []

    with open(filepath) as file:

        # loop to read iterate
        # last n lines and print it
        for line in (file.readlines()[-n:]):
            result.append(line.rstrip('\n'))

    return result
