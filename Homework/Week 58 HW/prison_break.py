def prison_break(nums: list[int]) -> int:
    """
    >>> prison_break([1, 1, 0, 0, 0, 1, 0])
    4
    >>> prison_break([1, 0, 0, 0, 0, 0, 0])
    2
    >>> prison_break([1, 1, 1, 0, 0, 0])
    2
    >>> prison_break([1, 0, 1, 0, 1, 0])
    6
    >>> prison_break([1, 1, 1])
    1
    >>> prison_break([0, 0, 0])
    0
    >>> prison_break([0, 1, 1, 1])
    0
    """
    if nums[0] == 0:
        return 0
    output = 0
    replaced_list = []
    for i in range(len(nums)):
        if nums[i] == 0:
            replaced_list.append(1)
        else:
            replaced_list.append(0)
    locked_unlocked = True
    for i in range(len(nums)):
        if locked_unlocked is True:
            if nums[i] == 1:
                output += 1
                locked_unlocked = False
        else:
            if replaced_list[i] == 1:
                output += 1
                locked_unlocked = True
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
