def find_the_difference(first, compare):
    """
    >>> find_the_difference("abcd", "abcde")
    ['e']
    >>> find_the_difference('asdfqwer', 'qwerasdftygh')
    ['t', 'y', 'g', 'h']
    """
    missing_nums = []
    for i in compare:
        if i not in list(first):
            missing_nums.append(i)
    return missing_nums


def faster_version(first, compare):
    """
    >>> find_the_difference("abcd", "abcde")
    ['e']
    >>> find_the_difference('asdfqwer', 'qwerasdftygh')
    ['t', 'y', 'g', 'h']
    """
    missing_nums = []
    for i in compare:
        try: first.index(i)
        except ValueError: missing_nums.append(first.index(i))
    return missing_nums


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
