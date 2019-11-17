from collections import defaultdict
import copy
import re
import string
from src.tools import process


class Workers(object):
    def __init__(self):
        self.workers = [0, 0, 0, 0, 0]
        self.items = ["", "", "", "", ""]

    def __str__(self):
        return str(zip(self.workers, self.items))

    def __repr__(self):
        return self.__str__()


def deps(rgraph, node, path):
    for d in rgraph.get(node, []):
        if d not in path:
            return False
    return True


def find_next(rgraph, nodes, path):
    available = []
    for node in nodes:
        if deps(rgraph, node, path):
            available.append(node)
    return available


def get_free_worker(workers, node):
    if node not in workers.items:
        for i, w in enumerate(workers.workers):
            if w == 0 and workers.items[i] == "":  # protect against A that has cost 0
                return i
    return None


def update_workers(workers, nodes, path):
    for i, worker in enumerate(workers.workers):
        if worker > 0:
            workers.workers[i] -= 1
        if worker == 0 and workers.items[i]:
            path += workers.items[i]
            nodes.remove(workers.items[i])
            workers.items[i] = ""


def find_path_with_workers(rgraph, nodes, workers=None, delay=0, cost={}):
    timing = 0
    path = []
    while nodes:
        for node in find_next(rgraph, nodes, path):
            i = get_free_worker(workers, node)
            if i is not None:
                workers.workers[i] = cost.get(node, 0) + delay
                workers.items[i] = node
        update_workers(workers, nodes, path)
        timing += 1
    return path, timing


def find_path(rgraph, nodes):
    path = []
    idx = 0
    while nodes:
        node = nodes[idx]
        if deps(rgraph, node, path):
            path += node
            nodes.remove(node)
            idx = 0
        else:
            idx += 1
    return path


def run(input_file):
    inst = re.compile(r"Step (\w) .* step (\w)")
    rgraph = defaultdict(list)
    nodes = set()

    for instruction in process(input_file):
        steps = inst.match(instruction)
        head = steps.group(1)
        step = steps.group(2)
        nodes.add(head)
        nodes.add(step)
        rgraph[step].append(head)

    nodes = sorted(list(nodes))
    nodes_2 = copy.deepcopy(nodes)

    print("".join(find_path(rgraph, nodes)))

    cost = {}
    i = 0
    for c in string.ascii_uppercase:
        cost[c] = i
        i += 1

    workers = Workers()
    print(find_path_with_workers(rgraph, nodes_2, workers, 60, cost))
