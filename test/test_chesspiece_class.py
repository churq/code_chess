import unittest
from chess.core import *

class Test_ChessPiece(unittest.TestCase):
    def setUp(self):
        self.chess_piece = ChessPiece()
    def test_chessPiece_jump(self):
        self.assertIsNone(self.chess_piece.jump('a1','b3'))

    def test_chessPiece_isvalid_case1(self):
        self.assertEqual(self.chess_piece._isvalid(0, 1), False)

    def test_chessPiece_isvalid_case2(self):
        self.assertEqual(self.chess_piece._isvalid(1, 1), True)

    def test_chessPiece_isvalid_case3(self):
        self.assertEqual(self.chess_piece._isvalid(8, 1), True)

    def test_chessPiece_isvalid_case4(self):
        self.assertEqual(self.chess_piece._isvalid(9, 1), False)

    def test_chessPiece_isvalid_case5(self):
        self.assertEqual(self.chess_piece._isvalid(5, 1), True)

    def test_chessPiece_isvalid_case6(self):
        self.assertEqual(self.chess_piece._isvalid(1, 0), False)

    def test_chessPiece_isvalid_case7(self):
        self.assertEqual(self.chess_piece._isvalid(1, 1), True)

    def test_chessPiece_isvalid_case8(self):
        self.assertEqual(self.chess_piece._isvalid(1, 5), True)

    def test_chessPiece_isvalid_case9(self):
        self.assertEqual(self.chess_piece._isvalid(1, 8), True)

    def test_chessPiece_isvalid_case10(self):
        self.assertEqual(self.chess_piece._isvalid(1, 9), False)

    def test_num_to_letter(self):
        self.assertEqual(self.chess_piece._num_to_letter(1),'a')

    def test_letter_to_num(self):
        self.assertEqual(self.chess_piece._letter_to_num('h'), 8)

    def test_next_move_case1(self):
        self.assertIsNone(self.chess_piece.next_move((1,2,3)))

    def test_next_move_case2(self):
        self.assertIsNone(self.chess_piece.next_move([1, 4]))





            # def test_knight_case1(self):
    #     myknight = Knight()
    #     self.assertCountEqual(myknight.jump([1,1]),[(3,2),(2,3)])
    #
    # def test_knight_case2(self):
    #     myknight = Knight()
    #     self.assertCountEqual(myknight.jump([1, 4]), [(2, 2), (3, 3),(3,5),(2,6)])
    #
    # def test_knight_case3(self):
    #     myknight = Knight()
    #     self.assertCountEqual(myknight.jump([3, 4]), [(1, 5), (2, 6),(4, 6),(5, 5),(5, 3),(4, 2),(2, 2),(1, 3)])
    #
    #
    # def test_case1(self):
    #     self.assertEqual(analysis((1, 1),(4, 4)), True)
    # def test_case2(self):
    #     self.assertEqual(analysis((0, 1), (4, 4)), False)
    #
    # def test_case3(self):
    #     self.assertEqual(analysis((9, 1), (4, 4)), False)
    #
    # def test_case4(self):
    #     self.assertEqual(analysis((1, 0), (4, 4)), False)
    #
    # def test_case5(self):
    #     self.assertEqual(analysis((1, 9), (4, 4)), False)
    #
    # def test_case6(self):
    #     self.assertEqual(analysis((1, 1), (0, 4)), False)
    #
    # def test_case7(self):
    #     self.assertEqual(analysis((1, 1), (9, 4)), False)
    #
    # def test_case8(self):
    #     self.assertEqual(analysis((1, 1), (4, 0)), False)
    #
    # def test_case9(self):
    #     self.assertEqual(analysis((1, 1), (4, 9)), False)
