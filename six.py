#!/usr/bin/env python

from collections import defaultdict, namedtuple
import fileinput
import string

Coord = namedtuple('Coord', ['n', 'x', 'y'])
coords = []
bounded = []
# alpha = list(string.ascii_lowercase)
alpha = list(string.ascii_letters)

max_value = 0
for line in fileinput.input():
    x, y = line.strip().split(",")
    x = int(x)
    y = int(y)
    if max(x, y) > max_value:
        max_value = max(x, y)
    coords.append(Coord(alpha.pop(0), x, y))

# print(coords)
max_value += 1

# NB: current calculation isn't correct
# you need to have intersections to be
# able to have a closed area
for c in coords:
    left, right, up, down = False, False, False, False
    intersect = []
    for cc in coords:
        if c == cc:
            continue
        if cc.x < c.x and cc.y < c.y: # lower right
            left = True
            intersect.append(cc)
            # print("x intersection left for {} and {}".format(c.n, cc.n))
        if cc.x < c.x and cc.y > c.y: # upper right
            # print("x intersection right for {} and {}".format(c.n, cc.n))
            right = True
            intersect.append(cc)
        if cc.x > c.x and cc.y < c.y: # lower left
            # print("y intersection up for {} and {}".format(c.n, cc.n))
            up = True
            intersect.append(cc)
        if cc.x > c.x and cc.y > c.y: # upper left
            # print("x intersection down for {} and {}".format(c.n, cc.n))
            down = True
            intersect.append(cc)
    if left and right and up and down:
        bounded.append(c.n)
        # print("{} is bounded by {}".format(c, intersect))

# line = ""
# counts = defaultdict(int)
# for y in range(0, max_value):
#     for x in range(0, max_value):
#         mind = max_value*max_value
#         char = "."
#         for coord in coords:
#             d = abs(coord.x - x) + abs(coord.y - y)
#             if d == mind:
#                 char = "."
#                 # mind = d
#             elif d < mind:
#                 char = coord.n
#                 mind = d
#         counts[char] += 1
        # line = line + char
    # line = line + "\n"
# print(line)

# 5333, b
# print(counts)
# print(max(counts.values()))

# max_area = 0
# choice = -1
# for b in bounded:
#     area = counts[b]
#     if area > max_area:
#         max_area = area
#         choice = b

# for b in coords:
#     area = line.count(b.n)
#     if area > max_area:
#         max_area = area
#         choice = b.n

# print(max_value, choice, max_area)


area = 0
# counts = defaultdict(int)
for y in range(-10, max_value+10):
    for x in range(-10, max_value+10):
        # mind = max_value*max_value
        # char = "."
        sumd = 0
        for coord in coords:
            sumd += abs(coord.x - x) + abs(coord.y - y)
            # if d == mind:
                # char = "."
                # mind = d
            # elif d < mind:
                # char = coord.n
                # mind = d
        if sumd < 10000:
            area += 1

print(area) # 35334
