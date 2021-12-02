#!/usr/bin/env python3
import os


def main():
    """ Main entry point of the app """
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        lastline = myfile.readline()
        myline = True
        increases = 0
        while myline:
            myline = myfile.readline()
            if (myline != "" and int(myline) > int(lastline)):
                increases += 1
            lastline = myline
        print("Increases: " + str(increases))


if __name__ == "__main__":
    main()
