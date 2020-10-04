def count_even(list_of_nums):
    """
    >>> count_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    5
    >>> count_even([1, 3, 2, 4, 3, 5, 7, 34, 5, 3, 2])
    4
    """
    even_num_count = 0
    for num in list_of_nums:
        if num % 2 == 0:
            even_num_count += 1
    return even_num_count


def lambda_fun(list_nums):
    """
    >>> lambda_fun([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    5
    >>> lambda_fun([1, 3, 2, 4, 3, 5, 7, 34, 5, 3, 2])
    4
    """
    return len(list(filter(lambda x: x % 2 == 0, list_nums)))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
