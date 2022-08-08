import pytz

MIN_MEETING_HOUR = 6
MAX_MEETING_HOUR = 22
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """
    Receive a utc datetime and one or more timezones and check if
    they are all within MIN_MEETING_HOUR and MAX_MEETING_HOUR
    (both included).
    """
    utc_aware = utc.replace(tzinfo=pytz.utc)

    localized_times = []

    for tz in timezones:
        if tz not in TIMEZONES:
            raise ValueError('not a valid timezone')

        tz = pytz.timezone(tz)
        localized_times.append(utc_aware.astimezone(tz))

    return all(
        MIN_MEETING_HOUR <= dt.hour <= MAX_MEETING_HOUR
        for dt in localized_times
    )
