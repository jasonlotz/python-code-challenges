import pytest

from numbers_to_dec import list_to_decimal

#    for num in nums:
#         if isinstance(num, bool) or not isinstance(num, int):
#             raise TypeError
#         elif not num in range(0, 10):
#             raise ValueError

#     return int(''.join(map(str, nums)))


@pytest.mark.parametrize('input, expected', [
    ([0, 4, 2, 8], 428),
    ([1, 2], 12),
    ([3], 3),
])
def test_fib(input, expected):
    assert list_to_decimal(input) == expected


def test_bool():
    with pytest.raises(TypeError) as e:
        list_to_decimal([True, ])


def test_string():
    with pytest.raises(TypeError) as e:
        list_to_decimal(['test', ])


def test_decimal():
    with pytest.raises(TypeError) as e:
        list_to_decimal([3.6, ])


def test_negative():
    with pytest.raises(ValueError) as e:
        list_to_decimal([-5, ])


def test__too_big():
    with pytest.raises(ValueError) as e:
        list_to_decimal([11, ])
