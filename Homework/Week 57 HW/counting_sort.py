def counting_sort(nums: list[int]) -> list[int]:
    """
    >>> counting_sort([0, 2, 1, 5, 3, 4])
    [0, 1, 2, 3, 4, 5]
    >>> counting_sort([1, 3, 2, 5, 3, 2, 1, 5, 8, 9, 6, 4, 5])
    [1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 8, 9]
    """
    # Getting the maximum number
    max_num = 0
    for i in range(len(nums)):
        if max_num < nums[i]:
            max_num = nums[i]
    # Counting the numbers
    count = [0] * (max_num + 1)
    for i in range(len(count)):
        count[i] += 1
    output = [0] * (max_num + 1)
    for i in range(len(count)):
        output[i] = count[i]
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
