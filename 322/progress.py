from datetime import datetime


def ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = None) -> bool:
    day_of_year = day_of_year or int(datetime.now().strftime('%j'))

    expected_books = books_goal * (day_of_year / 365)

    return books_read >= expected_books
