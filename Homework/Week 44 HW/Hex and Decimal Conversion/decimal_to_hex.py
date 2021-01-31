def decimal_to_hex(decimal):
    """
    >>> decimal_to_hex(123)
    '7B'
    >>> decimal_to_hex(0)
    '0'
    >>> decimal_to_hex(2456)
    '998'
    """
    output = []
    if decimal == 0:
        return '0'
    while decimal != 0:
        temp = decimal % 16
        if temp <= 9:
            output.append(str(temp))
        elif temp == 10:
            output.append('A')
        elif temp == 11:
            output.append('B')
        elif temp == 12:
            output.append('C')
        elif temp == 13:
            output.append('D')
        elif temp == 14:
            output.append('E')
        elif temp == 15:
            output.append('F')
        decimal //= 16
    return ''.join(reversed(output))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
