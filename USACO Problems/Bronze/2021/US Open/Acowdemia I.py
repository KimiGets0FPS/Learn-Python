# TODO: FINISH THIS PROBLEM
# LINK: http://usaco.org/index.php?page=viewproblem2&cpid=1131


def problem_1(n: int, l: int, nums: list[int]) -> int:
    """
    >>> problem_1(4, 0, [1, 100, 2, 3])
    2
    >>> problem_1(4, 1, [1, 100, 2, 3])
    2
    >>> problem_1(5, 1, [3, 0, 6, 1, 5])
    3
    >>> problem_1(3, 1, [1, 3, 1])
    1
    """
    h_index = 0  # the maximum h-index
    for i in range(n):
        count = 0
        for j in range(n):
            if nums[i] <= nums[j]:
                count += 1
        if count >= nums[i] > h_index:
            h_index = nums[i]
    return h_index


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
