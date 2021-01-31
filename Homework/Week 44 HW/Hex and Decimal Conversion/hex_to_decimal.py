def hex_to_decimal(hexadecimal):
    """
    >>> hex_to_decimal('1F')
    31
    >>> hex_to_decimal('7B')
    123
    >>> hex_to_decimal('0')
    0
    """
    multiplier = 0
    output = 0
    place = -1
    for _ in hexadecimal:
        if hexadecimal[place] == 'A':
            output += 10 * 16 ** multiplier
        elif hexadecimal[place] == 'B':
            output += 11 * 16 ** multiplier
        elif hexadecimal[place] == 'C':
            output += 12 * 16 ** multiplier
        elif hexadecimal[place] == 'D':
            output += 13 * 16 ** multiplier
        elif hexadecimal[place] == 'E':
            output += 14 * 16 ** multiplier
        elif hexadecimal[place] == 'F':
            output += 15 * 16 ** multiplier
        else:
            output += int(hexadecimal[place]) * 16 ** multiplier
        multiplier += 1
        place -= 1
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
