from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():

    result = []

    for n in range(1, 11):
        new_date = PYBITES_BORN + timedelta(days=n * 100)
        result.append(new_date)

    return result


print(gen_special_pybites_dates())
