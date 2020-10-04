def organize_nums(num_list):
    """
    >>> organize_nums([1, 3, 2, 4, 5 , 6, 3])
    [1, 2, 3, 4, 5, 6]
    >>> organize_nums([1, 4, 5, 6, 3, 7, 8, 4, 5, 3, 100])
    [1, 3, 4, 5, 6, 7, 8, 100]
    """
    non_duplicate = []
    for num in num_list:
        if num not in non_duplicate:
            non_duplicate.append(num)
    non_duplicate.sort()
    return non_duplicate


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)