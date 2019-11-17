#!/usr/bin/env python

from collections import defaultdict
import re
from src.tools import process


def run(input_file):
    guard_number_p = re.compile(".*#(\d+).*")
    guard_number = -1

    minute_p = re.compile(".* 00:(\d+)\].*")
    asleep = 0
    waking = 0

    patterns = dict()

    for line in sorted([line for line in process(input_file)]):
        log_entry = line.strip()
        if "Guard" in log_entry:
            guard_number = guard_number_p.match(line).group(1)
            if not patterns.get(guard_number):
                patterns[guard_number] = defaultdict(int)
        elif "asleep" in log_entry:
            asleep = minute_p.match(line).group(1)
        else:
            waking = minute_p.match(line).group(1)
            for i in range(int(asleep), int(waking)):
                patterns[guard_number][i] += 1
            # print(log_entry, guard_number, asleep, waking)

    max_minutes = 0
    heavy_sleepers = []

    for g, p in patterns.items():
        if len(p.keys()) >= max_minutes:
            max_minutes = len(p.keys())

    for g, p in patterns.items():
        if len(p.keys()) == max_minutes:
            heavy_sleepers.append(g)

    max_minute = -1
    heavy_sleep_minute = -1
    heavy_sleeper = -1

    for hs in heavy_sleepers:
        for k, v in patterns.get(hs).items():
            # print(v, k, hs)
            if v >= max_minute and k > heavy_sleep_minute:
                max_minute = v
                heavy_sleep_minute = k
                heavy_sleeper = hs

    mostest_max = -1
    mostest_minute = -1
    mostest_guard = -1

    for k, v in patterns.items():
        for kk, vv in v.items():
            if vv > mostest_max:
                mostest_max = vv
                mostest_minute = kk
                mostest_guard = k

    print(
        "{}*{} {}".format(
            heavy_sleeper, heavy_sleep_minute, int(heavy_sleeper) * heavy_sleep_minute,
        )
    )  # 33 * 3023
    # print(patterns.get(mostest_guard))
    print(
        "{}*{} {}".format(
            mostest_guard, mostest_minute, int(mostest_guard) * mostest_minute
        )
    )  # 2719 * 36
