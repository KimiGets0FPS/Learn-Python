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
    count_list = []
    for k, v in count.items():
        count_list.append(v)
    return len(count_list) == len(set(count_list))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
