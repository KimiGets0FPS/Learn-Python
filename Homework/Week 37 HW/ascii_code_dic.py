import unittest


def characters_to_ascii(t):
    l=[]
    for i in t:  #? opposite of ord() is chr()
        l.append({i: ord(i)})
    return l


class Test(unittest.TestCase):
    def test_1(self):
        t1v = characters_to_ascii(["a", "b", "c"])
        self.assertEqual(t1v, [{"a": 97}, {"b": 98}, {"c": 99}])
        
    def test_2(self):
        t2v = characters_to_ascii(["^"])
        self.assertEqual(t2v, [{"^": 94}])
        
    def test_3(self):
        t3v = characters_to_ascii([])
        self.assertEqual(t3v, [])


if __name__ == "__main__":
    unittest.main()
