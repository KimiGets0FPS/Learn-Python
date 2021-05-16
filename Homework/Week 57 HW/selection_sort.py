def selection_sort(nums: list[int]) -> list[int]:
    """
    >>> selection_sort([0, 2, 1, 5, 3, 4])
    [0, 1, 2, 3, 4, 5]
    >>> selection_sort([1, 3, 2, 5, 3, 2, 1, 5, 8, 9, 6, 4, 5])
    [1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 8, 9]
    >>> selection_sort([123, 456, 1234, 456, 58, 23, 2, 34, 245, 4756, 568])
    [2, 23, 34, 58, 123, 245, 456, 456, 568, 1234, 4756]
    """
    for i in range(len(nums)):
        smallest_ind = i
        for j in range(i+1, len(nums)):
            if nums[smallest_ind] > nums[j]:
                smallest_ind = j
        nums[smallest_ind], nums[i] = nums[i], nums[smallest_ind]
    return nums


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
