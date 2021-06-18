# TODO: FINISH THIS PROBLEM
# https://leetcode.com/problems/add-two-numbers/


def add_two_numbers(l1: list[int], l2: list[int]) -> list[int]:
    """
    >>> add_two_numbers([2, 4, 3], [5, 6, 4])
    [7, 0, 8]
    >>> add_two_numbers([0], [0])
    [0]
    >>> add_two_numbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9])
    [8, 9, 9, 9, 0, 0, 0, 1]
    """
    # Getting minimum length
    if len(l1) >= len(l2):
        min_len = len(l2)
    else:
        min_len = len(l1)
    # Adding the 2 numbers
    temp = []
    for i in range(min_len):
        temp.append(l1[i] + l2[i])
    # Adding the rest of the numbers that got left behind
    if len(l1) != len(l2):
        if min_len == len(l1):
            temp.append(l2[min_len:])
        elif min_len == len(l2):
            temp.append(l1[min_len:])
    # Getting the final output
    output = []
    for i in range(len(temp)-1):
        if temp[i] >= 10:
            temp[i+1] = 1
            temp[i] -= 10
    return temp


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
