def same_occurrence(nums: list[int]) -> bool:
    """
    >>> same_occurrence([1, 2, 2, 3, 3, 3])
    True
    >>> same_occurrence([1, 2, 3, 3])
    False
    """
    from collections import Counter
    cnt = Counter(nums)
    count_list = [cnt[key] for key in cnt]
    return len(count_list) == len(set(count_list))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
