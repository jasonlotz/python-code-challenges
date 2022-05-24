IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    result = []

    for name in names:
        if len(result) >= MAX_NAMES or name.startswith(QUIT_CHAR):
            break
        elif name.startswith(IGNORE_CHAR) or not name.isalpha():
            continue
        else:
            result.append(name)

    return result
