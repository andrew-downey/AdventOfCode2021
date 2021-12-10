#!/usr/bin/env python3
import os
import colorama.ansi as ansi
from functools import reduce
from collections import deque


scores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
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

    incomplete_rows = [row for row in rows if row not in [corrupt[0]
                                                          for corrupt in corrupted]]

    brackets_inverse = dict([(value, key) for key, value in brackets.items()])
    fixed_rows = {}
    for row in incomplete_rows:
        opened = deque()
        row_score = 0
        for index, char in enumerate(row):
            if char in brackets.values():
                # Opening a bracket
                opened.append(char)
            else:
                # Closing a bracket
                opened.pop()
                if index == len(row) - 1:
                    break

        while len(opened) > 0:
            char = opened.pop()
            row += brackets_inverse[char]
            row_score = (row_score * 5) + \
                scores[brackets_inverse[char]]
        fixed_rows[row] = row_score

    final_scores = deque(sorted(fixed_rows.values()))
    while len(final_scores) > 1:
        final_scores.pop()
        final_scores.popleft()

    print("Total fixed rows: " + str(len(fixed_rows)))
    [print("Row: {0}\nScore: {1}".format(index, value))
     for index, value in fixed_rows.items()]
    print("Final score: {0}".format(final_scores[0]))


if __name__ == "__main__":
    main()
