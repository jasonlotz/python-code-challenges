import collections

NOT_FOUND = "Not found"

group1 = {'tim': 30, 'bob': 17, 'ana': 24}
group2 = {'ana': 26, 'thomas': 64, 'helen': 26}
group3 = {'brenda': 17, 'otto': 44, 'thomas': 46}


def get_person_age(name):
    """Look up name (case insensitive search) and return age.
       If name in > 1 dict, return the match of the group with
       greatest N (so group3 > group2 > group1)
    """
    chained_map = collections.ChainMap(group3, group2, group1)

    for k, v in chained_map.items():
        if isinstance(name, str) and name.lower() == k:
            return v

    return NOT_FOUND
