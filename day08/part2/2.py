#!/usr/bin/env python3
import os

EASY_DIGITS = [2, 3, 4, 7]


class Digit:
    def __init__(self, code: str):
        self.code: str = code
        self.code_length = len(code)
        self.number = -1

    def get_number(self):
        if(self.number == -1):
            if(self.code_length == 2):
                self.number = 1
            elif(self.code_length == 3):
                self.number = 7
            elif(self.code_length == 4):
                self.number = 4
            elif(self.code_length == 7):
                self.number = 8
        return self.number

    def contains(self, digit: str):
        return len(self.subtract(digit)) == (self.code_length - len(digit))

    def subtract(self, b: str):
        return "".join(c for c in self.code if c not in b)


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    output_sum = 0
    for index, row in enumerate(rows):
        digits_input, digits_output = row.split(' | ')
        digits_input = [Digit(digit)
                        for digit in digits_input.split(' ')]
        digits_output = [Digit(digit)
                         for digit in digits_output.split(' ')]
        all_digits = digits_input + digits_output

        row_dict = {digit.get_number(
        ): digit for digit in all_digits if digit.get_number() != -1}
        four_minus_one = row_dict[4].subtract(row_dict[1].code)

        for digit in all_digits:
            if(digit.get_number() != -1):
                continue

            if(digit.code_length == 5):
                if(digit.contains(row_dict[1].code)):
                    row_dict[3] = digit
                elif(digit.contains(four_minus_one)):
                    row_dict[5] = digit
                else:
                    row_dict[2] = digit
            elif(digit.code_length == 6):
                if(digit.contains(row_dict[4].code)):
                    row_dict[9] = digit
                elif(digit.contains(four_minus_one)):
                    row_dict[6] = digit
                else:
                    row_dict[0] = digit

        row_dict = {index: "".join(sorted(value.code))
                    for index, value in row_dict.items()}

        output = ""
        for digit in digits_output:
            for dict_key, dict_value in row_dict.items():
                if(dict_value == "".join(sorted(digit.code))):
                    output += str(dict_key)

        print("Row {0}: {1} - {2}".format(
            index, output, row_dict)
        )
        output_sum += int(output)

    print("")
    print("Sum of all outputs: {0}".format(output_sum))


if __name__ == "__main__":
    main()
