import unittest
from find_medium_element import find_medium_element

class Test(unittest.TestCase):
    def test_case1(self):
        result = find_medium_element(1, 3, 4)
        self.assertEqual(result, 3)

    def test_case2(self):
        result = find_medium_element(4, 7, 5)
        self.assertEqual(result, 5)

    def test_case3(self):
        result = find_medium_element(8, 6, 10)
        self.assertEqual(result, 8)

    def test_case4(self):
        result = find_medium_element(0, 0, 0)
        self.assertEqual(result, 0)

    def test_case5(self):
        result = find_medium_element(30, 6, 10)
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()