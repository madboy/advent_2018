from src.eleven import (
    power_level,
    summed_area_table,
    rectangle_sum,
    compute_for_grid_size,
)
import unittest


class DayElevenTests(unittest.TestCase):
    def test_power_level(self):
        self.assertEqual(4, power_level(3, 5, 8))
        self.assertEqual(-5, power_level(122, 79, 57))
        self.assertEqual(0, power_level(217, 196, 39))
        self.assertEqual(4, power_level(101, 153, 71))

    def test_summed_area_intensity_serial_42(self):
        sat = summed_area_table(42, 300)
        self.assertEqual(119, rectangle_sum(sat, 232, 251, 12))

    def test_summed_area_intensity_serial_18(self):
        sat = summed_area_table(18, 300)
        self.assertEqual(113, rectangle_sum(sat, 90, 269, 16))

    @unittest.skip
    def test_square_power_level_18_variable_size(self):
        size = 300
        sat = summed_area_table(18, size)

        best_gs = 0
        best_spl = -1000
        best_top_left = (1, 1)
        for grid_size in range(2, 300):
            top_left, spl = compute_for_grid_size(sat, size, grid_size)
            if spl > best_spl:
                best_spl = spl
                best_top_left = top_left
                best_gs = grid_size

        self.assertEqual((90, 269), best_top_left)
        self.assertEqual(113, best_spl)
        self.assertEqual(16, best_gs)
