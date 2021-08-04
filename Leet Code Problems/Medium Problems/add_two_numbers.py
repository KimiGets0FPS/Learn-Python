# TODO: FINISH THIS PROBLEM
# https://leetcode.com/problems/add-two-numbers/


# list is actually linked list
def add_two_numbers(l1: list[int], l2: list[int]) -> list[int]:
    """
    >>> add_two_numbers([2, 4, 3], [5, 6, 4])
    [7, 0, 8]
    >>> add_two_numbers([0], [0])
    [0]
    >>> add_two_numbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9])
    [8, 9, 9, 9, 0, 0, 0, 1]
    """
    num1, num2 = [], []
    for i in range(len(l1)-1, -1, -1):
        num1.append(str(l1[i]))
    for i in range(len(l2)-1, -1, -1):
        num2.append(str(l2[i]))
    num1, num2 = int(''.join(num1)), int(''.join(num2))
    summed = list(str(num1 + num2))
    summed.reverse()
    for i in range(len(summed)):
        summed[i] = int(summed[i])
    return summed


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
