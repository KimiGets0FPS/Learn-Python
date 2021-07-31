def solution(num: str) -> int:
    """
    >>> solution('32')
    3
    >>> solution('82734')
    8
    >>> solution('27346209830709182346')
    9
    """
    return max(num)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
