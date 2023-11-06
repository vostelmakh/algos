import unittest
from binary_search import binary_search

class Test(unittest.TestCase):
    def test_case1(self):
        result = binary_search([1, 3, 4, 5, 6, 7], 6)
        self.assertTrue(result)

    def test_case2(self):
        result = binary_search([1, 5], 6)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
