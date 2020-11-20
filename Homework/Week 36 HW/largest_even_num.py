import unittest


def largest_even_num(num):
    largest_num = 0
    for current_num in num:
        if current_num > largest_num and current_num % 2 == 0:
            largest_num = current_num
    return largest_num


class Test(unittest.TestCase):
    def test_1(self):
        test_1_var = largest_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(test_1_var, 10)
    
    def test_2(self):
        test_2_var = largest_even_num([0])
        self.assertEqual(test_2_var, 0)
    
    def test_3(self):
        test_3_var = largest_even_num([1, 2, 7])
        self.assertEqual(test_3_var, 2)
    
    def test_4(self):
        test_4_var = largest_even_num([-2, 0, 5])
        self.assertEqual(test_4_var, 0)
    
    def test_5(self):
        test_5_var = largest_even_num([-2])
        self.assertEqual(test_5_var, 0)


if __name__ == "__main__":
    unittest.main()
