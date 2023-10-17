def jewels_and_stones(jewels: str, stones: str) -> int:
    """
    >>> jewels_and_stones('aA', 'aAbBcCdD')
    2
    """
    output = {}
    for i in jewels:
        output[i] = stones.count(i)
    return sum(output.values())


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
