def solution(costs: list[list[int]]) -> int:
    """
    >>> solution([[10, 20], [30, 200], [400, 50], [30, 20]])
    110
    >>> solution([[515, 563], [451, 713],[537, 709], [343, 819], [855, 779], [457, 60], [650, 359], [631, 42]])
    3086
    >>> solution([[10, 20], [30, 200]])
    50
    """
    output = 0
    for i in range(len(costs)):
        output += min(costs[i])
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
