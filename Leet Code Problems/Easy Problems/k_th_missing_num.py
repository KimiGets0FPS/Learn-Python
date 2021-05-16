# TODO: WORK ON THIS


def kth_missing_num(nums: list[int], target: int) -> int:
    """
    >>> kth_missing_num([2, 3, 4, 7, 11], 5)
    9
    >>> kth_missing_num([1, 2, 3, 4], 2)
    6
    """
    expected = 0
    missing_num = 0
    for i in range(len(nums)):
        if expected != nums[i] and missing_num == target:
            return nums[i]
        elif expected == nums[i] or missing_num != target:
            missing_num += 1
            expected += 1


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
