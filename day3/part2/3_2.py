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
        lines = myfile.read().splitlines()
        length = len(lines[0])
        print("Length: " + str(length))

        oxygen = ""
        mutable_lines = lines
        for i in list(range(length)):
            print("Index: " + str(i + 1))

            counts = dict()
            counts["0"] = 0
            counts["1"] = 0
            for line in mutable_lines:
                val = split(line)[i]
                if(val == "0" or val == "1"):
                    counts[split(line)[i]] += 1

            target = "1"
            if(counts["0"] > counts["1"]):
                target = "0"

            new_mutable_lines = []
            for line_index in range(len(mutable_lines)):
                if(split(mutable_lines[line_index])[i]) == target:
                    new_mutable_lines.append(mutable_lines[line_index])

            mutable_lines = new_mutable_lines
            print("Remaining lines: {0}".format(len(mutable_lines)))

            if(len(mutable_lines)) <= 1:
                oxygen = mutable_lines[0]
                print("Found final value for oxygen: {0}".format(oxygen))
                break

        co2 = ""
        mutable_lines = lines
        for i in list(range(length)):
            print("Index: " + str(i + 1))

            counts = dict()
            counts["0"] = 0
            counts["1"] = 0
            for line in mutable_lines:
                val = split(line)[i]
                if(val == "0" or val == "1"):
                    counts[split(line)[i]] += 1

            target = "1"
            if(counts["0"] <= counts["1"]):
                target = "0"

            new_mutable_lines = []
            for line_index in range(len(mutable_lines)):
                print("Considering line_index {0} ({2}), wants target {1} (has {3})".format(
                    line_index, target, mutable_lines[line_index], split(mutable_lines[line_index])[i]))
                if(split(mutable_lines[line_index])[i]) == target:
                    new_mutable_lines.append(mutable_lines[line_index])

            mutable_lines = new_mutable_lines
            print("Remaining lines: {0}".format(len(mutable_lines)))

            if(len(mutable_lines)) <= 1:
                co2 = mutable_lines[0]
                print("Found final value for co2: {0}".format(co2))
                break

        oxygen = ''.join(oxygen)
        co2 = ''.join(co2)
        print("oxygen: " + oxygen)
        print("co2: " + co2)

        oxygend = int(oxygen, 2)
        co2d = int(co2, 2)
        print("oxygend: " + str(oxygend))
        print("co2d: " + str(co2d))
        print("Multiplied: " + str(oxygend * co2d))


if __name__ == "__main__":
    main()
