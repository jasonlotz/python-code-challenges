from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple('Game', 'title link')


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    result = []
    for item in feedparser.parse(FEED_URL)['entries']:
        result.append(Game(item['title'], item['link']))
    
    return result

if __name__ == "__main__":
    print(get_games())