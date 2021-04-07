def good_pairs(nums: list[int]) -> int:
    """
    >>> good_pairs([1, 2, 1, 2])
    2
    """
    output = 0
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if x == y and i < j:
                output += 1
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
