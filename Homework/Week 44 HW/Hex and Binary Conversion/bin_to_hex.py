def bin_to_hex(binary):
    """
    >>> bin_to_hex(1111)
    'F'
    """
    multiplier = 0
    output = ''
    code = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    while binary != 0:
        if len(list(str(binary))) > 4:
            temp = list(str(binary))[-4:]
        multiplier += 1
        binary //= 100000
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
