def third_max(nums: list[int]):
    """
    >>> third_max([1, 2, 3])
    1
    >>> third_max([1, 2])
    2
    >>> third_max([2, 1, 4, 3])
    2
    >>> third_max([2, 1, 3, 3, 2, 4, 5])
    3
    """
    maximums = set()  # defining a set
    for num in nums:
        maximums.add(num)  # adding the nums into the maximums without duplicates
        if len(maximums) > 3:  # checking if len(maximums) is bigger than three
            maximums.remove(min(maximums))  # just remove the useless small number
    if len(maximums) == 3:
        return min(maximums)  # if the length of maximums is 3 then just return the smallest number
    return max(maximums)  # else then just return the biggest boi
    # Time complexity: O(n)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
