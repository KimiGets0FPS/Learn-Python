def monotonic(nums):
    temp_bool = True
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            temp_bool = False
    if temp_bool:
        return True
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            return False
    return True


def one_loop(nums):
    """
    >>> one_loop([1, 2, 3, 4])
    True
    >>> one_loop([1, 2, 2, 4])
    True
    >>> one_loop([1, 2, 1, 3])
    False
    >>> one_loop([4, 3, 2, 1])
    True
    """
    ascend = True
    descend = True
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            ascend = False
        if nums[i] > nums[i - 1]:
            descend = False
    return ascend or descend


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
