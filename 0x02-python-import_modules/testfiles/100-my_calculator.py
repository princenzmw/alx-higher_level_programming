#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    argc = len(sys.argv) - 1

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    add_result = add(a, b)
    sub_result = sub(a, b)
    mul_result = mul(a, b)
    div_result = div(a, b)

    if sys.argv[2] == '+':
        print("{} + {} = {}".format(a, b, add_result))
    elif sys.argv[2] == '-':
        print("{} - {} = {}".format(a, b, sub_result))
    elif sys.argv[2] == '*':
        print("{} * {} = {}".format(a, b, mul_result))
    elif sys.argv[2] == '/':
        print("{} / {} = {}".format(a, b, div_result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
