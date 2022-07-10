def how_many_smaller_nums(nums: list[int]) -> list[int]:
    """
    >>> how_many_smaller_nums([8, 1, 2, 2, 3])
    [4, 0, 1, 1, 3]
    >>> how_many_smaller_nums([6, 5, 4, 8])
    [2, 1, 0, 3]
    >>> how_many_smaller_nums([7, 7, 7, 7])
    [0, 0, 0, 0]
    """
    output = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                count += 1
        output.append(count)
    return output


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
