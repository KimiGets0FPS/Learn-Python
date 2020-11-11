import unittest


def sum_of_two(num_1, num_2):
    """
    >>> sum_of_two('5125515215521515', '125261616261626')
    '5250776831783141'
    >>> sum_of_two('6666666666666666666666666666', '99999999999999999999999')
    '6666766666666666666666666665'
    >>> sum_of_two('123456789123456789123456789', '987654321987654321987654329876543')
    '987654445444443445444443453333332'
    """
    num_list_1 = list(num_1)
    num_list_2 = list(num_2)
    multiplier = 1
    i = -1
    for _ in num_list_1:
        num_list_1[i] = int(num_list_1[i])
        num_list_1[i] *= multiplier
        i -= 1
        multiplier *= 10
    multiplier = 1
    i = -1
    for _ in num_list_2:
        num_list_2[i] = int(num_list_2[i])
        num_list_2[i] *= multiplier
        i -= 1
        multiplier *= 10
    sum_1 = sum(num_list_1)
    sum_2 = sum(num_list_2)
    return str(sum_1 + sum_2)


class Test(unittest.TestCase):
    def test_if_correct(self):
        sum_of_num = sum_of_two('5125515215521515', '125261616261626')
        self.assertEqual(sum_of_num, '5250776831783141')


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    unittest.main()
