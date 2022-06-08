import re

PATTERN = re.compile(r'(,){2,}')


def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    result = {}

    for line in passwd.splitlines():
        if line:
            split_line = line.split(':')

            user = split_line[0]
            name = split_line[4] if split_line[4] else 'unknown'

            name = name.rstrip(',')
            name = re.sub(PATTERN, ' ', name)

            result[user] = name

    return result
