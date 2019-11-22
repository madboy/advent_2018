def process(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()


def left_pad_process(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.rstrip()
