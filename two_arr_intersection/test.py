import unittest
from arrays_intersection import arrays_intersection

class Test(unittest.TestCase):
    def test_case1(self):
        result = arrays_intersection([1, 2, 3, 2, 0], [5, 1, 2, 7, 3, 2])
        self.assertEqual(len(result), 4)

    def test_case2(self):
        result = arrays_intersection([], [])
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()