from src.eleven import (
    power_level,
    find_largest_power_level,
    populate_grid,
    compute_square_power_level,
)
import unittest


class DayElevenTests(unittest.TestCase):
    def test_power_level(self):
        self.assertEqual(4, power_level(3, 5, 8))
        self.assertEqual(-5, power_level(122, 79, 57))
        self.assertEqual(0, power_level(217, 196, 39))
        self.assertEqual(4, power_level(101, 153, 71))

    def test_compute_square_power_level(self):
        grid = {
            (1, 1): 1,
            (1, 2): 1,
            (2, 1): 1,
            (2, 2): 1,
        }
        computed_grid = {
            (1, 1): 1,
            (1, 2): 1,
            (2, 1): 1,
            (2, 2): 1,
        }

        r = compute_square_power_level(1, 1, grid, 2, computed_grid)
        self.assertEqual(4, r)

    def test_compute_square_power_level_successive(self):
        grid = {
            (1, 1): 1,
            (1, 2): 1,
            (1, 3): 1,
            (2, 1): 1,
            (2, 2): 1,
            (2, 3): 1,
            (3, 1): 1,
            (3, 2): 1,
            (3, 3): 1,
        }
        computed_grid = {}

        r = compute_square_power_level(1, 1, grid, 1, computed_grid)
        self.assertEqual(1, r)

        r = compute_square_power_level(1, 1, grid, 2, computed_grid)
        self.assertEqual(4, r)

        r = compute_square_power_level(1, 1, grid, 3, computed_grid)
        self.assertEqual(9, r)

    def test_square_power_level_18(self):
        grid = populate_grid(18)
        top_left, pl, gs = find_largest_power_level(grid, 1, 4)
        self.assertEqual((33, 45), top_left)
        self.assertEqual(29, pl)
        self.assertEqual(3, gs)

    def test_square_power_level_42(self):
        grid = populate_grid(42)
        top_left, pl, gs = find_largest_power_level(grid, 1, 4)
        self.assertEqual((21, 61), top_left)
        self.assertEqual(30, pl)
        self.assertEqual(3, gs)

    def test_find_largest_power_level_ones(self):
        grid = {
            (1, 1): 1,
            (1, 2): 1,
            (2, 1): 1,
            (2, 2): 1,
        }
        top_left, pl, gs = find_largest_power_level(grid, 1, 3)
        self.assertEqual((1, 1), top_left)
        self.assertEqual(2, gs)
        self.assertEqual(4, pl)

    @unittest.skip
    def test_square_power_level_18_variable_size(self):
        grid = populate_grid(18)
        top_left, pl, gs = find_largest_power_level(grid, 1, 300)
        self.assertEqual((90, 269), top_left)
        self.assertEqual(113, pl)
        self.assertEqual(16, gs)

    @unittest.skip
    def test_square_power_level_42_variable_size(self):
        grid = populate_grid(42)
        top_left, pl, gs = find_largest_power_level(grid, 1, 300)
        self.assertEqual((232, 251), top_left)
        self.assertEqual(119, pl)
        self.assertEqual(12, gs)
