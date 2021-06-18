def duplicate_removal(letters: str) -> str:
    """
    >>> duplicate_removal('abbaca')
    'ca'
    >>> duplicate_removal('azxxzy')
    'ay'
    """
    letters = list(letters)
    temp = 0
    i = 0
    while i < len(letters):
        if letters[i-temp] == letters[i+1-temp]:
            letters.pop(i-temp)
            letters.pop(i-temp)
            temp += 1
        else:
            i += 1
    return ''.join(letters)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
