# TODO: FINISH THIS PROBLEM
# LINK: https://leetcode.com/problems/concatenation-of-array/


def solution(nums: list[int]):
    """
    >>> solution([1, 2, 1])
    [1, 2, 1, 1, 2, 1]
    >>> solution([1, 3, 2, 1])
    [1, 3, 2, 1, 1, 3, 2, 1]
    """
    return nums*2


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
