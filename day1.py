import csv
import cProfile

digit_map = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
            "zero": "0",
        }
def findfirstdigit(current_string):
    digit1 = None
    l = 0
    while l <= len(current_string):
        k = l + 1
        while k - l <= 5:
            sub_string = current_string[l:k]
            if sub_string.isnumeric() or sub_string in digit_map:
                if sub_string.isnumeric():
                    digit1 = sub_string
                else:
                    digit1 = digit_map[sub_string]
                return digit1
            k = k + 1
        l = l + 1


def findlastdigit(current_string):
    digit2 = None
    k = len(current_string)
    while k > 0:
        l = k - 1
        while k - l <= 5:
            sub_string = current_string[l:k]
            if sub_string.isnumeric() or sub_string in digit_map:
                if sub_string.isnumeric():
                    digit2 = sub_string
                else:
                    digit2 = digit_map[sub_string]
                return digit2
            l = l - 1
        k = k - 1


def day1():
    with open("inputs/day1.txt") as f:
        reader = csv.reader(f, delimiter=",")
        digits = 0
        total_num = 0
        for row in reader:
            current_string = row[0]
            digit1 = findfirstdigit(current_string)
            digit2 = findlastdigit(current_string)
            digits = digits + (int(digit1) * 10 + int(digit2))
            total_num = total_num + 1
        print(digits)


day1()
