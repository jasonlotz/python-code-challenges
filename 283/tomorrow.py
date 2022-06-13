import datetime


def tomorrow(today=None):
    today = today if today else datetime.date.today()

    return today + datetime.timedelta(days=1)
