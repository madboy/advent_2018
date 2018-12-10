#!/usr/bin/env python

import fileinput

inputs = fileinput.input()
inputs = inputs.readline().strip()
inputs_copy = inputs
cur = 0

while cur < len(inputs)-1:
    unit1, unit2 = inputs[cur:cur+2]
    if unit1.upper() == unit2.upper() and \
    ((unit1.islower() and unit2.isupper()) or (unit1.isupper() and unit2.islower())):
        inputs = inputs[:cur] + inputs[cur+2:]
        if cur > 0:
            cur -= 1
    else:
        cur += 1

print("{}... {}".format(inputs[:100], len(inputs)))

chars = set(inputs_copy.lower())
cur_min = len(inputs_copy)
min_char = 0

for char in chars:
    cur = 0
    icc = inputs_copy.replace(char, '')
    icc = icc.replace(char.upper(), '')
    while cur < len(icc)-1:
        unit1, unit2 = icc[cur:cur+2]
        if unit1.upper() == unit2.upper() and \
        ((unit1.islower() and unit2.isupper()) or (unit1.isupper() and unit2.islower())):
            icc = icc[:cur] + icc[cur+2:]
            if cur > 0:
                cur -= 1
        else:
            cur += 1
    if len(icc) < cur_min:
        cur_min = len(icc)
        min_char = char

print(cur_min, min_char)

