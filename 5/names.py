NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""

    result = []

    dedup_names = set(names)

    for name in dedup_names:
        result.append(name.title())

    return result


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)

    # return names.sort(key=lambda x: x.split()[-1], reverse=True)

    l2 = []

    # create 2d list of names
    for name in names:
        l2.append(name.split())

    sorted_name_list = []

    # sort by last name
    for name in sorted(l2, key=lambda x: x[-1], reverse=True):
        sorted_name_list.append(' '.join(name))

    # return sorted list
    return sorted_name_list


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)

    first_names = [name.split()[0] for name in names]

    return sorted(first_names, key=len)[0]
