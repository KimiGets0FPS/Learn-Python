import unittest


def how_many_int(num_List, output={}):
    for i in num_List:
        output[i] = output.get(i, 0) + 1
    return output


class Test(unittest.TestCase):
    def test_1(self):
        test_1_v = how_many_int([1, 2, 3, 1, 2, 3])
        self.assertEqual(test_1_v, {1: 2, 2: 2, 3: 2})


if __name__ == '__main__':
    unittest.main()
