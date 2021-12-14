#!/usr/bin/env python3
import os
from collections import defaultdict

ITERATIONS = 10


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    combinations = {}
    template = ""
    for row in rows:
        if len(row) > 0:
            if "->" in row:
                pair, insertion = row.split(" -> ")
                combinations[pair] = insertion
            else:
                template = row

    pairs = defaultdict(int)
    elements = defaultdict(int)
    for index, char in enumerate(template[:-1]):
        pairs[template[index:index+2]] += 1
        elements[char] += 1
    elements[template[-1]] += 1

    print("{0:<12} {1}".format(
        "Iteration 0 :", pairs))
    for iteration in range(1, ITERATIONS + 1):
        for pair, count in list(pairs.items()):
            new_element = combinations[pair]
            elements[new_element] += count
            pairs[pair] -= count
            pairs[pair[0] + new_element] += count
            pairs[new_element + pair[1]] += count
        print("{0:<12} {1}".format(
            "Iteration {0:>2}:".format(iteration), pairs))

    print("")
    print("After {0:>2} iterations: {1}".format(
        ITERATIONS, max(elements.values()) - min(elements.values())
    ))


if __name__ == "__main__":
    main()
