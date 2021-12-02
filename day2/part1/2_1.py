#!/usr/bin/env python3
import os


def main():
    """ Main entry point of the app """
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        horizontal = 0
        depth = 0
        lines = myfile.readlines()
        for line in lines:
            command, value = line.split(' ')
            if(command == 'forward'):
                horizontal += int(value)
            elif(command == 'down'):
                depth += int(value)
            elif(command == 'up'):
                depth -= int(value)

        print("Horizontal Distance: " + str(horizontal))
        print("Final Depth: " + str(depth))
        print("Multiplied: " + str(horizontal * depth))


if __name__ == "__main__":
    main()
