import unittest


class Name:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def return_full_name(self):
        return f"{self.fname.title()} {self.lname.title()}"

    def return_initial(self):
        return f"{list(self.fname)[0].title()}.{list(self.lname)[0].title()}"
    
    
class Test(unittest.TestCase):
    def test_1(self):
        n1_var = Name('john', 'SMITH')
        test_1_var = n1_var.return_full_name()
        self.assertEqual(test_1_var, 'John Smith')

    def test_2(self):
        n2_var = Name('john', 'SMITH')
        test_2_var = n2_var.return_initial()
        self.assertEqual(test_2_var, 'J.S')

    def test_3(self):
        n3_var = Name('kimi', 'wan')
        test_var_3 = n3_var.return_full_name()
        self.assertEqual(test_var_3, 'Kimi Wan')
        
    def test_4(self):
        n4_var = Name('kimi', 'wan')
        test_var_4 = n4_var.return_initial()
        self.assertEqual(test_var_4, 'K.W')


if __name__ == "__main__":
    unittest.main()