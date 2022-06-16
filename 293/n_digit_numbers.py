import math

from typing import List, TypeVar
T = TypeVar('T', int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    if n < 1:
        raise ValueError

    return [int(number * (10 ** (n - count_digit(number)))) for number in numbers]


def count_digit(n):
    count = 0
    n = abs(n)

    while n != 0:
        n //= 10
        print(n)
        count += 1

    return count
