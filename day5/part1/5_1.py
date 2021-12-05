#!/usr/bin/env python3
from colored import style
import threading
import concurrent.futures as futures
import os
import re


class VentLine:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)
        self.points = None

    def getpoints(self):
        if(self.points == None):
            self.points = []
            for x in range(self.x2 - self.x1):
                for y in range(self.y2 - self.y1):
                    self.points.append([x, y])
        return self.points

    def testpoints(self, points):
        overlaps = 0
        for point in points:
            if(self.testpoint(point[0], point[1])):
                overlaps += 1
        return overlaps

    def testpoint(self, x, y):
        return ((x >= self.x1 and x <= self.x2) and (y >= self.y1 and y <= self.y2))


def testoverlaps(ventline, ventlines):
    overlaps = 0
    for testventline in ventlines:
        if(testventline != ventline):
            overlaps += ventline.testpoints(testventline.getpoints())
    return overlaps


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        lines = myfile.read().splitlines()

    coords = [coord for coord in lines if coord[0][0]
              == coord[1][0] or coord[0][1] == coord[1][1]]

    # print("Creating VentLine objects...")
    # ventlines = []
    # for line in lines:
    #     coords = re.findall("(\d+),(\d+)", line)
    #     ventlines.append(
    #         VentLine(coords[0][0], coords[0][1], coords[1][0], coords[1][1])
    #     )

    # overlaps = 0
    # tasks = []
    # print("Creating {0} check overlap threads...".format(len(ventlines)))
    # with futures.ThreadPoolExecutor(12) as pool:
    #     for ventline in ventlines:
    #         if(len(tasks) % 10 == 0):
    #             print(".", end="")
    #         tasks.append(pool.submit(
    #             testoverlaps, ventline, ventlines)
    #         )

    #     print("")
    #     print("Collecting {0} results...".format(len(tasks)))
    #     progress = 0
    #     for task in futures.as_completed(tasks):
    #         progress += 1
    #         if(progress % 10 == 0):
    #             print(".", end="")
    #         overlaps += task.result()

    print("")
    print(style.BOLD + "Total Overlaps: " + style.RESET + str(overlaps))


if __name__ == "__main__":
    main()
