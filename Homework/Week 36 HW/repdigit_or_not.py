import unittest


def repdigit(num):
    if num < 0:
        return False
    num = str(num)
    for i in range(len(num)):
        if num[i] != num[i-1]:
            return False
    return True
        
def repdigit_2(num):
    return all(list(str(num)))

class Test(unittest.TestCase):
    def test_1(self):
        
        test_1_var = repdigit_2(11)
        self.assertEqual(test_1_var, True)
    
    def test_2(self):
        test_2_var = repdigit_2(123)
        self.assertEqual(test_2_var, False)


if __name__ == "__main__":
    unittest.main()
