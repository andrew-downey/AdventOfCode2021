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

    crabs = []
    for crab in row.strip().split(","):
        crabs.append(int(crab))

    total_fuel_used = {}
    for x in range(0, max(crabs)):
        total_fuel_used.setdefault(
            x, sum([abs(x - crab) for crab in crabs if crab != x]))
        print("Total fuel used for position {0}: {1}".format(
            x, total_fuel_used[x]))

    print("")
    print("Lowest fuel consumption: position {0} with {1} fuel used".format(
        min(total_fuel_used, key=total_fuel_used.get), min(total_fuel_used.values())))


if __name__ == "__main__":
    main()
