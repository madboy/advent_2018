#!/usr/bin/env python
from dataclasses import dataclass
from src import (
    one,
    two,
    three,
    four,
    five,
    six,
    seven,
    eight,
    nine,
    ten,
    eleven,
    twelve,
    thirteen,
    fourteen,
)
import sys
from typing import Callable

@dataclass
class Day:
    program: Callable
    input_file: str

days = [
    (),
    Day(one.run, "input/1"),
    Day(two.run, "input/2"),
    Day(three.run, "input/3"),
    Day(four.run, "input/4"),
    Day(five.run, "input/5"),
    Day(six.run, "input/6"),
    Day(seven.run, "input/7"),
    Day(eight.run, "input/8"),
    Day(nine.run, "input/9"),
    Day(ten.run, "input/10"),
    Day(eleven.run, "input/11"),
    Day(twelve.run, "input/12"),
    Day(thirteen.run, "input/13"),
    Day(fourteen.run, "input/14"),
]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: ./advent.py <day_nbr>")
        sys.exit(1)

    try:
        day = int(sys.argv[1])
    except ValueError:
        print("Try using a number.")
        sys.exit(2)

    if day >= len(days) or day <= 0:
        print(f"I don't know that day yet. Try one between 1-{len(days)-1}.")
        sys.exit(3)

    d = days[day]
    d.program(d.input_file)
