def degree_of_an_array(nums):
    output = len(nums)
    maximum_freq = 0
    for i in nums:  # Finding the maximum frequency number
        if nums.count(i) > maximum_freq:
            maximum_freq = i  # updating the maximum frequency number if larger
    for i in range(len(nums)):  # just getting rid of the first one
        if nums[i] == maximum_freq:
            break  # stops for loop
        else:
            output -= 1
    for i in range(len(nums)-1, -1, -1):  # reversed operation of the top one
        if nums[i] == maximum_freq:
            break  # stops the loop
        else:
            output -= 1
    return output


def working_way(nums):
    """
    >>> working_way([3, 1, 2, 2, 3, 1])
    2
    """
    max_num = 0
    maximum_l = []
    for i in nums:
        count = nums.count(i)
        if count > max_num:
            maximum_l.clear()
            max_num = count
        if count == max_num:
            maximum_l.append(i)
    output = {}
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

    # max_out = 0
    # for i in output:
    #     if output[i] > max_out:
    #         max_out = i
    # return max_out


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
