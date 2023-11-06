import unittest
from arr2interval import arr2interval


class Test(unittest.TestCase):
    def test_case1(self):
        result = arr2interval([1, 4, 5, 2, 3, 9, 8, 11, 0])
        self.assertEqual(result, "0-5,8-9,11")

    def test_case2(self):
        result = arr2interval([1, 4, 3, 2])
        self.assertEqual(result, "1-4")

    def test_case3(self):
        result = arr2interval([1, 4])
        self.assertEqual(result, "1,4")


if __name__ == '__main__':
    unittest.main()
