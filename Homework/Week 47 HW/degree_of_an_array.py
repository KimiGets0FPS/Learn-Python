def degree_of_an_array(nums):
    """
    >>> degree_of_an_array([1,2,2,3,1])
    2
    >>> degree_of_an_array([1,2,2,3,1,4,2])
    6
    """
    # counts = {}
    maximum_freq = 0
    for i in nums:  # Finding the maximum frequency number
        if nums.count(i) > maximum_freq:
            maximum_freq = i  # updating the maximum frequency number if larger
    for i in range(len(nums)):  # just getting rid of the first one
        if nums[i] == maximum_freq:
            break  # stops for loop
        else:
            nums.pop(i)  # gets rid of the useless number
    for i in range(len(nums)-1, -1, -1):  # reversed operation of the top one
        if nums[i] == maximum_freq:
            break  # stops the loop
        else:
            nums.pop(i)  # gets rid of the other useless number
    return len(nums)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
