import re


def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    output = {}
    for row in passwd.strip().splitlines():
        fields = row.split(':')
        username = fields[0]
        name = re.sub(r',+', r' ', fields[4].strip(',')) or 'unknown'
        output[username] = name
    return output
