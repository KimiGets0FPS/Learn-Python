import unittest


def repdigit(num):
    """
    >>> repdigit(1243)
    False
    >>> repdigit(11)
    True
    >>> repdigit(-11)
    False
    """
    if num < 0:
        return False
    if num == 0:
        return True
    num = str(num)
    nums = list(num)
    i = 0
    for _ in nums:
        nums[i] = int(nums[i])
        i += 1
    i = 0
    for x in nums:
        previous_num = nums[i-1]
        if x != previous_num:
            return False
        i += 1
    return True
        
    

class Test(unittest.TestCase):
    def test_1(self):
        test_1_var = repdigit(11)
        self.assertEqual(test_1_var, True)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    unittest.main()
