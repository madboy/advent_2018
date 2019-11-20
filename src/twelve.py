import re
from src.tools import process


def pad_initial_state(istate, padding=10):
    return "." * 3 + istate + "." * 11


EMPTY = "."
PLANT = "#"


def run(input_file):
    file_contents = process(input_file)
    initial_state = next(file_contents)
    initial_state = initial_state[15:]  # remove the line description
    initial_state = pad_initial_state(
        initial_state
    )  # make sure we have some empty pots on the sides

    next(file_contents)  ## drain empty line

    patterns = {}
    for line in file_contents:
        pattern, result = line.split(" => ")
        pattern = pattern.replace(
            ".", r"\."
        )  # change so that we can use the pattern as regex
        patterns[pattern] = result

    print(initial_state)
    for _ in range(0, 5):
        matches = set()
        for pattern, result in patterns.items():
            i = re.finditer(pattern, initial_state)
            for m in i:
                matches.add((m.start(0), result))

        state_list = list(initial_state)
        for match in matches:
            # assume that all pots surrounding a (matching?) pattern will be set to empty
            # I don't think we can assume this as it makes result non-deterministic as we can change the same point more than once
            # and the order of which we have the matches will matter
            state_list[match[0]] = EMPTY
            state_list[match[0] + 1] = EMPTY
            state_list[match[0] + 2] = match[1]
            state_list[match[0] + 3] = EMPTY
            state_list[match[0] + 4] = EMPTY

        initial_state = "".join(state_list)
        print(initial_state)
