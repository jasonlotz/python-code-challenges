import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve
from statistics import mean

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = os.getenv("TMP", "/tmp")

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    movies = defaultdict(list)

    movies_file = csv.DictReader(open(local))

    for movie in movies_file:
        if movie['title_year'] and movie['director_name'] and movie['movie_title'] and movie['imdb_score'] and int(movie['title_year']) >= MIN_YEAR:
            director_movie = Movie(
                movie['movie_title'], int(movie['title_year']), float(movie['imdb_score']))
            movies[movie['director_name']].append(director_movie)

    return movies


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    return round(mean(movie.score for movie in movies), 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    average_scores = []

    for director, movies in directors.items():
        if len(movies) < MIN_MOVIES:
            continue
        average_scores.append((director, calc_mean_score(movies)))

    return sorted(average_scores,
                  key=lambda t: t[1],
                  reverse=True)
