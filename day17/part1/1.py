#!/usr/bin/env python3
import os
import re
from typing import DefaultDict, Dict, List, Tuple
from progressbar.progressbar import ProgressBar

MAX_STEPS = 400


class Probe:
    def __init__(self, initial_x, initial_y) -> None:
        self.x: int = 0
        self.y: int = 0
        self.y_max: int = 0
        self.initial_x = initial_x
        self.initial_y = initial_y
        self.x_velocity: int = initial_x
        self.y_velocity: int = initial_y

    def step(self) -> Tuple[int, int]:
        self.x += self.x_velocity
        self.y += self.y_velocity
        self.y_max = max(self.y, self.y_max)
        self.x_velocity += -1 if self.x_velocity > 0 else 1 if self.x_velocity < 0 else 0
        self.y_velocity -= 1
        return (self.x, self.y)


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    # target area: x=20..30, y=-10..-5
    target_coords = {coord[0]: tuple(map(int, coord[1].split(
        ".."))) for coord in re.findall(r"([xy])=([-\d]+..[-\d]+)", rows[0])}
    grid: Dict[int, Dict[int, str]] = DefaultDict(dict)
    for y in range(15, target_coords["y"][0] - 15, -1):
        for x in range(-15, target_coords["x"][1] + 15):
            grid[y][x] = "T" if (target_coords["y"][0] <= y <= target_coords["y"][1]) and (
                target_coords["x"][0] <= x <= target_coords["x"][1]) else "."
    grid[0][0] = "S"
    grid_y = (min(grid.keys()), max(grid.keys()))
    grid_x = (min(grid[0].keys()), max(grid[0].keys()))

    print("Target range: {0}".format(target_coords))

    debug_velocities = []
    successful_probes: List[Probe] = []
    min_x_velocity = 1
    min_y_velocity = 1
    progress = ProgressBar(29 * 399).start()
    for x_velocity in range(min_x_velocity, 30):
        for y_velocity in range(min_y_velocity, 400):
            progress.update(x_velocity * y_velocity)
            probe = Probe(x_velocity, y_velocity)
            probe_grid = {y: {x: char for x, char in row.items()}
                          for y, row in grid.items()}
            if (x_velocity, y_velocity) in debug_velocities:
                print("Attempting probe {0}, {1}".format(
                    x_velocity, y_velocity))
            steps = 0
            while steps <= MAX_STEPS:
                steps += 1
                x, y = probe.step()
                if x > target_coords["x"][1] or y < target_coords["y"][0]:
                    # Out of bounds
                    break
                if grid_y[0] < y < grid_y[1] and grid_x[0] < x < grid_x[1]:
                    probe_grid[y][x] = "#"
                if target_coords["x"][0] <= x <= target_coords["x"][1] and target_coords["y"][0] <= y <= target_coords["y"][1]:
                    successful_probes.append(probe)
                    min_y_velocity = y_velocity
                    # debug_draw_grid(probe_grid)
                    break

            if (x_velocity, y_velocity) in debug_velocities:
                debug_draw_grid(probe_grid)
    progress.finish()

    y_maximums = {(probe.initial_x, probe.initial_y): probe.y_max for probe in successful_probes}
    y_maximum = sorted(y_maximums.items(), key=lambda x: x[1], reverse=True)[0]
    print("Success: yMax {0} with {1}, {2}".format(
        y_maximum[1], y_maximum[0][0], y_maximum[0][1]))


def debug_draw_grid(grid: Dict[int, Dict[int, str]]):
    for y, row in grid.items():
        print("{0:>3}: ".format(y), end="")
        for point in row.values():
            print(point, end="")
        print("")
        print("")


if __name__ == "__main__":
    main()
