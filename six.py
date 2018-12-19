#!/usr/bin/env python

from collections import defaultdict, namedtuple
import fileinput
import string

Coord = namedtuple('Coord', ['n', 'x', 'y'])
coords = []
bounded = []
alpha = list(string.ascii_letters)

max_value = 0
for line in fileinput.input():
    x, y = map(int, line.strip().split(","))
    if max(x, y) > max_value:
        max_value = max(x, y)
    coords.append(Coord(alpha.pop(0), x, y))

max_value += 1

def closest_char(x, y, coords, max_value):
    mind = max_value*max_value
    char = "."
    for coord in coords:
        d = abs(coord.x - x) + abs(coord.y - y)
        if d == mind:
            char = "."
        elif d < mind:
            char = coord.n
            mind = d
    return char

counts = defaultdict(int)
for y in range(0, max_value):
    for x in range(0, max_value):
        char = closest_char(x, y, coords, max_value)
        counts[char] += 1

# check if area expands if we go outside of box
infinite = set()
for y in [-2, -1, max_value+1, max_value+2]:
    for x in range(0, max_value):    
        char = closest_char(x, y, coords, max_value)
        infinite.add(char)

for y in range(0, max_value):
    for x in [-2, -1, max_value+1, max_value+2]: 
        char = closest_char(x, y, coords, max_value)
        infinite.add(char)

largest_area = 0
for k, v in counts.items():
    if k not in infinite and v > largest_area:
        largest_area = v

print(largest_area)

area = 0
for y in range(-10, max_value+10):
    for x in range(-10, max_value+10):
        sumd = 0
        for coord in coords:
            sumd += abs(coord.x - x) + abs(coord.y - y)
        if sumd < 10000:
            area += 1

print(area)
