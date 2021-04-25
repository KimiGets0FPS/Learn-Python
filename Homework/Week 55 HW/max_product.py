def max_product(nums: list[int]) -> int:
    """
    >>> max_product([1, 2, 3])
    6
    >>> max_product([2, 5, 7, 2, 6, 4, 8])
    56
    >>> max_product([-13, -10, -5, -1, 0])
    130
    >>> max_product([-13, -4, 2, 74, -2, -100, -200])
    20000
    >>> max_product([])
    0
    >>> max_product([1, 2])
    2
    """
    if len(nums) < 2:
        return 0
    max_1, max_2, small_1, small_2 = 0, 0, 0, 0
    for i in nums:
        # Getting the Maximum numbers
        # 1st Example:
        # max_1: 1, 2, 3
        # max_2: 0, 1, 2
        if i > max_1:
            max_2 = max_1
            max_1 = i
        elif i > max_2:
            max_2 = i
        # Getting the minimum numbers
        # 3rd Example:
        # small_1: -13, -10
        # small_2: 0, -13
        if i < 0 and abs(i) > abs(small_1):
            small_2 = small_1
            small_1 = i
        elif i < 0 and abs(i) > abs(small_2):  # if asb(i) is greater than asb(small_2), then small_2 = i
            small_2 = i
    if small_1 * small_2 > max_1 * small_2:
        return small_1 * small_2
    return max_1 * max_2


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
