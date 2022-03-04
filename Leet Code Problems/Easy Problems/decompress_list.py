def decompress_list(nums: list[int]) -> list[int]:
    """
    >>> decompress_list([1, 1, 2, 3])
    [1, 3, 3]
    >>> decompress_list([1, 2, 3, 4])
    [2, 4, 4, 4]
    """
    output = []
    for i in range(0, len(nums), 2):
        output.extend([nums[i+1]] * nums[i])
    return output


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
