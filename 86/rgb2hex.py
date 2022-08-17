def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    result = '#'
    for value in rgb:
        if value < 0 or value > 255:
            raise ValueError
        result += hex(value).replace('0x', '').ljust(2, '0').upper()

    return result
