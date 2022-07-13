import json


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    return [json.load(open(file)) for file in files]


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    for movie in movies:
        if 'Comedy' in movie['Genre']:
            return movie['Title']


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    return max(movies,
               key=lambda m: int(m["Awards"].split(
                   " & ")[-1].replace(" nominations.", ""))
               )["Title"]


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    return max(movies,
               key=lambda m: int(m["Runtime"].replace(" min", ""))
               )["Title"]
