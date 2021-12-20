#!/usr/bin/env python3
import os
from time import time


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../example.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    print("Rows: {0}".format(rows))


if __name__ == "__main__":
    start = time()
    main()
    end = time()
    print(f'Finished in {round(end - start, 2)} seconds')
