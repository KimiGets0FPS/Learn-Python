import math


def largest_num_once(nums: list[int]):
    """
    >>> largest_num_once([1, 1, 2, 3, 3])
    2
    >>> largest_num_once([1, 2, 2, 3])
    3
    >>> largest_num_once([2, 1, 4, 5, 2, 1, 4])
    5
    >>> largest_num_once([1, 2, 2, 4])
    4
    >>> largest_num_once([-5, -2, -3])
    -2
    """
    # Criteria: Find the largest number in a list that only appeared once
    temp = {}
    for i in nums:
        if i not in temp:  # Had to use this because that one didn't work
            temp[i] = 0
        temp[i] += 1
    max_val = -math.inf
    for x, y in temp.items():
        if y == 1 and max_val < x:
            max_val = x
    if max_val == -math.inf:
        return -1
    return max_val
    # Time complexity: O(n)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
