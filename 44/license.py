from secrets import choice
from string import ascii_uppercase, digits

ALPHABET = ascii_uppercase + digits
DASH = '-'


def _random_str(chars_per_part: int) -> str:
    return ''.join(
        choice(ALPHABET) for _ in range(chars_per_part)
    )


def gen_key(parts: int = 4, chars_per_part: int = 8) -> str:
    """
    Generate and return a random license key containing
    upper case characters and digits.

    Example with default "parts" and "chars_per_part"
    being 4 and 8: KI80OMZ7-5OGYC1AC-735LDPT1-4L11XU1U

    If parts = 3 and chars_per_part = 4 a random license
    key would look like this: 54N8-I70K-2JZ7
    """
    return DASH.join(_random_str(chars_per_part)
                     for _ in range(parts))
