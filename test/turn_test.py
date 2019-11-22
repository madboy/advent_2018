from src.tools import turn
import unittest


class TurnTest(unittest.TestCase):
    def test_turn_left_f(self):
        self.assertEqual("down", turn("left", "left"))
        self.assertEqual("left", turn("up", "left"))
        self.assertEqual("up", turn("right", "left"))
        self.assertEqual("right", turn("down", "left"))

    def test_turn_right_f(self):
        self.assertEqual("up", turn("left", "right"))
        self.assertEqual("right", turn("up", "right"))
        self.assertEqual("down", turn("right", "right"))
        self.assertEqual("left", turn("down", "right"))

    def test_turn_straight_f(self):
        self.assertEqual("left", turn("left", "straight"))
        self.assertEqual("up", turn("up", "straight"))
        self.assertEqual("right", turn("right", "straight"))
        self.assertEqual("down", turn("down", "straight"))
