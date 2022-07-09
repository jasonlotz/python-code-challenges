from cmath import e
import itertools


def friends_teams(friends: list, team_size: int = 2, order_does_matter: bool = False):
    if order_does_matter:
        return itertools.permutations(friends, team_size)
    else:
        return itertools.combinations(friends, team_size)
