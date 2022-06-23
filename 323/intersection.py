import functools
from typing import Iterable, Set, Any


def intersection(*args: Iterable) -> Set[Any]:
    non_empties = [x for x in args if x]
    try:
        result = functools.reduce(
            lambda x, y: set(x).intersection(y), non_empties)
        result = set(result)
    except TypeError:
        result = set()
    return result
