def sum_of_digits(num):
    """
    >>> sum_of_digits(123)
    6
    """
    if num > 0:
        return num % 10 + sum_of_digits(num//10)
    return 0


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
