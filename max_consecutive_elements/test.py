import unittest
from max_consecutive_elements import max_consecutive_elements

class Test(unittest.TestCase):
    def test_case1(self):
        result = max_consecutive_elements('12333ff')
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()