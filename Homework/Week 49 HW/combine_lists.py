def combine_lists(n1, n, n2, m):
    """
    >>> combine_lists([1, 2, 3], 3, [2, 5, 6], 3)
    [1, 2, 2, 3, 5, 6]
    """
    output = []
    for i in range(len(n1)):
        if i <= n:
            output.append(n1[i])
    for i in range(len(n2)):
        if i <= m:
            output.append(n2[i])
    return sorted(output)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
