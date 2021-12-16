#!/usr/bin/env python3
import os
from typing import DefaultDict
import colorama.ansi


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    grid = [list(map(int, row)) for row in rows]
    width = len(grid[0])
    height = len(grid)
    graph = DefaultDict(dict)
    # Add an edge for each neighbour
    for y, row in enumerate(grid):
        for x, point in enumerate(row):
            for ny, nx in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                if(y + ny < height and y + ny >= 0 and x + nx < width and x + nx >= 0):
                    graph[(y, x)][(y + ny, x + nx)] = grid[y + ny][x + nx]

    target_point = (height - 1, width - 1)
    paths = {node: 0 if node == (0, 0) else float("inf")
             for node in graph.keys()}
    visited = []
    queue = {(0, 0): 0}
    while len(queue) > 0:
        current_risk = min(queue.values())
        current_risk_index = list(queue.values()).index(current_risk)
        current_node = list(queue.keys())[current_risk_index]
        visited.append(current_node)
        for neighbour, cost in graph[current_node].items():
            if neighbour not in visited:
                new_cost = cost + paths[current_node]
                if new_cost < paths[neighbour]:
                    paths[neighbour] = new_cost
                    queue[neighbour] = new_cost
        del queue[current_node]

    for y in range(height):
        print("")
        for x in range(width):
            value = paths[(y, x)]
            # print(colorama.ansi.Style.BRIGHT if value <
            #       10 else colorama.ansi.Style.DIM if value > 25 else colorama.ansi.Style.NORMAL, end="")
            print(" {0}".format(value), end="")
            # print(colorama.ansi.Style.RESET_ALL, end="")

    print("")
    print("Cost to get to bottom right: {0}".format(
        paths[(height - 1, width - 1)]))


if __name__ == "__main__":
    main()
