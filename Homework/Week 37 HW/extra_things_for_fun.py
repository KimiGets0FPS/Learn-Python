import unittest
import codecs


def turn_things_to_hex(t):
    l = list(t)
    lc = []
    for i in l:
        lc.append(i.encode("utf-8").hex())
    return ' '.join(lc)
    


class Test(unittest.TestCase):
    def test_1(self):
        test_1_var = turn_things_to_hex('hello world')
        self.assertEqual(test_1_var, '68 65 6c 6c 6f 20 77 6f 72 6c 64')
    def test_2_var(self):
        test_2_var = turn_things_to_hex('Big Boi')
        self.assertEqual(test_2_var, '42 69 67 20 42 6f 69')
    def test_3(self):
        test_3_var = turn_things_to_hex('your mom')
        self.assertEqual(test_3_var, '79 6f 75 72 20 6d 6f 6d')


if __name__ == "__main__":
    unittest.main()
