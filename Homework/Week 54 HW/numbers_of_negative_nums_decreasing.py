def negative_nums(nums: list[int]) -> int:
    """
    >>> negative_nums([0, -1, -2, -3, -4])
    4
    >>> negative_nums([-1, -2, -3])
    3
    >>> negative_nums([9, 6, 5, 1, 1, 0, 0, -1, -2, -9])
    3
    >>> negative_nums([8, -1, -6, -210])
    3
    >>> negative_nums([-2304571207255423875408237])
    1
    >>> negative_nums([])
    0
    """
    output = len(nums)
    high = len(nums) - 1
    low = 0
    while high >= low:
        mid = (high + low) // 2
        if nums[mid] >= 0:
            output = len(nums) - mid - 1
            low = mid + 1
        else:
            high = mid - 1
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
