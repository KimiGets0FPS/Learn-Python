import unittest


def largest_even_num(num):
    """
    >>> largest_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    10
    """
    largest_num = 0
    for current_num in num:
        if current_num > largest_num and current_num % 2 == 0:
            largest_num = current_num
    return largest_num
    
    
class Test(unittest.TestCase):
    def test_1(self):
        test_1_var = largest_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(test_1_var, 10)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    unittest.main()
