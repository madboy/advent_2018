#!/usr/bin/env python

from collections import defaultdict
import fileinput

def get_index(length, current):
    n = current + 2
    # l = len(circle)
    if n <= length:
        return n
    else:
        return n - length

def insert(current, length, circle, marble):
    score = 0
    if (marble % 23) == 0:
        score += marble
        score += circle.pop(current-7)
        current = (current - 7)%length
    else:
        current = get_index(length, current)
        if current < 0:
            print(current, i)
        if current == length:
            circle.append(marble)
        else:
            circle = circle[:current] + [marble] + circle[current:]
    return circle, score, current

# def insert(current, length, circle, marble):
#     score = 0
#     if (marble % 23) == 0:
#         score += marble
#         score += circle.pop(current-7)
#     elif current >= length:
#         circle.append(marble)
#     else:
#         circle = circle[:current] + [marble] + circle[current:]
#     return circle, score

players, last = map(int, fileinput.input().readline().strip().split())

circle = [0]
current = 0
scores = defaultdict(int)
for i in range(1, last+1):
    player = i % players
    length = len(circle)
    circle, score, current = insert(current, length, circle, i)
    scores[player] += score

# assert circle == [0, 16, 8, 17, 4, 18, 19, 2, 24, 20, 25, 10, 21, 5, 22, 11, 1, 12, 6, 13, 3, 14, 7, 15], circle
print(max(scores.values()))
