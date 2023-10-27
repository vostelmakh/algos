import unittest
from max_ones_length import max_ones_length

class Test(unittest.TestCase):
    def test_case1(self):
        result = max_ones_length([0, 0, 1, 1, 0, 1, 1, 0])
        self.assertCountEqual(result, 4)

if __name__ == '__main__':
    unittest.main()