#!/usr/bin/python3
from magic_calculation_102 import add, sub

if __name__ == "__main__":
    def magic_calculation(a, b):
        if a < b:
            c = add(a, b)
            for i in range(4, 6):
                c = add(c, i)
            return c
        else:
            return (sub(a, b))
