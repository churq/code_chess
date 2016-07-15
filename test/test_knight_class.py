import unittest
from chess.core import *

class Test_Knight(unittest.TestCase):
    def setUp(self):
        self.knight = Knight()

    def test_instance_1(self):
        self.assertIsInstance(self.knight,Knight)


    def test_instance_2(self):
        self.assertIsInstance(self.knight, ChessPiece)

# myknight = Knight()
#     self.assertCountEqual(myknight.jump([1, 4]), [(2, 2), (3, 3),(3,5),(2,6)])
#
    def test_next_move_case1(self):
        self.assertCountEqual(self.knight.next_move([3, 4]), [(1, 5), (2, 6),(4, 6),(5, 5),(5, 3),(4, 2),(2, 2),(1, 3)])

    def test_next_move_case2(self):
        self.assertCountEqual(self.knight.next_move([1, 4]), [(2, 2), (3, 3), (3, 5), (2, 6)])

