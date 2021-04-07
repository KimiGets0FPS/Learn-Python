def shuffle_string(string: str, index: list[int]) -> str:
    """
    >>> shuffle_string('codeleet', [4, 5, 6, 7, 0, 2, 1, 3])
    'leetcode'
    """
    output = ['-'] * len(index)
    string = list(string)
    for i in range(len(index)):
        output.pop(index[i])
        output.insert(index[i], string[i])
    return ''.join(output)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
