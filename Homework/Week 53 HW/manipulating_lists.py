def manipulating_lists(nums: list[int] or list[list[int]]) -> list[int] or list[list[int]]:
    """
    >>> manipulating_lists([1, 2, 3, 4])
    [[1], [2], [3], [4]]
    >>> manipulating_lists([[5], [6], [9]])
    [5, 6, 9]
    >>> manipulating_lists([])
    []
    """
    output = []
    if nums:
        if isinstance(nums[0], list):  # nested list scenario
            for i in nums:
                output.append(i[0])
        else:
            for i in nums:
                output.append([i])
    return output
    # Time complexity: O(n)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
