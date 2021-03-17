def third_max(nums: list[int]):
    """
    >>> third_max([1, 2, 3])
    3
    >>> third_max([1, 2])
    2
    """
    # Criteria: Given integer array nums, return the third maximum number in this array. If the third maximum does
    # not exist, return the maximum number.
    sorted_nums = sorted(nums)
    max1, max2, max3 = 0, 0, 0
    for i in sorted_nums:
        if i > max1:
            max3, max2, max1 = max2, max1, i
    if max1 != 0:
        return max1
    return max3
    # Time complexity: O(n)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
