#!/usr/bin/env python

import fileinput
import re

class Point(object):
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def __str__(self):
        return "({}, {}) -> ({}, {})".format(self.x, self.y, self.vx, self.vy)

    def __repr__(self):
        return self.__str__()

def display(points, minx, maxx, miny, maxy):
    grid = dict()
    for p in points:
        grid["{},{}".format(p.x, p.y)] = "#"
    for y in range(miny-2, maxy+2):
        row = ""
        for x in range(minx-2, maxx+2):
            row += grid.get("{},{}".format(x, y), ".")
        print(row)

point_re = re.compile("position=<\s?([-]?\d+), \s?([-]?\d+)> velocity=<\s?([-]?\d+), \s?([-]?\d+)>")

points = []
for line in fileinput.input():
    point = line.strip()
    x, y, vx, vy = list(map(int, point_re.match(point).groups()))
    points.append(Point(x, y, vx, vy))

for i in range(1, 25000):
    maxx = maxy = 0
    minx = miny = 1000000
    for p in points:
        nx = p.x + p.vx
        ny = p.y + p.vy
        p.x, p.y = nx, ny
        if nx > maxx:
            maxx = nx
        elif nx < minx:
            minx = nx
        if ny > maxy:
            maxy = ny
        elif ny < miny:
            miny = ny
    if abs(maxx - minx) < 70 and abs(maxy - miny) < 25:
        print(i)
        display(points, minx, maxx, miny, maxy)
        break
