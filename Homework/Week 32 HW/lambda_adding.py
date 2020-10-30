def lambda_adds_a_lot(user_input_1):
    """
    >>> add1 = lambda_adds_a_lot(1)
    >>> add1(3)
    4
    >>> add1(5.7)
    6.7
    >>> add10 = lambda_adds_a_lot(10)
    >>> add10(44)
    54
    >>> add10(20)
    30
    """
    return lambda user_input: user_input + user_input_1


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
