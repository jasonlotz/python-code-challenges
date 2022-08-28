from collections import namedtuple
from datetime import datetime

TimeOffset = namedtuple('TimeOffset', 'offset date_str divider')

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60*60, 24*60*60
TIME_OFFSETS = (
    TimeOffset(10, 'just now', None),
    TimeOffset(MINUTE, '{} seconds ago', None),
    TimeOffset(2*MINUTE, 'a minute ago', None),
    TimeOffset(HOUR, '{} minutes ago', MINUTE),
    TimeOffset(2*HOUR, 'an hour ago', None),
    TimeOffset(DAY, '{} hours ago', HOUR),
    TimeOffset(2*DAY, 'yesterday', None),
)


def pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    if not isinstance(date, datetime) or date > NOW:
        raise ValueError('expecting past datetime')

    # using total_seconds because seconds only goes till max 1 day
    seconds = int((NOW - date).total_seconds())

    for time in TIME_OFFSETS:
        if seconds < time.offset:
            amount = time.divider and int(seconds/time.divider) or seconds
            return time.date_str.format(amount)
    else:
        # beyond yesterday just print date string
        return date.strftime('%m/%d/%y')
