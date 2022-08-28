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
    if not isinstance(date, datetime):
        raise ValueError("The provided value is not a datetime")

    if date > NOW:
        raise ValueError("The provided date cannot be greater than now")

    time = NOW - date
    total_seconds = time.total_seconds()

    for time_offset in TIME_OFFSETS:
        # offset = (total_seconds / time_offset.offset) * time_offset.offset

        if total_seconds < time_offset.offset:
            if time_offset.divider:
                return time_offset.date_str.format(int(total_seconds / time_offset.divider))
            else:
                return time_offset.date_str.format(int(total_seconds))

    return date.strftime('%m/%d/%y')
