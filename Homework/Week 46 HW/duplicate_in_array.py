def find_duplicate(array):
    """
    >>> find_duplicate([1, 2, 2, 3, 4])
    True
    >>> find_duplicate([1, 2, 3, 4])
    False
    """
    sorted_list = sorted(array)
    for i in range(1, len(sorted_list)):
        if sorted_list[i] == sorted_list[i-1]:
            return True
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
