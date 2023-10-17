def maximum_wealth(accounts: list[list[int]]) -> int:
    """
    >>> maximum_wealth([[1, 2, 3], [3, 2, 1]])
    6
    """
    output = 0
    for i in accounts:
        if sum(i) > output:
            output = sum(i)
    return output


def faster_way(accounts: list[list[int]]) -> int:
    """
    >>> faster_way([[1, 2, 3], [3, 2, 1]])
    6
    """
    return max(sum(i) for i in accounts)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
