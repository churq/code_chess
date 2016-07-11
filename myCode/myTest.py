import unittest
from myLib import *

class MyTest(unittest.TestCase):
    def test_knight_case1(self):
        myknight = knight()
        self.assertCountEqual(myknight.jump([1,1]),[(3,2),(2,3)])

    def test_knight_case2(self):
        myknight = knight()
        self.assertCountEqual(myknight.jump([1, 4]), [(2, 2), (3, 3),(3,5),(2,6)])

    def test_knight_case3(self):
        myknight = knight()
        self.assertCountEqual(myknight.jump([3, 4]), [(1, 5), (2, 6),(4, 6),(5, 5),(5, 3),(4, 2),(2, 2),(1, 3)])


    def test_case1(self):
        self.assertEqual(analysis((1, 1),(4, 4)), True)
    def test_case2(self):
        self.assertEqual(analysis((0, 1), (4, 4)), False)

    def test_case3(self):
        self.assertEqual(analysis((9, 1), (4, 4)), False)

    def test_case4(self):
        self.assertEqual(analysis((1, 0), (4, 4)), False)

    def test_case5(self):
        self.assertEqual(analysis((1, 9), (4, 4)), False)

    def test_case6(self):
        self.assertEqual(analysis((1, 1), (0, 4)), False)

    def test_case7(self):
        self.assertEqual(analysis((1, 1), (9, 4)), False)

    def test_case8(self):
        self.assertEqual(analysis((1, 1), (4, 0)), False)

    def test_case9(self):
        self.assertEqual(analysis((1, 1), (4, 9)), False)

if __name__=='__main__':
    unittest.main()