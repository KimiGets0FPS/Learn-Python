def max_product(nums: list[int]) -> int:
    """
    >>> max_product([1, 2, 3])
    6
    >>> max_product([2, 5, 7, 2, 6, 4, 8])
    56
    """
    max_1 = 1
    max_2 = 1
    for i in nums:
        if max_1 < i:
            max_2 = max_1
            max_1 = i
    return max_1 * max_2


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
