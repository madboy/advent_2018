#!/usr/bin/env python

from collections import defaultdict
import fileinput

class Node(object):
    def __init__(self, v, n, p):
        self.v = v
        self.n = n
        self.p = p

    def __str__(self):
        if self.n and self.p:
            return "({} <- {} -> {})".format(self.p.v, self.v, self.n.v)
        elif self.n:
            return ". <- {} -> {}".format(self.v, self.n.v)
        elif self.p:
            return "{} <- {} -> .".format(self.p.v, self.v)
        else:
            return "(. <- {} -> .)".format(self.v)

    def __repr__(self):
        return self.__str__()

players, last = map(int, fileinput.input().readline().strip().split())
scores = defaultdict(int)

start = current = Node(0, None, None)
current.n = current

for i in range(1, last+1):
    if (i % 23) == 0:
        for _ in range(0, 7):
            current = current.p
        scores[i%players] += (i+ current.v)
        current.p.n = current.n
        current.n.p = current.p
        current = current.n
    else:
        tmp = Node(i, None, None)
        relink = current.n
        tmp.n = relink.n
        tmp.p = relink
        relink.n = tmp
        tmp.n.p = tmp
        current = tmp

print(max(scores.values()))
