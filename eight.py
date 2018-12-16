#!/usr/bin/env python

import fileinput

class Node(object):
    def __init__(self, c, m):
        self.c = int(c)
        self.m = int(m)

    def __str__(self):
        return "({}, {})".format(self.c, self.m)

    def __repr__(self):
        return self.__str__()


def dfs_visit(tree, u, metadata):
    n, m = tree[u:u+2]
    n = int(n)
    m = int(m)
    for _ in range(0, n):
        u = dfs_visit(tree, u+2, metadata)
    metadata.append(tree[u+2:u+2+m])
    return u + m

tree = fileinput.input().readline().strip().split(" ")
metadata = []

dfs_visit(tree, 0, metadata)
total = 0
for e in metadata:
    for m in e:
        total += int(m)

# print(total)
print(total, metadata)
