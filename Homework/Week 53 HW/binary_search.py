def binary_search(nums: list[int], target: int) -> int:
    """
    >>> binary_search(list(range(1, 100)), 101)
    -1
    >>> binary_search(list(range(1, 100)), 31)
    30
    >>> binary_search([1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4], 3)
    11
    >>> binary_search([1, 2, 3], 4)
    -1
    >>> binary_search([1, 2, 3], 1)
    0
    """
    high = len(nums) - 1
    low = 0
    found = -1
    while high >= low:
        mid = (high + low) // 2
        if nums[mid] == target:
            found = mid
        if nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return found


def find_smallest_index(nums: list[int], target: int) -> int:
    """
    >>> find_smallest_index([1, 2, 2, 3, 3, 4], 2)
    1
    """
    import math
    found = math.inf
    high = len(nums) - 1
    low = 0
    while high >= low:
        mid = (high + low) // 2
        if nums[mid] == target:
            found = mid
        if nums[mid] < target:
            high = mid - 1
        else:
            low = mid + 1
    if found != math.inf:
        return found
    return -1


def linear_search(nums: list[int], target: int) -> int:
    """
    >>> linear_search(list(range(1, 100)), 101)
    -1
    >>> linear_search(list(range(1, 100)), 31)
    30
    """
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
