def fibonacci_num(end: int) -> int:
    """
    >>> fibonacci_num(0)
    0
    >>> fibonacci_num(269)
    73822750993122698578207436143903804565580923764844306069
    >>> fibonacci_num(275)
    1324695516964754142521850507284930515811378128425638237225
    """
    num1, num2 = 0, 1
    output = [0, 1]
    for _ in range(end):
        num1, num2 = num2, num1 + num2
        output.append(num2)
    return output[end]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
