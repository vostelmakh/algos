import unittest
from max_ones_length import max_ones_length

class Test(unittest.TestCase):
    def test_case1(self):
        result = max_ones_length( [0, 0, 1, 1, 0, 1, 1, 0] )
        self.assertEquals(result, 4)

    def test_case2(self):
        result = max_ones_length( [1, 1, 0] )
        self.assertEquals(result, 2)

    def test_case3(self):
        result = max_ones_length( [1, 0, 1, 1, 0] )
        self.assertEquals(result, 3)

    def test_case4(self):
        result = max_ones_length( [0, 1, 1, 0, 1, 1, 1, 0, 1, 1] )
        self.assertEquals(result, 5)

    def test_case5(self):
        result = max_ones_length( [1, 1, 1, 1, 1] )
        self.assertEquals(result, 5)

    def test_case6(self):
        result = max_ones_length( [0, 0, 0, 0, 0] )
        self.assertEquals(result, 0)

    def test_case7(self):
        result = max_ones_length( [] )
        self.assertEquals(result, 0)

if __name__ == '__main__':
    unittest.main()