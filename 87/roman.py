from collections import OrderedDict


def romanize(decimal_number):
    """Takes a decimal number int and converts its Roman Numeral str"""

    # If a non int or invalid number (<= 0 or >= 4000) is given raise a ValueError.
    if not isinstance(decimal_number, int) or decimal_number <= 0 or decimal_number >= 4000:
        raise ValueError

    roman = OrderedDict()
    roman[1000] = 'M'
    roman[900] = 'CM'
    roman[500] = 'D'
    roman[400] = 'CD'
    roman[100] = 'C'
    roman[90] = 'XC'
    roman[50] = 'L'
    roman[40] = 'XL'
    roman[10] = 'X'
    roman[9] = 'IX'
    roman[5] = 'V'
    roman[4] = 'IV'
    roman[1] = 'I'

    def roman_num(decimal_number):
        for r in roman.keys():
            x, _ = divmod(decimal_number, r)
            yield roman[r] * x
            decimal_number -= (r * x)
            if decimal_number <= 0:
                break

    return ''.join([a for a in roman_num(decimal_number)])
