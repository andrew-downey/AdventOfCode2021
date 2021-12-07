#!/usr/bin/env python3
from colored import style
import os

DEFAULT_TIMER = 6
DEFAULT_FRESH_TIMER = 8
DAYS_TO_SIMULATE = 80


class Lanternfish:
    def __init__(self, timer=DEFAULT_TIMER) -> None:
        self.timer = timer

    def update(self):
        if(self.timer == 0):
            self.timer = DEFAULT_TIMER
            return True
        else:
            self.timer -= 1
        return False


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        row = myfile.read().splitlines()[0]

    lanternfish = []
    for timer in row.strip().split(","):
        lanternfish.append(Lanternfish(int(timer)))

    print("Initial state: {0}".format(
        [fish.timer for fish in lanternfish[0:10]]))
    for i in range(1, DAYS_TO_SIMULATE + 1):
        newfish = []
        for fish in lanternfish:
            if(fish.update()):
                newfish.append(Lanternfish(DEFAULT_FRESH_TIMER))
        lanternfish += newfish
        print("After {0:>2} {2}: {1}".format(
            i,
            [fish.timer for fish in lanternfish[0:10]],
            "days" if i > 0 else "day"
        )
        )

    print("")
    print(style.BOLD + "Total Lanternfish after {0} days: ({1})".format(DAYS_TO_SIMULATE,
                                                                        len(lanternfish)) + style.RESET)


if __name__ == "__main__":
    main()
