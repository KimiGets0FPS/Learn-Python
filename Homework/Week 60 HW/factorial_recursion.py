def factorial_recursion(times: int) -> int:
    """
    >>> factorial_recursion(10)
    3628800
    >>> factorial_recursion(0)
    1
    >>> factorial_recursion(1)
    1
    """
    if times > 1:
        return times * factorial_recursion(times-1)
    return 1


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
