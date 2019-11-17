"""
Given a 300x300 grid of fuel cells select the 3x3 (1) or variable size (2) cell 
square that has the largest total power
"""
import math
from src.tools import process


def power_level(x, y, grid_serial_number):
    rack_id = x + 10
    power_lvl = rack_id * y
    power_lvl += grid_serial_number
    power_lvl *= rack_id
    # keep only the hundreds digit, if below 100 -> 0
    power_lvl = int(power_lvl / 100) % 10
    return power_lvl - 5


def compute_square_power_level(x, y, grid, grid_size, computed_grid):
    # use a successively computed grid and only look at new column and row
    total_power_level = computed_grid.get((x, y), 0)
    for i in range(x, x + grid_size):
        total_power_level += grid[(i, y + grid_size - 1)]

    # avoid duplicate of coord that has already been covered above by not going to last y
    for i in range(y, y + grid_size - 1):
        total_power_level += grid[(x + grid_size - 1, i)]
    computed_grid[(x, y)] = total_power_level
    return total_power_level


def populate_grid(grid_serial_number):
    grid = {}
    for x in range(1, 301):
        for y in range(1, 301):
            grid[(x, y)] = power_level(x, y, grid_serial_number)
    return grid


def find_largest_power_level(grid, smallest_grid_size, largest_grid_size):
    top_left = (1, 1)
    current_spl = -1000
    best_gs = 1
    size = int(math.sqrt(len(grid.keys())))
    computed_grid = {}
    for x in range(1, size + 1):
        for y in range(1, size + 1):
            for gs in range(smallest_grid_size, largest_grid_size):
                if (x + gs - 1) > size or (y + gs - 1) > size:
                    continue
                spl = compute_square_power_level(x, y, grid, gs, computed_grid)
                if spl > current_spl:
                    top_left = (x, y)
                    current_spl = spl
                    best_gs = gs
    return top_left, current_spl, best_gs


def run(input_file):
    for grid_serial_number in process(input_file):
        grid_serial_number = int(grid_serial_number)
        grid = populate_grid(grid_serial_number)
        print(find_largest_power_level(grid, 1, 4))
        print(find_largest_power_level(grid, 1, 301))
