def same_occurrence(nums: list[int]) -> bool:
    """
    >>> same_occurrence([1, 2, 2, 3, 3, 3])
    True
    >>> same_occurrence([1, 3, 2])
    False
    """
    count = {}
    for i in nums:
        count[i] = count.get(i, 0) + 1
    count_set = []
    for v in count.values():
        count_set.append(v)
    return len(count_set) == len(set(count_set))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
