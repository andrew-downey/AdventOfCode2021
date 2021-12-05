#!/usr/bin/env python3
import os


def binary_to_decimal(binary):
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal


def split(word):
    return [char for char in word]


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    length = 0
    with open(filename, "r") as myfile:
        linebytes = []
        for line in myfile.readlines():
            if(length == 0):
                length = len(line)
            linebytes.append(line)

        gamma = []
        epsilon = []
        for i in list(range(length - 1)):
            counts = dict()
            counts["0"] = 0
            counts["1"] = 0
            for linebyte in linebytes:
                val = split(linebyte)[i]
                if(val == "0" or val == "1"):
                    counts[split(linebyte)[i]] += 1

            if(counts["0"] >= counts["1"]):
                gamma.append("0")
                epsilon.append("1")
            else:
                gamma.append("1")
                epsilon.append("0")

        gamma = ''.join(gamma)
        epsilon = ''.join(epsilon)
        print("gamma: " + str(gamma))
        print("epsilon: " + str(epsilon))

        gammad = int(gamma, 2)
        epsilond = int(epsilon, 2)
        print("gammad: " + str(gammad))
        print("epsilond: " + str(epsilond))
        print("Multiplied: " + str(gammad * epsilond))


if __name__ == "__main__":
    main()
