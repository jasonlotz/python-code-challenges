def round_to_next(number: int, multiple: int):
    mod = number % multiple

    return number + multiple - mod if mod else number
