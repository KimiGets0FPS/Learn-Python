def bubble_sort(nums: list[int]) -> list[int]:
    """
    >>> bubble_sort([9, 6, 7, 4, 8, 3, 5, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
