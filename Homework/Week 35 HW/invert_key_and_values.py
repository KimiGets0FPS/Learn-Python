import unittest


def key_and_values(input_dict):
    """
    >>> key_and_values({'z':'q', 'w':'f'})
    {'q': 'z', 'f': 'w'}
    >>> key_and_values({'a': 1, 'b':2, 'c':3})
    {1: 'a', 2: 'b', 3: 'c'}
    """
    copy_of_dict = input_dict.copy()
    input_dict.clear()
    for key, value in copy_of_dict.items():
        input_dict[value] = key
    return input_dict


class Test(unittest.TestCase):
    def test_if_correct(self):
        inverting = key_and_values({'a': 1, 'b': 2, 'c': 3})
        self.assertTrue(inverting, {1: 'a', 2: 'b', 3: 'c'})


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    unittest.main()
