#!/usr/bin/env python3
import os
import re

TIMES_TO_FOLD = 1


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    points = []
    folds = []
    for row in rows:
        if len(row.strip()) > 0:
            # Fold commands
            if "fold" in row:
                # Where do we fold?
                print(re.findall(r"(\w)=(\d+)", row))
                folds.append(re.findall(r"(\w)=(\d+)", row)[0])
            else:
                # Add a point to the grid
                points.append(tuple(map(int, row.split(","))))

    highest_x = sorted(points, key=lambda x: x[0], reverse=True)[0][0] + 1
    highest_y = sorted(points, key=lambda x: x[1], reverse=True)[0][1] + 1
    grid = []
    for y in range(highest_y):
        grid.append([])
        for x in range(highest_x):
            grid[y].append(".")

    for point in points:
        x, y = point
        grid[y][x] = "#"

    [print(str(index) + ": " + "".join(row))
     for index, row in enumerate(grid)]
    for fold_command in folds[0:1]:
        axis, coord = fold_command
        coord = int(coord)
        if axis == "y":
            fold_points = [value for key,
                           value in enumerate(grid) if key > coord]
            for y, fold_row in enumerate(fold_points):
                for x, fold_point in enumerate(fold_row):
                    if(fold_point == "#"):
                        grid[coord - y - 1][x] = "#"
            grid = grid[:coord]
        else:
            fold_points = [[value for key, value in enumerate(
                v) if key > coord] for k, v in enumerate(grid)]
            for y, fold_row in enumerate(fold_points):
                for x, fold_point in enumerate(fold_row):
                    if(fold_point == "#"):
                        grid[y][coord - x - 1] = "#"
            grid = [[point for key, point in enumerate(
                row) if key < coord] for row in grid]

        print("")
        print("Folding at {0}={1}".format(axis, coord))

    print("Final grid")
    [print(str(index) + ": " + "".join(row))
        for index, row in enumerate(grid)]

    print("")
    print("Total points: " + str(len(points)))
    print("Total folds: " + str(len(folds)))
    points_visible = [value for row in grid for value in row if value == "#"]
    print("Points visible after 1 fold: {0}".format(len(points_visible)))


if __name__ == "__main__":
    main()
