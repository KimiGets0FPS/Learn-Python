def largest_num_once(nums: list[int]):
    """
    >>> largest_num_once([1, 1, 2, 3, 3])
    2
    >>> largest_num_once([1, 2, 2, 3])
    3
    """
    temp = {}
    for i in nums:
        if temp[i] is None:  # TIME COMPLEXITY: O(1)!!!
            temp[i] = 0
        temp[i] += 1
    max_val = 0
    for x, y in temp.items():
        if y == 0 and max_val > x:
            return x
    return -1
    # Time complexity: O(n)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
