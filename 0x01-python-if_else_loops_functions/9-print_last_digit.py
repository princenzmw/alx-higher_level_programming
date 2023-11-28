#!/usr/bin/python3
def print_last_digit(number):
    last_dig = number % 10
    print(last_dig if number >= 0 else -last_dig, end='')
    return abs(last_dig)
