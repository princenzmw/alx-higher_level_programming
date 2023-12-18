#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    status = False

    try:
        print("{:d}".format(value))
        status = True
    except ValueError as te:
        print(f"Exception: {te}", file=sys.stderr)
        status = False
    except TypeError as me:
        print(f"{me}", file=sys.stderr)
        status = False

    return status
