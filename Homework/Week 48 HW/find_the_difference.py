def find_the_difference(first, compare):
    missing_nums = []
    for i in compare:
        try:
            first.index(i)
        except ValueError:
            missing_nums.append(i)
    return missing_nums


def using_zip(first, compare):
    """
    >>> using_zip("abcd", "abcde")
    ['e']
    >>> using_zip('asdfqwer', 'asdfqwertygh')
    ['t', 'y', 'g', 'h']
    """
    output = []
    temp = 0
    for i in range(len(first)):
        if compare[i + temp] != first[i]:
            output.append(i)
            temp += 1
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
