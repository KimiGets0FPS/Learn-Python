# TODO: SUBMIT THIS PROBLEM
# https://leetcode.com/problems/kth-missing-positive-number/


def kth_missing_num(nums: list[int], target: int) -> int:
    """
    >>> kth_missing_num([2, 3, 4, 7, 11], 5)
    9
    >>> kth_missing_num([1, 2, 3, 4], 2)
    6
    """
    expected = 0
    count = 0  # Counting the xth missing number
    for i in range(len(nums), 1):
        if nums[i] != expected:
            count += 1
            expected += 1
        elif nums[i] == expected:
            expected += 1
    return count


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
