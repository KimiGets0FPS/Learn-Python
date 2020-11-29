import unittest


class Name:
    def __init__(self, fname, lname, mname=None):
        self.fname = fname
        self.lname = lname
        self.mname = mname
    
    def fullname(self):
        if self.mname:
            return f'{self.fname.title()} {self.mname.title} {self.lname.title()}'
        return f'{self.fname.title()} {self.lname.title()}'

    def rfname(self):
        return self.fname.title()
    
    def rlname(self):
        return self.lname.title()

    def rinitial(self):
        return f"{list(self.fname)[0].title()}.{list(self.lname)[0].title()}"


class Test(unittest.TestCase):
    def test_1(self):
        n1_var = Name('john', 'SMITH')
        test_1_var = n1_var.rfname()
        self.assertEqual(test_1_var, 'John')

    def test_2(self):
        n2_var = Name('john', 'SMITH')
        test_2_var = n2_var.rlname()
        self.assertEqual(test_2_var, 'Smith')

    def test_3(self):
        n3_var = Name('kimi', 'wan')
        test_var_3 = n3_var.rinitial()
        self.assertEqual(test_var_3, 'K.W')
        
    def test_4(self):
        n4_var = Name('kimi', 'wan')
        test_var_4 = n4_var.rlname()
        self.assertEqual(test_var_4, 'Wan')


if __name__ == "__main__":
    unittest.main()
