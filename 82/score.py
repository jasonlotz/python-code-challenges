from statistics import mean
from enum import Enum

THUMBS_UP = '👍'  # in case you go f-string ...


class Score(Enum):
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4
    CHEATED = 1

    @classmethod
    def average(cls):
        return mean([score.value for score in Score])

    def __str__(self):
        return f'{self.name} => {THUMBS_UP * self.value}'
