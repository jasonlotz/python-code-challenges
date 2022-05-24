IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    result = []

    for name in names:
        if len(result) >= MAX_NAMES or QUIT_CHAR == name[0]:
            break
        elif IGNORE_CHAR == name[0] or not name.isalpha():
            continue
        else:
            result.append(name)

    return result
