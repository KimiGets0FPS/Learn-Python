# TODO: EXCEED TIME LIMIT O(N)^2 TOO MUCH

def count_smaller_nums_after(nums: list[int]) -> list[int]:
    """
    >>> count_smaller_nums_after([5, 2, 6, 1])
    [2, 1, 1, 0]
    >>> count_smaller_nums_after([-1])
    [0]
    >>> count_smaller_nums_after([-1, -1])
    [0, 0]
    """
    output = []
    for i in range(len(nums)):
        count = 0
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                count += 1
        output.append(count)
    return output


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
