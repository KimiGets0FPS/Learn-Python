import unittest


def pluralize(words: list) -> list:
    output = []
    for i in words:
        if words.count(i) < 2:
            output.append(i)
        elif i + 's' not in output:
            output.append(i + 's')
    return output
    # Time complexity: O(n)
    # Space complexity: O(n)


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(pluralize(["cow", "pig", "cow", "cow"]), ['cows', 'pig'])

    def test_2(self):
        self.assertEqual(pluralize(["table", "table", "table"]), ['tables'])


if __name__ == '__main__':
    unittest.main(verbosity=True)
