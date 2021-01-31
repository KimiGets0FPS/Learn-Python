def bin_to_decimal(binary):
    """
    >>> bin_to_decimal(1111)
    15
    >>> bin_to_decimal(1010)
    10
    >>> bin_to_decimal(10010)
    18
    """
    # nums = list(str(binary))
    multiplier = 0
    output = 0
    while binary != 0:
        output += (binary % 10) * (2 ** multiplier)
        multiplier += 1
        binary //= 10
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
