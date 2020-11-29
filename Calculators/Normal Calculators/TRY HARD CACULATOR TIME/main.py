import unittest


class C:
    def __init__(self, *n):
        self.n = n

    @property
    def a(self):
        s = 0
        for i in self.n:
            s += i
        return s

    @property
    def s(self):
        cn = self.n[0]
        for a in self.n:
            cn -= a
        return cn

    @property
    def m(self):
        cn = 1
        for i in self.n:
            cn *= i
        return cn

    @property
    def d(self):
        cn = self.n[0]
        for i in self.n:
            cn /= i
        return cn




class Tests(unittest.TestCase):
    def test_1(self):
        c1v = C(1, 2, 3)
        t1v = c1v.a
        self.assertEqual(t1v, 6)

    def test_2(self):
        c1v = C(5, 3, 1)
        t1v = c1v.s
        self.assertEqual(t1v, 1)


if __name__ == "__main__":
    unittest.main()
