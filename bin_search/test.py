import unittest
from bin_search import bin_search

class Test(unittest.TestCase):
    def test_case1(self):
        result = bin_search([1, 3, 4, 5, 6, 7], 6)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()