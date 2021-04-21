def negative_numbers(nums: list[int]) -> int:
    """
    >>> negative_numbers(list(range(-100, 100)))
    99
    >>> negative_numbers([-1, 0, 1])
    1
    >>> negative_numbers(list(range(-50, 50)))
    49
    >>> negative_numbers(list(range(0, 100)))
    0
    """
    high = len(nums) - 1
    low = 0
    if nums[0] == 0:
        return 0
    while high >= low:
        mid = (high + low) // 2
        if nums[mid] == 0:
            return len(nums) - mid - 1
        if nums[mid] > 0:
            high = mid - 1
        else:
            low = mid + 1


def non_positive_numbers(nums: list[int]) -> int:
    """
    >>> non_positive_numbers(list(range(-100, 100)))
    100
    >>> non_positive_numbers([-1, 0, 1])
    2
    >>> non_positive_numbers(list(range(-50, 50)))
    50
    >>> non_positive_numbers(list(range(0, 100)))
    1
    >>> non_positive_numbers(list(range(1, 100)))
    0
    """
    high = len(nums) - 1
    low = 0
    if nums[0] == 0:
        return 1
    if nums[0] == 1:
        return 0
    while high >= low:
        mid = (high + low) // 2
        if nums[mid] == 0:
            return len(nums) - mid
        if nums[mid] > 0:
            high = mid - 1
        else:
            low = mid + 1


def positive_numbers(nums: list[int or float]) -> int:
    """
    >>> positive_numbers(list(range(-100, 100)))
    99
    >>> positive_numbers(list(range(0, 100)))
    99
    >>> positive_numbers(list(range(50, 100)))
    50
    >>> positive_numbers([-2, 2])
    1
    >>> positive_numbers([-2, 0, 2])
    1
    >>> positive_numbers([0.5, 1, 1.5])
    3
    >>> positive_numbers([-1, 0])
    0
    """
    high = len(nums) - 1
    low = 0
    output = 0
    while high >= low:
        mid = (high + low) // 2
        if nums[mid] > 0:
            output = len(nums) - mid
            high = mid - 1
        elif nums[mid] <= 0:
            low = mid + 1
    return output


def non_negative_numbers(nums: list[int]) -> int:
    """
    >>> non_negative_numbers(list(range(-100, 100)))
    100
    >>> non_negative_numbers(list(range(0, 100)))
    100
    >>> non_negative_numbers(list(range(-100, 1)))
    1
    """
    high = len(nums) - 1
    low = 0
    output = 0
    if nums[-1] == 0:
        return 1
    while high >= low:
        mid = (high + low) // 2
        if nums[mid] >= 0:
            output = len(nums) - mid
            high = mid - 1
        elif nums[mid] < 0:
            low = mid + 1
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
