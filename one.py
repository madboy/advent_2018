#!/usr/bin/env python
from collections import defaultdict
import fileinput

inputs = fileinput.input()

current_frequency = 0
frequencies = defaultdict(int)
fr = []

for line in inputs:
    line = line.strip()
    frequency = int(line)
    fr.append(frequency)
    current_frequency += frequency
    frequencies[current_frequency] += 1

print(current_frequency)
i = 0

while frequencies[current_frequency] < 2:
    current_frequency += fr[i]
    frequencies[current_frequency] += 1
    i += 1
    if i >= len(fr):
        i = 0

print(current_frequency)
