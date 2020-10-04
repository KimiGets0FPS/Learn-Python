def car(people):
    """
    >>> car(9)
    2
    >>> car(100)
    20
    >>> car(101)
    21
    >>> car(4)
    1
    >>> car(5)
    1
    """
    if people == 0:
        return 0
    elif 0 < people <= 5:
        return 1
    else:
        if people % 5 == 0:
            return people // 5
        else:
            if people // 5 - 1 >= 0:
                return people // 5 + 1
            else:
                return people // 5 + 2


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
