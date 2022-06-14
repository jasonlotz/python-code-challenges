from typing import List


def minimum_number(digits: List[int]) -> int:
    cleaned_digits = sorted(set(digits)) if digits else [0]

    digit_strings = [str(integer) for integer in cleaned_digits]
    num_string = "".join(digit_strings)
    return int(num_string)
