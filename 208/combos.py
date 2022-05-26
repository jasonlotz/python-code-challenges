from itertools import combinations


def find_number_pairs(numbers, N=10):
    result = []

    all_combos = list(combinations(numbers, r=2))

    return [combo for combo in all_combos if combo[0] + combo[1] == N]
