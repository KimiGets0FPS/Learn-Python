def two_dif_sums(x: int, y: int, z: int) -> int:
    """
    >>> two_dif_sums(17, 25, 77)
    76
    """
    # Criteria: Given three numbers x, y and m where 1 <= x <= y <= m, use x and y to compose the largest possible
    # number that is <=m. You can use any number of x and y.
    output = 0
    range_num = 0
    temp_multi = 0
    multi1, multi2 = 0, 0
    while True:
        if temp_multi * y <= z:
            range_num = temp_multi
            temp_multi += 1
        else:
            break
    for n in range(x):
        for i in range(range_num):
            temp = x * multi1 + y * multi2
            if output <= temp <= z:
                output = temp
            elif temp == z:
                return z
            elif temp > z:
                break
            multi2 += 1
        multi1 += 1
        multi2 = 0
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
