def greatest_amount_of_candies(candies: list[int], extra: int) -> list[bool]:
    """
    >>> greatest_amount_of_candies([2,3,5,1,3])
    [True,True,True,False,True]
    """
    output = []
    most_candies = max(candies)
    for i in candies:
        if i + extra >= most_candies:
            output.append(True)
        else:
            output.append(False)
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
