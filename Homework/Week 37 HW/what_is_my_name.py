import unittest


class Name:
    def __init__(self, firstname, lastname, middle_name=None):
        self.firstname = firstname
        self.lastname = lastname
        self.middle_name = middle_name

    def full_name(self):
        if self.middle_name:
            return f'{self.firstname.title()} {self.middle_name.title} {self.lastname.title()}'
        return f'{self.firstname.title()} {self.lastname.title()}'

    def first_name(self):
        return self.firstname.title()
    
    def last_name(self):
        return self.lastname.title()

    def initial(self):
        return f"{list(self.firstname)[0].title()}.{list(self.lastname)[0].title()}"


class Test(unittest.TestCase):
    def test_1(self):
        n1_var = Name('john', 'SMITH')
        test_1_var = n1_var.first_name()
        self.assertEqual(test_1_var, 'John')

    def test_2(self):
        n2_var = Name('john', 'SMITH')
        test_2_var = n2_var.last_name()
        self.assertEqual(test_2_var, 'Smith')

    def test_3(self):
        n3_var = Name('kimi', 'wan')
        test_var_3 = n3_var.initial()
        self.assertEqual(test_var_3, 'K.W')
        
    def test_4(self):
        n4_var = Name('kimi', 'wan')
        test_var_4 = n4_var.last_name()
        self.assertEqual(test_var_4, 'Wan')


if __name__ == "__main__":
    unittest.main()
