import pytz
from datetime import datetime, timedelta
from typing import List

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """
    Receive a utc datetime and one or more timezones and check if
    they are all within MIN_MEETING_HOUR and MAX_MEETING_HOUR
    (both included).
    """
    if not all([t in TIMEZONES for t in timezones]):
        raise ValueError

    seconds_in_hour = 60 * 60
    results = []

    utc_tz = pytz.timezone('UTC')
    for timezone in timezones:
        current_tz = pytz.timezone(timezone)

        v1 = utc_tz.localize(utc)
        v2 = current_tz.localize(utc)

        hours = abs((v1 - v2).total_seconds()) / seconds_in_hour

        if v1 > v2:
            diff = v1 + timedelta(hours=hours)
            results.append(diff.hour in MEETING_HOURS)
        else:
            diff = v1 - timedelta(hours=hours)
            results.append(diff.hour in MEETING_HOURS)

    return all(results)
