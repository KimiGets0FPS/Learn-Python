import unittest


def next_letter(word):
    output = []
    letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
            't', 'u', 'v', 'w', 'x', 'y', 'z']
    letters = list(word)
    for letter in letters:
        i = 0
        while letter != letter_list[i]:
            i += 1
        output.append(letter_list[i+1])
    return ''.join(output)


class Test(unittest.TestCase):
    def test_1(self):
        test_1_var = next_letter('hi')
        self.assertEqual(test_1_var, 'ij')
    def test_2(self):
        test_2_var = next_letter('hello')
        self.assertEqual(test_2_var, 'ifmmp')
        

if __name__ == "__main__":
    unittest.main()
