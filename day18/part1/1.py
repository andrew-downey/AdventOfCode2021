#!/usr/bin/env python3
from math import ceil, floor
import os
from time import time
from typing import List, Tuple


def explode(elements, opening_bracket_index):
    left_number = elements[opening_bracket_index + 1]
    right_number = elements[opening_bracket_index + 2]

    for i in range(opening_bracket_index - 1, 0, -1):
        if isinstance(elements[i], int):
            elements[i] += left_number
            break

    for i in range(opening_bracket_index + 4, len(elements)):
        if isinstance(elements[i], int):
            elements[i] += right_number
            break

    return elements[:opening_bracket_index] + [0] + elements[opening_bracket_index + 4:]


def try_explode(elements):
    open_brackets = 0
    for i in range(len(elements)):
        if open_brackets == 4 and elements[i] == '[':
            elements = explode(elements, i)
            return True, elements
        elif elements[i] == '[':
            open_brackets += 1
        elif elements[i] == ']':
            open_brackets -= 1
    return False, elements


def split(elements: List):
    for i in range(len(elements)):
        if isinstance(elements[i], int) and elements[i] >= 10:
            elements[i:i + 1] = ['[',
                                 floor(elements[i] / 2), ceil(elements[i] / 2), ']']
            return True, elements
    return False, elements


def reduce(elements: List) -> List:
    has_reduced = True
    while has_reduced:
        has_reduced, elements = try_explode(elements)
        if not has_reduced:
            has_reduced, elements = split(elements)

    return elements


def magnitude(elements, index=0):
    if isinstance(elements[index], int):
        return elements[index], index

    left_sum, index = magnitude(elements, index + 1)
    right_sum, index = magnitude(elements, index + 1)

    return 3 * left_sum + 2 * right_sum, index + 1


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    elements = []
    for index, row in enumerate(rows):
        new_elements = filter(lambda element: element != ',', row)
        new_elements = list(map(lambda element: int(element)
                                if element.isdigit() else element, new_elements))
        elements.append(new_elements)

    result = elements[0]
    print("Step 0: {0}".format(result))
    for i in range(1, len(elements)):
        result = ['['] + result + elements[i] + [']']
        result = reduce(result)
        print("Step {1}: {0}".format(result, i))

    print("")
    print("Result: {0}".format(magnitude(result)))


if __name__ == "__main__":
    start = time()
    main()
    end = time()
    print(f'Finished in {round(end - start, 2)} seconds')
