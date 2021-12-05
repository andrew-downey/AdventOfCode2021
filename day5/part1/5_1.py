#!/usr/bin/env python3
from colored import style
import os
import progressbar


def points_of_line(start: tuple, end: tuple) -> list:
    points = []
    x, y = start
    dx = 0 if start[0] == end[0] else 1 if start[0] < end[0] else -1
    dy = 0 if start[1] == end[1] else 1 if start[1] < end[1] else -1
    if(dx == 0 or dy == 0):
        while x != end[0] + dx or y != end[1] + dy:
            points.append((x, y))
            x += dx
            y += dy
    return points


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    lines = []
    for row in rows:
        line = row.strip().split(" -> ")
        lines.append(
            tuple((
                tuple(map(int, line[0].split(","))),
                tuple(map(int, line[1].split(",")))
            ))
        )

    all_points = []
    for line in lines:
        all_points.append(points_of_line(*line))

    all_points = [item for sub_list in all_points for item in sub_list]

    checklist = []
    overlaps = set()
    bar = progressbar.ProgressBar(len(all_points)).start()
    progress_current = 0
    for point in all_points:
        progress_current += 1
        bar.update(progress_current)
        if point in checklist:
            overlaps.add(point)
        else:
            checklist.append(point)

    print("")
    print(style.BOLD + "Total Overlaps: " + style.RESET + str(len(overlaps)))


if __name__ == "__main__":
    main()
