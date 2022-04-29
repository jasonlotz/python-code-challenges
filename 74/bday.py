import datetime


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    return date.strftime("%A")

if __name__ == '__main__':
    print(weekday_of_birth_date(datetime.datetime.now()))