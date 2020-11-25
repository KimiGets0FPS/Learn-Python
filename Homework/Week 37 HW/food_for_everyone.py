import unittest



class Person:
    def __init__(self, name, like_food, hate_food):  #! like_food, hate_food --> list
        self.name = name
        self.like_food = like_food
        self.hate_food = hate_food
    
    def taste(self, inpt_food):
        if inpt_food in self.like_food:
            return f'{self.name.title()} eats {inpt_food} and likes it!'
        elif inpt_food in self.hate_food:
            return f'{self.name.title()} eats {inpt_food} and hates it!'
        else:
            return f'{self.name.title()} eats {inpt_food}.'  
        
        
class Test(unittest.TestCase):
    def test_1(self):
        p1_var = Person('Sam', ['ice cream', 'steak', 'hambugers'], ['grapes', 'apples', 'milk'])
        test_1_var = p1_var.taste('steak')
        self.assertEqual(test_1_var, 'Sam eats steak and likes it!')
    
    def test_2(self):
        p2_var = Person('john', ['grapes', 'apples', 'milk'], ['steak', 'hambuger', 'pizza'])
        test_2_var = p2_var.taste('steak')
        self.assertEqual(test_2_var, 'John eats steak and hates it!')
        
    def test_3(self):
        p3_var = Person('You', ['air'], ['pizza', 'grapes', 'apples', 'hambuger','milk'])
        test_3_var = p3_var.taste('dogs')
        self.assertEqual(test_3_var, 'You eats dogs.')


if __name__ == "__main__":
    unittest.main()
