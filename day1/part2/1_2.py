#!/usr/bin/env python3
import os
import numpy as np


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        lines = myfile.readlines()
        numbers = [int(num, base=16) for num in lines]
        moving_averages = np.convolve(numbers, np.ones(3, dtype=int), 'valid')
        print("Averages: " + str(moving_averages))

        increases = 0
        lastsum = moving_averages[0]
        for currentsum in moving_averages:
            if (currentsum > lastsum):
                print("Increase")
                increases += 1
            else:
                print("Decrease or Same")
            lastsum = currentsum
        print("Increases: " + str(increases))


if __name__ == "__main__":
    main()
