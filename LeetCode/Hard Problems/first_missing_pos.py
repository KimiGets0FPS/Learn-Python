def first_missing_pos(nums: list[int]) -> int:
    """
    >>> first_missing_pos([7,8,9,11,12])
    1
    """
    i = 1
    while True:
        if i not in nums:
            break
        else:
            i += 1
    return i


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
