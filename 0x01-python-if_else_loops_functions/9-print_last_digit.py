#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_dig = number % -10
        print("{}".format(last_dig))
    else:
        last_dig = number % 10
        print("{}".format(last_dig))
    return last_dig
