def bubble_sort(nums: list[int]) -> list[int]:
    """
    >>> bubble_sort([9, 6, 7, 4, 8, 3, 5, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    for i in range(len(nums)):
        for j in range(0, len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
