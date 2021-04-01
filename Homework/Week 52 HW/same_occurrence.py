def same_occurrence(nums: list[int]) -> bool:
    """
    >>> same_occurrence([1, 2, 2, 3, 3, 3])
    True
    >>> same_occurrence([1, 2, 3, 3])
    False
    """
    occ = {}
    for i in nums:
        if i in occ:  # finding the current number i, and if it doesn't find it, it sets the value
            occ[i] = 0
        occ[i] += 1
        # to 0 and + 1
    count = []
    for val in occ.values():
        count.append(val)
    return len(count) == len(set(count))


def another_way(nums: list[int]) -> bool:
    """
    >>> another_way([1, 2, 2, 3, 3, 3])
    True
    >>> another_way([1, 2, 3, 3])
    False
    """
    from collections import Counter
    counts = []
    for i in Counter(nums):
        counts.append(Counter(nums)[i])
    return len(counts) == len(set(counts))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
