#!/usr/bin/env python3
from collections import deque
import os
from time import time
from typing import DefaultDict, Dict, List, Tuple


class Beacon:
    def __init__(self, x: int, y: int, z: int = 0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def get_position(self, rotation: int):
        coords = (self.x, self.y, self.z)
        if rotation == 0:
            coords = (self.x, self.y, self.z)
        elif rotation == 1:
            coords = (self.x, -self.z, self.y)
        elif rotation == 2:
            coords = (self.x, -self.y, -self.z)
        elif rotation == 3:
            coords = (self.x, self.z, -self.y)
        elif rotation == 4:
            coords = (self.y, self.z, self.x)
        elif rotation == 5:
            coords = (self.y, -self.x, -self.z)
        elif rotation == 6:
            coords = (self.y, -self.z, -self.x)
        elif rotation == 7:
            coords = (self.y, self.x, -self.z)
        elif rotation == 8:
            coords = (self.z, self.x, self.y)
        elif rotation == 9:
            coords = (self.z, -self.y, self.x)
        elif rotation == 10:
            coords = (self.z, -self.x, -self.y)
        elif rotation == 11:
            coords = (self.z, self.y, -self.x)
        elif rotation == 12:
            coords = (-self.z, -self.y, -self.x)
        elif rotation == 13:
            coords = (-self.z, self.x, -self.y)
        elif rotation == 14:
            coords = (-self.z, self.y, self.x)
        elif rotation == 15:
            coords = (-self.z, -self.x, self.y)
        elif rotation == 16:
            coords = (-self.y, -self.x, -self.z)
        elif rotation == 17:
            coords = (-self.y, self.z, -self.x)
        elif rotation == 18:
            coords = (-self.y, self.x, self.z)
        elif rotation == 19:
            coords = (-self.y, -self.z, self.x)
        elif rotation == 20:
            coords = (-self.x, -self.z, -self.y)
        elif rotation == 21:
            coords = (-self.x, self.y, -self.z)
        elif rotation == 22:
            coords = (-self.x, self.z, self.y)
        elif rotation == 23:
            coords = (-self.x, -self.y, self.z)
        return coords

    def distance_to(self, beacon: "Beacon") -> Tuple:
        manhattan_distance = []
        for self_i, beacon_i in zip((self.x, self.y, self.z), (beacon.x, beacon.y, beacon.z)):
            manhattan_distance.append(self_i - beacon_i)

        return tuple(manhattan_distance)

    def represent(self) -> Tuple[int, int, int]:
        return (self.x, self.y, self.z)


class Scanner:
    def __init__(self, index) -> None:
        self.rotation = 0
        self.index = index
        self.x = 0
        self.y = 0
        self.z = 0
        self.beacons = []

    def set_position(self, position):
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]

    def calculate_distances(self, test_scanner: "Scanner") -> Dict[int, int]:
        distances = DefaultDict(int)
        for beacon in self.beacons:
            for test_beacon in test_scanner.get_beacons():
                distances[beacon.distance_to(test_beacon)] += 1
        return distances

    def next_rotation(self) -> None:
        self.rotation += 1
        if self.rotation > 23:
            self.rotation = 0

    def get_beacons(self) -> List[Beacon]:
        beacons = [Beacon(*beacon.get_position(self.rotation))
                   for beacon in self.beacons]
        for beacon in beacons:
            beacon.x += self.x
            beacon.y += self.y
            beacon.z += self.z
        return beacons

    def debug(self):
        print("Scanner {4} at {0},{1},{2} with {3} beacons".format(
            self.x, self.y, self.z, len(self.beacons), self.index))
        [print("  {0},{1},{2}".format(beacon.x, beacon.y, beacon.z))
         for beacon in self.beacons]

    def dedupe(self) -> int:
        starting_beacons = len(self.beacons)
        # print("  Deduping: started with {0}".format(starting_beacons))
        new_beacons_list = []
        new_beacons_representations = []
        for index, beacon in enumerate(self.beacons):
            # print("    Considering beacon at {0}".format(beacon.represent()))
            if beacon.represent() not in new_beacons_representations:
                new_beacons_representations.append(beacon.represent())
                new_beacons_list.append(beacon)
        self.beacons = new_beacons_list
        ending_beacons = len(self.beacons)
        # print("  Deduping: ended with {0}".format(len(self.beacons)))
        return starting_beacons - ending_beacons


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    all_scanners: List[Scanner] = []
    current_scanner = None
    for row in rows:
        if len(row.strip()) > 0:
            if "---" in row:
                current_scanner = Scanner(len(all_scanners))
                all_scanners.append(current_scanner)
            else:
                try:
                    x, y, z = list(map(int, row.split(",")))
                except ValueError:
                    x, y = list(map(int, row.split(",")))
                    z = 0
                if(current_scanner == None):
                    raise Exception("Adding beacon but no scanner")
                current_scanner.beacons.append(Beacon(x, y, z))

    # [scanner.debug() for scanner in all_scanners]
    print("")

    root_scanner = all_scanners[0]
    unknown_scanners = deque(all_scanners[1:])
    while len(unknown_scanners) > 0:
        scanner = unknown_scanners.popleft()
        distances = root_scanner.calculate_distances(scanner)
        common_distances = sorted(distances.values(), reverse=True)
        print(common_distances[:5])
        common_distance = common_distances[0]

        if common_distance >= 12:
            distances = [offset for offset, distance in distances.items()
                         if distance == common_distance]
            offset = distances[0]
            print("Scanner {0} has >= 12 overlaps in orientation {1} with offset {2}".format(
                scanner.index, scanner.rotation, offset))
            scanner.set_position(offset)
            original_beacons = root_scanner.beacons[:]
            root_scanner.beacons += scanner.get_beacons()
            if root_scanner.dedupe() < 12:
                print("Unexpected dedupe count, adding back to list")
                scanner.set_position((0, 0, 0))
                root_scanner.beacons = original_beacons
                unknown_scanners.append(scanner)
        else:
            print("Scanner {0} needs to be rotated to find overlaps".format(
                scanner.index))
            scanner.next_rotation()
            unknown_scanners.append(scanner)

    print("Total beacons: {0}".format(len(root_scanner.beacons)))


if __name__ == "__main__":
    start = time()
    main()
    end = time()
    print(f'Finished in {round(end - start, 2)} seconds')
