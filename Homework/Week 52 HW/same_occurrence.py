def same_occurrence(nums: list[int]) -> bool:
    """
    >>> same_occurrence([1, 2, 2, 3, 3, 3])
    True
    >>> same_occurrence([1, 2, 3, 3])
    False
    """
    occ = {}
    for i, num in enumerate(nums):
        occ[num] = occ.get(num, 0) + 1  # finding the current number i, and if it doesn't find it, it sets the value
        # to 0 and + 1
    count = []
    for val in occ.values():
        count.append(val)
    return len(count) == len(set(count))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
