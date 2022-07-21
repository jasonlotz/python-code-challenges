import string
import re

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())


def validate_password(password):
    if not 6 <= len(password) <= 12:
        return False

    if not re.search(r'[a-z].*[a-z]', password):
        return False

    if not re.search(r'[A-Z]', password):
        return False

    if not re.search(r'[0-9]', password):
        return False

    if not any(char in PUNCTUATION_CHARS for char in password):
        return False

    if password in used_passwords:
        return False

    used_passwords.add(password)
    return True
