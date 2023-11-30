#!/usr/bin/python3

from magic_calculation_102 import add, sub

def magic_calculation(a, b):
    if a < b:
        return add(a, b) + sum(range(4, 6))
    else:
        return sub(a, b)
