import unittest
from find_k_nearest import find_k_neares


class Test(unittest.TestCase):
    def test_case1(self):
        result = find_k_neares([2, 3, 5, 7, 11], 3, 2)
        self.assertEqual(result, [7, 5])

    def test_case2(self):
        result = find_k_neares([4, 12, 15, 15, 24], 1, 3)
        self.assertEqual(result, [12, 15, 15])

    def test_case3(self):
        result = find_k_neares([2, 3, 5, 7, 11], 2, 2)
        self.assertEqual(result, [5, 3])


if __name__ == '__main__':
    unittest.main()
