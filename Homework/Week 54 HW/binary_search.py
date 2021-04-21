def largest_index(nums: list[int], target: int) -> int:
    """
    >>> largest_index([1, 2, 3, 3, 3, 3, 4], 3)
    5
    >>> largest_index([], 10)
    -1
    >>> largest_index([1, 2, 3], 4)
    -1
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


def smallest_index_with_group(nums: list[int], target: int) -> int:
    """
    >>> smallest_index_with_group([1, 2, 3, 3, 3, 3, 4], 3)
    2
    >>> smallest_index_with_group([], 10)
    -1
    >>> smallest_index_with_group([1, 2, 3], 4)
    -1
    """
    high = len(nums) - 1
    low = 0
    found = -1
    while high >= low:
        mid = (high + low) // 2
        if nums[mid] == target:
            found = mid
        if nums[mid] >= target:
            high = mid - 1
        else:
            low = mid + 1
    return found


def smallest_index(nums: list[int], target: int) -> int:
    """
    >>> smallest_index([1, 2, 3, 3, 3, 3, 4], 3)
    2
    >>> smallest_index([], 10)
    -1
    >>> smallest_index([1, 2, 3], 4)
    -1
    """
    high = len(nums) - 1
    low = 0
    while high >= low:
        mid = (high + low) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid
        elif mid > 0 and nums[mid-1] == target:
            high = mid
        else:
            return mid
    return -1


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
