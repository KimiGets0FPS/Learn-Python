def running_sum(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        nums[i] = nums[i - 1] + nums[i]
    return nums


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
