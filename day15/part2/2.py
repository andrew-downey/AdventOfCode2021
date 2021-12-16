#!/usr/bin/env python3
import os
from typing import DefaultDict
import colorama.ansi

SCALE_FACTOR = 5
MAXINT = int(9999999)


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    grid = [list(map(int, row)) for row in rows]
    width = len(grid[0])
    height = len(grid)

    # E X P A N D
    expanded_grid = []
    # first expand horizontally
    for x in range(width):
        original_row = grid[x]
        row = []
        for j in range(SCALE_FACTOR):
            for p in range(height):
                new_val = original_row[p]+j
                if new_val > 9:
                    new_val = new_val-9
                row.append(new_val)
        expanded_grid.append(row)

    size = len(expanded_grid[0])
    # now expand vertically
    for y in range(1, SCALE_FACTOR):
        for i in range(width):
            row = []
            original_row = expanded_grid[i]
            for j in range(size):
                new_val = original_row[j]+y
                if new_val > 9:
                    new_val = new_val-9
                row.append(new_val)
            expanded_grid.append(row)

    grid = expanded_grid

    width *= SCALE_FACTOR
    height *= SCALE_FACTOR
    graph = DefaultDict(dict)
    # Add an edge for each neighbour
    for y, row in enumerate(grid):
        for x, point in enumerate(row):
            for ny, nx in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                if(y + ny < height and y + ny >= 0 and x + nx < width and x + nx >= 0):
                    graph[(y, x)][(y + ny, x + nx)] = grid[y + ny][x + nx]

    target_point = (height - 1, width - 1)
    visited = {}
    queue = {(0, 0): 0}
    minimums_cache_stack = [(0, (0, 0))]
    print("Running on grid: {0}x{1}".format(width, height))
    while len(queue) > 0:
        # the current minimum for pushing into stack
        if len(minimums_cache_stack) == 0:
            current_minimum = min(queue.values())
        else:
            current_minimum, temp_coord = minimums_cache_stack[-1]
        # attempt to recover the minimum from the cache stack
        try:
            cost, coord = minimums_cache_stack.pop()
            if queue[coord] != cost:
                raise IndexError
            current_node = coord
            current_cost = cost
            if current_cost > min(queue.values()):
                print("BUG", current_cost, min(queue.values()))
        except (IndexError, KeyError):
            # cache stack is empty or invalid, nullify it and find the minimum
            current_cost = min(queue.values())
            minimums_cache_stack = []
            current_cost_index = list(queue.values()).index(current_cost)
            current_node = list(queue.keys())[current_cost_index]

        for neighbour, cost in graph[current_node].items():
            if neighbour not in visited:
                new_cost = MAXINT
                try:
                    new_cost = queue[neighbour]
                except KeyError:
                    pass
                candidate_cost = current_cost + cost
                if candidate_cost < new_cost:
                    queue[neighbour] = candidate_cost
                    if new_cost <= current_minimum:
                        minimums_cache_stack.append((new_cost, neighbour))
                        current_minimum = new_cost

        visited[current_node] = current_cost
        del queue[current_node]

        if(current_node == target_point):
            break

    # for y in range(height):
    #     print("")
    #     for x in range(width):
    #         value = paths[(y, x)]
    #         # print(colorama.ansi.Style.BRIGHT if value <
    #         #       10 else colorama.ansi.Style.DIM if value > 25 else colorama.ansi.Style.NORMAL, end="")
    #         print(" {0}".format(value), end="")
    #         # print(colorama.ansi.Style.RESET_ALL, end="")

    print("")
    print("Cost to get to bottom right: {0}".format(
        visited[(height - 1, width - 1)]))


if __name__ == "__main__":
    main()
