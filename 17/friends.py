from cmath import e
import itertools


def friends_teams(friends: list, team_size: int = 2, order_does_matter: bool = False):
    if order_does_matter:
        func = itertools.permutations
    else:
        func = itertools.combinations
    return func(friends, team_size)
