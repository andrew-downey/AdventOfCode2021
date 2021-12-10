#!/usr/bin/env python3
from colored import style
import os

DEFAULT_TIMER = 6
DEFAULT_FRESH_TIMER = 8
DAYS_TO_SIMULATE = 256


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        row = myfile.read().splitlines()[0]

    lanternfish = {i: 0 for i in range(0, DEFAULT_FRESH_TIMER + 1)}
    for fish in row.strip().split(","):
        lanternfish[int(fish)] += 1

    print("Initial state: {0}".format(lanternfish))

    for i in range(1, DAYS_TO_SIMULATE + 1):
        num_breeders = lanternfish[0]
        lanternfish = {
            key-1: value for (key, value) in lanternfish.items() if key != 0}
        lanternfish[DEFAULT_FRESH_TIMER] = num_breeders
        lanternfish[DEFAULT_TIMER] += num_breeders
        if(i % 50 == 0 or i == 256):
            print("After {0:>2} {2}: ({3}) {1}".format(
                i,
                lanternfish,
                "days" if i > 0 else "day",
                sum(lanternfish.values())
            )
            )

    print("")
    print(style.BOLD + "Total Lanternfish after {0} days: ({1})".format(
        DAYS_TO_SIMULATE, sum(lanternfish.values())) + style.RESET)


if __name__ == "__main__":
    main()
