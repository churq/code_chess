import unittest
from chess.myLib import *

class Test_Knight(unittest.TestCase):
    def setUp(self):
        self.knight = Knight()

    def test_instance_1(self):
        self.assertIsInstance(self.knight,Knight)


    def test_instance_2(self):
        self.assertIsInstance(self.knight, ChessPiece)
