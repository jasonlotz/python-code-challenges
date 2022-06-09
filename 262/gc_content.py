from collections import defaultdict


def def_value():
    return 0


def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    counts = defaultdict(def_value)

    for char in sequence:
        counts[char.lower()] += 1

    return round(100 * (counts['g'] + counts['c']) / (counts['a'] + counts['c'] + counts['g'] + counts['t']), 2)
