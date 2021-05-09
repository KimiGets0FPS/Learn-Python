def three_consecutive_odds(nums: list[int]) -> bool:
    """
    >>> three_consecutive_odds([2, 6, 4, 1])
    False
    >>> three_consecutive_odds([1, 2, 34, 3, 4, 5, 7, 23, 12])
    True
    """
    count = 0
    for i in range(len(nums)):
        if nums[i] % 2 != 0:
            count += 1
        else:
            count = 0
        if count == 3:
            return True
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
