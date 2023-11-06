import unittest
from find_range import find_range_with_target_sum


class Test(unittest.TestCase):
    def test_case1(self):
        nums = [1, 2, 4, 4, 3, 2, 1]
        result = find_range_with_target_sum(nums, 9)
        self.assertEqual(sum(nums[result[0]:result[1]]), 9)


if __name__ == '__main__':
    unittest.main()
