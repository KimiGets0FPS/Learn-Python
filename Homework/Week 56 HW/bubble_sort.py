def big_num_right_side(nums: list[int]) -> list[int]:
    """
    >>> big_num_right_side([0, 2, 1, 4, 3, 6, 5, 7, 9, 8])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> big_num_right_side([-1, -3, -2, -4, -7, -5, -6, -9, -8, 0])
    [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0]
    >>> big_num_right_side([])
    []
    """
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j+1], nums[j] = nums[j], nums[j+1]
    return nums


def small_num_left_side(nums: list[int]) -> list[int]:
    """
    >>> small_num_left_side([2, 0, 1, 4, 3, 6, 5, 7, 9, 8])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> small_num_left_side([-1, -3, -2, -4, -7, -5, -6, -9, -8, 0])
    [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0]
    >>> small_num_left_side([])
    []
    """
    for i in range(len(nums)-1, -1, -1):
        for j in range(len(nums)-i-1, -1, -1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
    return nums


def bubble_sort_descending(nums: list[int]) -> list[int]:
    """
    >>> bubble_sort_descending([2, 0, 1, 4, 3, 6, 5, 7, 9, 8])
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    >>> bubble_sort_descending([-1, -3, -2, -4, -7, -5, -6, -9, -8, 0])
    [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
    >>> bubble_sort_descending([])
    []
    """
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] < nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
