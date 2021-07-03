def special_nums(list_num):
    """
    >>> special_nums([1, 2, 3, 3, 4, 4, 3, 1, 2, 3, 4, 5, 6])
    [5, 6]
    >>> special_nums([1, 1, 3, 5, 5, 4, 6, 8, 7])
    [3, 4, 6, 8, 7]
    """
    non_duplicated_nums = []
    num_count = {}
    for number in list_num:
        if number not in num_count:
            num_count[number] = 1
        else:
            num_count[number] += 1
    for num, count in num_count.items():
        if count == 1:
            non_duplicated_nums.append(num)
    return non_duplicated_nums


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
