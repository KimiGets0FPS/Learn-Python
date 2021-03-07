def degree_of_an_array(nums):
    """
    >>> degree_of_an_array([3, 3, 1, 2, 2, 1])
    2
    """
    max_num = 0
    maximum_l = []
    output = {}
    for i in nums:
        count = nums.count(i)
        if count > max_num:
            maximum_l.clear()
            max_num = count
        if count == max_num:
            maximum_l.append(i)
    for i in maximum_l:
        count_nums = len(nums)
        for x in maximum_l:
            if x == i:
                break
            else:
                count_nums -= 1
        for y in reversed(maximum_l):
            if y == i:
                break
            else:
                count_nums -= 1
        output[i] = count_nums
    min_value = output[1]
    for key, value in output.items():
        if value < min_value:
            min_value = value
    return min_value


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
