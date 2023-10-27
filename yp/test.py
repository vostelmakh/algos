import unittest
from NumberStorage import NumberStorage

class Test(unittest.TestCase):
    def test_case1(self):
        numbers = [2, 5, 7, 8, 4, 3, 1, 77, 33, 11]
        storage = NumberStorage(numbers)

        self.assertTrue(storage.has_number(3))

if __name__ == '__main__':
    unittest.main()