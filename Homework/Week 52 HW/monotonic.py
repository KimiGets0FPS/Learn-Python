def monotonic(nums: list[int]) -> bool:
    """
    >>> monotonic([1, 2, 2, 3])
    True
    """
    up = True
    down = True
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:  # checking if the previous number is smaller, if smaller, then it's descending.
            up = False
        elif nums[i] > nums[i-1]:  # checking if the previous number is bigger, if bigger, then it's descending.
            down = False
    return up or down  # if either one is True,  returns True, if none of them are True, then return False
    # Time complexity: O(n)


def another_way(nums: list[int]):
    """
    >>> another_way([1, 2, 2, 3])
    True
    """
    ...


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
