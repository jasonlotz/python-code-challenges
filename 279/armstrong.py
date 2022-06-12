def is_armstrong(n: int) -> bool:
    n_str = str(n)
    num_digits = len(n_str)

    armstrong_num = 0

    for digit in n_str:
        armstrong_num += int(digit) ** num_digits

    return armstrong_num == n
