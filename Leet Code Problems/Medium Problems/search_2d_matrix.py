# TODO: FINISH THIS PROBLEM
# https://leetcode.com/problems/search-a-2d-matrix/


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """
    >>> search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
    True
    >>> search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)
    False
    >>> search_matrix([[1], [3], [5]], 5)
    True
    """
    high = len(matrix)
    low = 0
    mid = 0
    while high > low:
        mid = (high - low) // 2
        # print(mid)
        if matrix[mid][0] <= target <= matrix[mid][-1]:
            break
        elif matrix[mid][0] > target > matrix[mid][-1]:
            low = mid
        else:
            high = mid
    for i in range(len(matrix[mid])):
        if matrix[mid][i] == target:
            return True
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
