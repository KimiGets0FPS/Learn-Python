def find_index(nums: list[int], target: int) -> int:
    """
    >>> find_index([1, 3, 5, 6], 5)
    2
    >>> find_index([1, 3, 5, 6], 2)
    1
    """
    # Criteria: Given a sorted array of distinct integers and a target value, return the index if the target is
    # found. If not, return the index where it would be if it were inserted in order.
    if target not in nums:
        nums.append(target)
        return sorted(nums).index(target)
    for i in nums:
        if i == target:
            return nums.index(i)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
