#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except (TypeError, ValueError, ZeroDivisionError, IndexError) as fe:
        print(f"Exception: {fe}", file=sys.stderr)
        return None
