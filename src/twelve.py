from dataclasses import dataclass
from src.tools import process


@dataclass
class Pattern:
    pattern: str
    result: str


EMPTY = "."
PLANT = "#"


def print_state(state, low, high):
    s = ""
    for i in range(low, high + 1):
        s += state.get(i, EMPTY)
    print(s)


def run(input_file):
    file_contents = process(input_file)
    initial_state = next(file_contents)
    initial_state = initial_state[15:]  # remove the line description
    low = 0
    high = len(initial_state)

    state = {}
    for i, c in enumerate(initial_state):
        if c == PLANT:
            state[i] = c

    next(file_contents)  ## drain empty line

    print_state(state, low, high)

    patterns = []
    for line in file_contents:
        pattern, result = line.split(" => ")
        patterns.append(Pattern(pattern, result))

    for g in range(0, 20):
        changes = []
        for i in range(low - 2, high + 2):

            llcrr = (
                state.get(i - 2, EMPTY)
                + state.get(i - 1, EMPTY)
                + state.get(i, EMPTY)
                + state.get(i + 1, EMPTY)
                + state.get(i + 2, EMPTY)
            )
            for pattern in patterns:
                if llcrr == pattern.pattern and pattern.result == PLANT:
                    changes.append(i)
                    continue

        new_state = {}
        for idx in changes:
            new_state[idx] = PLANT
            if idx < low:
                low = idx
            if idx > high:
                high = idx

        state = new_state

    print(sum(state))
    # for part two we can use the result from 100 and 1000 generations for the pattern g * 50 + 695 => 50000000000 * 50 + 695
