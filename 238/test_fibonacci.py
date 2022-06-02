import pytest

from fibonacci import fib


@pytest.mark.parametrize('input, expected', [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (20, 6765)
])
def test_fib(input, expected):
    assert fib(input) == expected


def test_fails():
    with pytest.raises(ValueError) as e:
        fib(-10)
