import fileinput
from src.tools import process


def dfs_visit_2(tree, u, metadata):
    n, m = tree[u : u + 2]
    my_metadata = []
    for _ in range(0, n):
        u = dfs_visit_2(tree, u + 2, my_metadata)
    if n == 0:
        metadata.append(sum(tree[u + 2 : u + 2 + m]))
    else:
        total = 0
        meta = tree[u + 2 : u + 2 + m]
        for e in meta:
            try:
                total += my_metadata[e - 1]
            except IndexError:
                pass
        metadata.append(total)
    return u + m


def dfs_visit(tree, u, metadata):
    n, m = tree[u : u + 2]
    for _ in range(0, n):
        u = dfs_visit(tree, u + 2, metadata)
    metadata.append(sum(tree[u + 2 : u + 2 + m]))
    return u + m


def run(input_file):
    line = next(process(input_file))
    tree = list(map(int, line.split(" ")))

    metadata = []

    dfs_visit(tree, 0, metadata)
    print(sum(metadata))

    metadata2 = []
    dfs_visit_2(tree, 0, metadata2)
    print(metadata2.pop())
