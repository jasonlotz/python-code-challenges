from collections import namedtuple
from pickle import FALSE

User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=False)
bob = User(name='Bob', role=USER, expired=True)
pybites = User(name='PyBites', role=ADMIN, expired=False)
USERS = (julian, bob, pybites)

# define exception classes here


class UserDoesNotExist(Exception):
    pass


class UserAccessExpired(Exception):
    pass


class UserNoPermission(Exception):
    pass


def get_secret_token(username):
    name_check = False
    role_check = False
    expire_check = False

    for user in USERS:
        if user.name == username:
            name_check = True

            if user.role == ADMIN:
                role_check = True

            if not user.expired:
                expire_check = True

    if not name_check:
        raise UserDoesNotExist
    elif not expire_check:
        raise UserAccessExpired
    elif not role_check:
        raise UserNoPermission
    else:
        return SECRET
