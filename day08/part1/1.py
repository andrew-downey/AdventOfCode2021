#!/usr/bin/env python3
import os


EASY_DIGITS = [2, 3, 4, 7]


class Digit:
    def __init__(self, code: str):
        self.code = code
        self.code_length = len(code)
        self.number = None

    def get_number(self):
        if(self.number == None):
            if(self.code_length == 2):
                self.number = 1
            elif(self.code_length == 3):
                self.number = 7
            elif(self.code_length == 4):
                self.number = 4
            elif(self.code_length == 7):
                self.number = 8
        return self.number


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    all_digits_input = []
    all_digits_output = []
    for row in rows:
        digits_input, digits_output = row.split(' | ')
        all_digits_input += [Digit(digit) for digit in digits_input.split(' ')]
        all_digits_output += [Digit(digit)
                              for digit in digits_output.split(' ')]

    print([digit.get_number()
          for digit in all_digits_output if digit.get_number() != None])
    output_easy_digits = [
        digit for digit in all_digits_output if digit.get_number() != None
    ]

    print("")
    print("Count of [1, 4, 7, 8] in output: " + str(len(output_easy_digits)))


if __name__ == "__main__":
    main()
