#!/usr/bin/env python
from src import *
import sys

days = [
    "",
    (one.run, "input/1"),
    (two.run, "input/2"),
    (three.run, "input/3"),
    (four.run, "input/4"),
    (five.run, "input/5"),
    (six.run, "input/6"),
]


if __name__ == "__main__":
    try:
        day = int(sys.argv[1])
        days[day][0](days[day][1])
    except (IndexError, ValueError):
        print("usage: ./advent.py <day_nbr>")
