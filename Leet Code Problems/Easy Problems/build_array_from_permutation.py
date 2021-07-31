def solution(nums: list[int]):
    """
    >>> solution([0, 2, 1, 5, 3, 4])
    [0, 1, 2, 4, 5, 3]
    >>> solution([5, 0, 1, 2, 3, 4])
    [4, 5, 0, 1, 2, 3]
    """
    output = []
    for i in range(len(nums)):
        output.append(nums[nums[i]])
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
