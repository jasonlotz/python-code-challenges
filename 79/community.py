import csv
from collections import Counter

import requests

CSV_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'

timezones = Counter()


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    with requests.Session() as s:
        download = s.get(CSV_URL)
        return download.content.decode('utf-8')


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and print a table of timezones
       and their corresponding member counts in pluses to standard output
    """
    reader = csv.DictReader(content.splitlines(), delimiter=',')
    for row in reader:
        tz = row['tz']
        timezones[tz] += 1

    for location, count in sorted(timezones.items()):
        print(f'{location:<20} | {"+"*count}')
