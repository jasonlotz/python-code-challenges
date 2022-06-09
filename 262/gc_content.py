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

    # My solution wasn't bad, but I do think a Counter was more appropriate than
    # a defaultdict for this.
    #
    # counts = Counter(sequence.upper())
    # gc_content = counts.get("G", 0) + counts.get("C", 0)
    # at_content = counts.get("A", 0) + counts.get("T", 0)
    # return round(gc_content * 100 / (gc_content + at_content), 2)
