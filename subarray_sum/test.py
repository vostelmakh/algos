import unittest
from subarray_sum import subarray_sum

class Test(unittest.TestCase):
    def test_case1(self):
        result = subarray_sum([1, 3, 4, 5, 5, 6, 7], 7)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()