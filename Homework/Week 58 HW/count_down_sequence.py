# TODO: FINISH THIS PROBLEM
# https://edabit.com/challenge/KveKxSD9t8fX7ybSt


def count_down_sequence(nums: list[int]) -> list[int, list[int]]:
    """
    >>> count_down_sequence([4, 8, 3, 2, 1, 2])
    [1, [[3, 2, 1]]]
    """
    # haha yes counting sort
    max_num = 0
    for i in range(len(nums)):
        if max_num < nums[i]:
            max_num = nums[i]
    count = [0] * (max_num + 1)
    for i in range(len(nums)):
        count[nums[i]] += 1
    sorted_nums = []
    for i in range(len(count)):
        while count[i] != 0:
            sorted_nums.append(i)
            count[i] -= 1
    # now the other stuff
    output = []
    for i in range(len(sorted_nums)):
        for j in range(len(sorted_nums)):
            ...
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
