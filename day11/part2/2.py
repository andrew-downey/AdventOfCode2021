#!/usr/bin/env python3
import os
import colorama


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    grid = [[int(num) for num in row] for row in rows]
    height = len(grid)
    width = len(grid[0])
    flashes = 0

    print("")
    print("Before any steps:")
    for row in grid:
        [print((colorama.ansi.Style.BRIGHT if cell == 0 else colorama.ansi.Fore.RED if cell == 9 else colorama.ansi.Style.DIM) + str(cell) +
               colorama.ansi.Style.RESET_ALL, end='') for cell in row]
        print("")
    print("")

    step = 0
    while sum([sum(row) for row in grid]) > 0:
        step += 1
        # Step 1) Add 1 to all cells
        grid = [[cell + 1 for cell in row] for row in grid]
        next_grid = grid[:]
        flashers = [[cell for cell in row if cell > 9]
                    for row in grid]
        flashers = [item for sub_list in flashers for item in sub_list]
        has_flashed = []

        # For each number at 9, increase the neighbourhood
        while len(flashers) > 0:
            for y in range(height):
                for x in range(width):
                    octopus = grid[y][x]
                    if octopus > 9 and (y, x) not in has_flashed:
                        flashes += 1
                        has_flashed.append((y, x))
                        for ny in range(-1, 2):
                            for nx in range(-1, 2):
                                # if(x == 0 and y == 0):
                                #     continue
                                if(y + ny < height and y + ny >= 0 and x + nx < width and x + nx >= 0):
                                    next_grid[y + ny][x + nx] += 1

            # Copy the new grid to working grid
            grid = [[cell for cell in row]
                    for row in next_grid]
            flashers = [[cell for x, cell in enumerate(row) if cell > 9 and (y, x) not in has_flashed]
                        for y, row in enumerate(grid)]
            flashers = [item for sub_list in flashers for item in sub_list]

        # Zero the energy on any flashers
        grid = [[cell if cell <= 9 else 0 for cell in row]
                for row in next_grid]

        # if(step % 10 == 0):
        print("")
        print("After step {0}:".format(step))
        for row in grid:
            [print((colorama.ansi.Style.BRIGHT if cell == 0 else colorama.ansi.Fore.RED if cell == 9 else colorama.ansi.Style.DIM) + str(cell) +
                   colorama.ansi.Style.RESET_ALL, end='') for cell in row]
            print("")
        print("")

    print("")
    print("Total flashes: {0}".format(flashes))


if __name__ == "__main__":
    main()
