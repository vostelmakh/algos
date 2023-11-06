import unittest
from longest_increasing_subsequence import longest_increasing_subsequence


class Test(unittest.TestCase):
    def test_case1(self):
        result = longest_increasing_subsequence([2, 3, 6, 4, 1, 3, 5, 4, 7])
        self.assertEqual(result, 5)

    def test_case2(self):
        result = longest_increasing_subsequence([])
        self.assertEqual(result, 0)

    def test_case3(self):
        result = longest_increasing_subsequence([1])
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
