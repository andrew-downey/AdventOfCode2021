#!/usr/bin/env python3
from colored import style
import os
import progressbar


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    print("")
    print(style.BOLD + "Total Overlaps: " + style.RESET + str(len(overlaps)))


if __name__ == "__main__":
    main()
