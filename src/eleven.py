"""
Given a 300x300 grid of fuel cells select the 3x3 cell square that has the largest total power
"""
from src.tools import process


def power_level(x, y, grid_serial_number):
    rack_id = x + 10
    power_lvl = rack_id * y
    power_lvl += grid_serial_number
    power_lvl *= rack_id
    # keep only the hundreds digit, if none 0
    try:
        power_lvl = int(str(power_lvl)[-3])
    except IndexError:
        power_lvl = 0
    return power_lvl - 5


def compute_square_power_level(x, y, grid, grid_size):
    total_power_level = 0
    for i in range(x, x + grid_size):
        for ii in range(y, y + grid_size):
            total_power_level += grid[(i, ii)]
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
    for x in range(1, 298):
        for y in range(1, 298):
            for gs in range(smallest_grid_size, largest_grid_size):
                if x + gs > 300 or y + gs > 300:
                    continue
                spl = compute_square_power_level(x, y, grid, gs)
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
