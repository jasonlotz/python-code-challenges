import re


def sum_numbers(numbers):
    """Sums numbers

    :param numbers: a list of numbers
    :type numbers: list
    :raises TypeError: if not all numeric values passed in
    :return: sum of numbers
    :rtype: int 
    """
    pass


# doc = f'\n{sum_numbers.__doc__.strip()}'
# print(doc)

# # for some lines allow variable content after colon
# for line in (r'Sums numbers',
#              r'    :param numbers: \S.*?\n',
#              r'    :type numbers: list',
#              r'    :raises TypeError: \S.*?\n',
#              r'    :return: \S.*?\n',
#              r'    :rtype: asdfasfd'):
#     # newline to test proper indenting
#     print(line)
#     print(re.search(f'\n{line}', doc))
