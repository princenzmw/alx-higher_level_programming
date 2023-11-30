#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    plural = "s" if argc != 1 else ""
    separator = ":" if argc > 0 else "."

    print("{} argument{}{}".format(argc, plural, separator))

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
