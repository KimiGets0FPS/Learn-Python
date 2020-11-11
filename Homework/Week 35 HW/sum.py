# >>> sum_of_two(5125515215521515, 125261616261626)
# 5250776831783141
# >>> sum_of_two('6666666666666666666666666666', '99999999999999999999999')
# '6666766666666666666666666665'
# >>> sum_of_two('123456789123456789123456789', '987654321987654321987654329876543')
# '987654445444443445444443453333332'


def sum_of_two(num_1, num_2):
    """
    >>> sum_of_two('123', '456')
    '581'
    """
    num_list_1 = list(num_1)
    num_list_2 = list(num_2)
    multiplier = 1
    i = 0
    for _ in num_list_1:
        num_list_1[i] = int(num_list_1[i])
        num_list_1[i] *= multiplier
        num_list_2[i] = int(num_list_2[i])
        num__list_2 *= multiplier
        multiplier *= 10
    return sum(num_list_1, num__list_2)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
