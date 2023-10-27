import unittest
from RLE import RLE

class Test(unittest.TestCase):
    def test_case1(self):
        result = RLE('')
        self.assertEqual(result, '')

    def test_case2(self):
        result = RLE('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB')
        self.assertEqual(result, 'A4B3C2XYZD4E3F3A6B28')

if __name__ == '__main__':
    unittest.main()