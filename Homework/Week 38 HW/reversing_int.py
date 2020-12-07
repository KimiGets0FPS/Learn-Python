import unittest


def reverse_int(num):
    output = []
    i = 0
    m = 1
    ln = list(str(num))
    for _ in ln:
        ln[i] = int(ln[i])
        output.append(ln[i]*m)
        i += 1
        m *= 10
    return sum(output)


def way_two(n):
    return int(str(n)[::-1])


class Test(unittest.TestCase):
    def test_1(self):
        test_1_v = reverse_int(123)
        self.assertEqual(test_1_v, 321)

    def test_2(self):
        test_1_v = way_two(123)
        self.assertEqual(test_1_v, 321)


if __name__ == '__main__':
    unittest.main()
