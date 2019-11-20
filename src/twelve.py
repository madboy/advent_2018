from dataclasses import dataclass
from src.tools import process


@dataclass
class Pattern:
    pattern: str
    result: str


@dataclass
class Change:
    index: int
    value: str


def print_state(state, low, high):
    s = ""
    for i in range(low, high + 1):
        s += state.get(i, ".")
    print(s)


def run(input_file):
    file_contents = process(input_file)
    initial_state = next(file_contents)
    initial_state = initial_state[15:]  # remove the line description
    low = 0
    high = len(initial_state)

    state = {}
    for i, c in enumerate(initial_state):
        if c == "#":
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
                state.get(i - 2, ".")
                + state.get(i - 1, ".")
                + state.get(i, ".")
                + state.get(i + 1, ".")
                + state.get(i + 2, ".")
            )
            for pattern in patterns:
                if llcrr == pattern.pattern and pattern.result == "#":
                    changes.append(Change(i, pattern.result))
                    continue

        new_state = {}
        for change in changes:
            new_state[change.index] = change.value
            if change.index < low:
                low = change.index
            if change.index > high:
                high = change.index

        state = new_state

    print(sum(state))
