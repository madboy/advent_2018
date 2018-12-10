#!/usr/bin/env python

from collections import defaultdict
import fileinput
import re

inputs = fileinput.input()

pattern = re.compile("#(\d+) @ (\d+)\,(\d+): (\d+)x(\d+)")
cloth = defaultdict(int)
whole = set({})
intersect = set({})
overlap = 0

for line in inputs:
    claim = line.strip()
    g = pattern.match(claim)
    cid, lefte, righte, width, height = g.group(1), int(g.group(2)), int(g.group(3)), int(g.group(4)), int(g.group(5))
    for i in range(lefte+1, lefte+width+1):
        for j in range(righte+1, righte+height+1):
            # cloth["{}, {}".format(i, j)] += 1
            coord = "{},{}".format(i, j)
            if cloth.get(coord, 0) == 0:
                whole.add(cid)
                cloth[coord] = cid            
            else:
                intersect.add(cid)
                intersect.add(cloth.get(coord))
                # if cloth[coord] != -1:
                #     overlap += 1
                cloth[coord] = -1      

for v in cloth.values():
    if v == -1:
        overlap += 1

print(overlap)
print(whole - intersect)
