"""
Given a 300x300 grid of fuel cells select the 3x3 (1) or variable size (2) cell 
square that has the largest total power
"""
from src.tools import process


def power_level(x, y, grid_serial_number):
    rack_id = x + 10
    power_lvl = rack_id * y
    power_lvl += grid_serial_number
    power_lvl *= rack_id
    # keep only the hundreds digit, if below 100 -> 0
    power_lvl = (power_lvl // 100) % 10
    return power_lvl - 5


def summed_area_table(grid_serial_number, size):
    summed_grid = {}
    for y in range(1, size + 1):
        for x in range(1, size + 1):
            summed_grid[(x, y)] = (
                power_level(x, y, grid_serial_number)
                + summed_grid.get((x, y - 1), 0)
                + summed_grid.get((x - 1, y), 0)
                - summed_grid.get((x - 1, y - 1), 0)
            )
    return summed_grid


def rectangle_sum(sat, x, y, w):
    return (
        sat.get((x - 1, y - 1))
        + sat.get((x + w - 1, y + w - 1))
        - sat.get((x - 1, y + w - 1))
        - sat.get((x + w - 1, y - 1))
    )


def compute_for_grid_size(summed_table, size, grid_size):
    current_spl = -1000
    top_left = (1, 1)
    for x in range(2, size + 1):
        for y in range(2, size + 1):
            if (x + grid_size - 1) > size or (y + grid_size - 1) > size:
                continue

            spl = rectangle_sum(summed_table, x, y, grid_size)
            if spl > current_spl:
                top_left = (x, y)
                current_spl = spl
    return top_left, current_spl


def run(input_file):
    for grid_serial_number in process(input_file):
        grid_serial_number = int(grid_serial_number)
        size = 300
        summed_table = summed_area_table(grid_serial_number, size)

        # part 1
        print(compute_for_grid_size(summed_table, size, 3))

        # # part 2
        best_gs = 0
        best_spl = -1000
        best_top_left = (1, 1)
        for grid_size in range(2, 300):
            top_left, spl = compute_for_grid_size(summed_table, size, grid_size)
            if spl > best_spl:
                best_spl = spl
                best_top_left = top_left
                best_gs = grid_size
        print(best_top_left, best_spl, best_gs)
