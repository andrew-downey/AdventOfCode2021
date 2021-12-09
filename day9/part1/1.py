#!/usr/bin/env python3
import os
import colorama


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
                lowspots.append(tuple((x, y, point)))
                print(colorama.Fore.BLUE, end='')

            print((colorama.Style.BRIGHT if point > 8 else colorama.Style.DIM if point < 2 else colorama.Style.NORMAL) + str(point) +
                  colorama.Style.RESET_ALL, end='')
    print("")
    print("Total lowspots {0}".format(str(len(lowspots))))
    print("Total lowspot value: {0}".format(
        sum([1 + lowspot[2] for lowspot in lowspots]))
    )


if __name__ == "__main__":
    main()
