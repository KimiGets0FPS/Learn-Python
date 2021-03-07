def first_before_second(sentence, first, second):
    """
    >>> first_before_second('a rabbit jumps joyfully', 'a', 'j')
    True
    >>> first_before_second('amd is better than intel', 'z', 'y')
    False
    """
    for i in range(len(sentence)-1, -1, -1):
        if sentence[i] != first and sentence[i] == second:
            return True
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
