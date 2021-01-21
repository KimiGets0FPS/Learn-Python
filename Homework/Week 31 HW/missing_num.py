def what_is_the_missing_num(num_list):
    """
    >>> what_is_the_missing_num([5, 3, 1, 0, 4])
    2
    >>> what_is_the_missing_num([1, 0, 2])
    3
    >>> what_is_the_missing_num([2, 1, 3])
    0
    """
    num_list.sort()
    if 0 not in num_list:
        return 0
    for num in num_list:
        next_num = num + 1
        if next_num not in num_list:
            return next_num


def another_way(nums):
    """
    >>> another_way([5, 3, 1, 0, 4])
    2
    >>> another_way([1, 0, 2])
    3
    >>> another_way([2, 1, 3])
    0
    """
    nums.sort()
    if nums[-1] != len(nums):  # just checking if n is the last index
        return len(nums)
    elif nums[0] != 0:
        return 0
    for i in range(1, len(nums)):
        expected_num = nums[i - 1] + 1
        if nums[i] != expected_num:
            return expected_num


def another_one(list_num):  # works in most cases though :\
    """
    >>> another_way([5, 3, 1, 0, 4])  # ordered my_list is 0, 1, 3, 4, 5
    2
    >>> another_way([1,0,2])
    3
    >>> another_way([2, 1, 3])
    0
    """
    list_num.sort()
    if list_num[0] != 0:
        return 0
    for i in range(1, len(list_num)):
        expected_num = list_num[i - 1] + 1
        if list_num[i] != expected_num:
            return expected_num


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
