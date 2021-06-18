def binary_recursive(nums: list[int], target: int, low: int, high: int):
    """
    >>> binary_recursive([1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 8, 15], 4, 0, 11)  # High = len(nums) - 1
    True
    >>> binary_recursive([1, 3, 4, 6, 8, 9, 10, 11, 12], 10, 0, 8)
    True
    >>> binary_recursive([3, 4, 5, 7, 9, 9, 20, 25, 54, 123, 2354, 3456, 456456, 2345254], 6, 0, 13)
    False
    >>> binary_recursive([0], 10, 0, 0)
    False
    >>> binary_recursive([], 1, 0, -1)
    False
    """
    if high > low:
        mid = (high + low) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            return binary_recursive(nums, target, low, mid-1)
        else:
            return binary_recursive(nums, target, mid + 1, high)
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

