#!/usr/bin/env python3
import os
from shell_colours import Colour, bold


class BingoNumber:
    def __init__(self, number, stamped):
        self.number = int(number)
        self.stamped = stamped

    def stamp(self):
        self.stamped = True

    def debug(self):
        if(self.stamped):
            return bold('{0:^4}'.format(self.number))
        else:
            return '{0: ^4}'.format(self.number)


class Board:
    def __init__(self, number_lines):
        self.finished = False
        self.number_lines = []
        for line in number_lines:
            bingo_line = []
            for number in line:
                bingo_line.append(BingoNumber(number, False))
            self.number_lines.append(bingo_line)

    def stamp(self, new_number):
        for number_line in self.number_lines:
            for number in number_line:
                if(number.number == new_number):
                    number.stamp()
        return self

    def check(self):
        # rows
        for row in range(len(self.number_lines[0])):
            all_stamped = True
            for col in self.number_lines[row]:
                if(not col.stamped):
                    all_stamped = False
            if(all_stamped):
                return True

        # columns
        for col in range(len(self.number_lines)):
            all_stamped = True
            for row in range(len(self.number_lines[0])):
                if(not self.number_lines[row][col].stamped):
                    all_stamped = False
            if(all_stamped):
                return True

        return False

    def score(self, score_mul):
        score = 0
        for line in self.number_lines:
            for number in line:
                if(not number.stamped):
                    score += number.number
        return score * score_mul

    def debug(self):
        for number_line in self.number_lines:
            debug_line = []
            for number in number_line:
                debug_line.append(number.debug())
            print(''.join(debug_line))


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        lines = myfile.read().splitlines()

    bingo_callouts = lines[0]
    bingo_boards = []

    bingo_lines = []
    for i in range(2, len(lines)):
        if(len(lines[i].strip()) != 0):
            bingo_numbers = lines[i].split()
            bingo_lines.append(bingo_numbers)
            if(len(bingo_lines) == 5):
                bingo_boards.append(Board(bingo_lines[:]))
                bingo_lines.clear()

    # Stamp the bingo boards
    loser = None
    loser_score = 0
    winners = 0
    for number in bingo_callouts.split(","):
        number = int(number)
        for i in range(len(bingo_boards)):
            current_board = bingo_boards[i]
            if(not current_board.finished and current_board.stamp(number).check()):
                current_board.finished = True
                winners += 1
                if(winners == len(bingo_boards)):
                    loser = i
                    winning_number = number
                    loser_score = current_board.score(winning_number)
                    break
        if(loser != None):
            break

    print("Total bingo boards: {0}".format(len(bingo_boards)))
    print("Bingo callouts: {0}".format(bingo_callouts))
    print("losing board {0}".format(loser + 1))
    print("winning callout {0}".format(winning_number))
    print("loser board score {0}".format(
        int(loser_score / int(winning_number))))
    print("loser total score {0}".format(loser_score))
    bingo_boards[loser].debug()
    # for board in bingo_boards:
    #     print("")
    #     board.debug()


if __name__ == "__main__":
    main()
