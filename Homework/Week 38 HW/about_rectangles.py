import unittest


class Rectangle:
    def __init__(self, width, length, color='red'):
        self.width = int(width)
        self.length = int(length)
        self.color = color

    @property
    def perimeter(self):
        return self.width*2+self.length*2

    @property
    def area(self):
        return self.width*self.length


class Test(unittest.TestCase):
    def test_1(self):
        class_1_v = Rectangle(4, 5)
        test_1_v = class_1_v.perimeter
        self.assertEqual(test_1_v, 18)

    def test_2(self):
        class_2_v = Rectangle(1, 2, 'blue')
        test_2_v = class_2_v.area
        self.assertEqual(test_2_v, 2)

    def test_3(self):
        class_3_v = Rectangle(3, 10)
        test_3_v = class_3_v.area
        self.assertEqual(test_3_v, 30)


if __name__ == "__main__":
    unittest.main()
