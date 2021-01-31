def decimal_to_bin(decimal):
    """
    >>> decimal_to_bin(15)
    1111
    >>> decimal_to_bin(8)
    1000
    >>> decimal_to_bin(123)
    1111011
    >>> decimal_to_bin(123123)
    11110000011110011
    """
    multiplier = 1
    output = 0
    while decimal != 0:
        if decimal % 2 == 1:
            output += multiplier
        decimal //= 2
        multiplier *= 10
    return output


def smarter_way(decimal):
    if decimal > 1:
        smarter_way(decimal // 2)
    print(decimal % 2, end='')


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
