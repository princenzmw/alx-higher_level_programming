#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_dig = number % -10
        print(last_dig, sep='')
    else:
        last_dig = number % 10
        print(last_dig, sep='')
    return abs(last_dig)
