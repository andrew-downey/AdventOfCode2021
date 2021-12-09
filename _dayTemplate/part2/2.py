#!/usr/bin/env python3
import os


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../example.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    print("")
    print("Total: " + str(len(rows)))


if __name__ == "__main__":
    main()
