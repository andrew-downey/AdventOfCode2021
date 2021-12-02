#!/usr/bin/env python3
import os


def main():
    """ Main entry point of the app """
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        horizontal = 0
        aim = 0
        depth = 0
        lines = myfile.readlines()
        for line in lines:
            command, value = line.split(' ')
            value = int(value)
            if(command == 'forward'):
                horizontal += value
                depth += aim * value
            elif(command == 'down'):
                aim += value
            elif(command == 'up'):
                aim -= value

        print("Horizontal Distance: " + str(horizontal))
        print("Final Aim: " + str(aim))
        print("Final Depth: " + str(depth))
        print("Multiplied: " + str(horizontal * depth))


if __name__ == "__main__":
    main()
