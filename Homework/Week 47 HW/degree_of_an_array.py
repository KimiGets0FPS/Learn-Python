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


def dict_way(nums):
    """
    >>> degree_of_an_array([3, 1, 2, 2, 3, 1])
    2
    >>> degree_of_an_array([1, 2, 2, 3, 1, 4, 2])
    6
    """
    length = {}
    count = {}
    for i in nums:
        if i in count:
            count[i] += 1
        else:
            count[i] = 0
    maximum_list = []
    maximum_ = 0
    for i in count:
        if count[i] > maximum_:
            maximum_ = count[i]
    maximum_list.append(i for i in count if i == maximum_)  # oh yeah just one line
    for x in maximum_list:
        for y in range(len(nums)):  # just getting rid of the first one
            if nums[y] == count[x]:
                break  # stops for loop
            else:
                count -= 1
        for z in range(len(nums) - 1, -1, -1):  # reversed operation of the top one
            if nums[z] == count[x]:
                break  # stops the loop
            else:
                count -= 1
        length[x] = count
    min_val = length
    return [i for i in length if length[i] > min_val]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
