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
    #* Seperating everything
    list_1 = list(num_1)
    list_2 = list(num_2)
    #* Making sure that everything is the same, so there aren't going to be any errors in the future.
    if len(list_1) != len(list_2):
        if len(list_1) > len(list_2):
            while len(list_1) != len(list_2):
                list_2.insert(0, '0')
        else:
            while len(list_1) != len(list_2):
                list_1.insert(0, '0')
    #* Making everything an integer for list_1
    i = 0
    for _ in list_1:
        list_1[i] = int(list_1[i])
        i+=1
    #* Making everything an integer for list_2
    i = 0
    for _ in list_2:
        list_2[i] = int(list_2[i])
        i+=1
    #* Calcualtion starts here
    i = -1
    for _ in list_1:
        list_1[i] += list_2[i]
        if list_1[i] >= 10:
            list_1[i-1] += 1
            list_1[i] -= 10
        list_1[i] = str(list_1[i])
        i -= 1
        #* Returning the final answer
    return ''.join(list_1)


def welp_right_but_wrong(num_1, num_2):
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
    
    def test_2(self):
        test_2_car = sum_of_two('6666666666666666666666666666', '99999999999999999999999')
        self.assertEqual(test_2_car, '6666766666666666666666666665')


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    unittest.main()
