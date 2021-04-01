def two_dif_sums(x: int, y: int, z: int) -> int:
    """
    >>> two_dif_sums(17, 25, 77)
    76
    >>> two_dif_sums(3, 5, 17)
    17
    """
    # Criteria: Given three numbers x, y and m where 1 <= x <= y <= m, use x and y to compose the largest possible
    # number that is <=m. You can use any number of x and y.
    output, multi1, multi2, range_num = 0, 0, 0, z // y
    for n in range(z // x + 1):
        for i in range(range_num + 1):
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
