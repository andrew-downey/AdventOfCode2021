#!/usr/bin/env python3
import os
import colorama.ansi as ansi

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

brackets = {")": "(", "]": "[", "}": "{", ">": "<"}


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    corrupted = []
    for row in rows:
        opened = []
        for index, char in enumerate(row):
            if char in brackets.values():
                opened.append(char)
            else:
                if brackets[char] != opened.pop():
                    corrupted.append((row, index, char))
                    break

    for corrupt in corrupted:
        for index, char in enumerate(corrupt[0]):
            if(index == corrupt[1]):
                print(ansi.Style.BRIGHT +
                      char + ansi.Style.RESET_ALL, end="")
            else:
                print(char, end="")
        print("")

    print("Total corrupted lines: " + str(len(corrupted)))
    print("Total score: {0}".format(
        sum([scores[corrupt[2]] for corrupt in corrupted])))


if __name__ == "__main__":
    main()
