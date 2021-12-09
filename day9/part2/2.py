#!/usr/bin/env python3
import os
import colorama
from functools import reduce


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    grid = [list(map(int, row)) for row in rows]
    width = len(grid[0])
    height = len(grid)

    lowspots = []
    for y in range(0, height):
        print("")
        for x in range(0, width):
            point = grid[y][x]
            testpoints = []
            testpoints.append(grid[y - 1][x] if y > 0 else 9)
            testpoints.append(grid[y + 1][x] if y < height - 1 else 9)
            testpoints.append(grid[y][x + 1] if x < width - 1 else 9)
            testpoints.append(grid[y][x - 1] if x > 0 else 9)

            low = True
            for testpoint in testpoints:
                if testpoint <= point:
                    low = False
            if low:
                lowspots.append((y, x, point))
                print(colorama.Fore.BLUE, end='')

            print((colorama.Style.BRIGHT if point == 9 else colorama.Style.DIM if point < 4 else colorama.Style.NORMAL) + str(point) +
                  colorama.Style.RESET_ALL, end='')

    basins = {}
    for lowspot in lowspots:
        visited = []
        queue = []
        visited.append(lowspot)
        queue.append(lowspot)
        while queue:
            point = queue.pop()
            neighbours = []
            y, x, value = point
            neighbours.append([y - 1, x, grid[y - 1][x]
                               if y > 0 else 9])
            neighbours.append([y + 1, x, grid[y + 1][x]
                               if y < height - 1 else 9])
            neighbours.append([y, x + 1, grid[y][x + 1]
                               if x < width - 1 else 9])
            neighbours.append([y, x - 1, grid[y][x - 1]
                               if x > 0 else 9])
            for neighbour in [neighbour for neighbour in neighbours if neighbour[2] != 9]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        basins[lowspot] = len(visited) - 1

    basins = sorted(basins.values(), reverse=True)
    print("")
    print("Total basins {0}".format(len(basins)))
    print("Top 3 basins: {0}".format(basins[0: 3]))
    print("Top 3 basin volume: {0}".format(
        reduce(lambda x, y: x*y, basins[0:3])
    ))


if __name__ == "__main__":
    main()
