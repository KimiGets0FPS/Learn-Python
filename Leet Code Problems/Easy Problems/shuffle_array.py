def shuffle_array(nums: list[int], target: int) -> list[int]:
    """
    >>> shuffle_array([1, 1, 2, 2], 2)
    [1, 2, 1, 2]
    """
    output = []
    temp = len(nums) // 2
    for i in range(len(nums) // 2):
        output.append(nums[i])
        output.append(nums[temp])
        temp += 1
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
