import unittest
from find_substring import find


class Test(unittest.TestCase):
    def test_case1(self):
        result = find("eceeba", 2)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
