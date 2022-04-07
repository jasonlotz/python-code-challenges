def sum_numbers(numbers=None):

    if numbers is None:
        numbers = range(0, 101)

    result = 0

    for number in numbers:
        result += number

    return result
