import datetime


def friday_the_13th(month, year):
    """
    >>> friday_the_13th(3, 2020)
    True
    >>> friday_the_13th(10, 2017)
    True
    """
    return True if datetime.datetime.strptime(f"13 {month} {year}", "%d %m %Y").weekday() == 4 else False


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
