#!/usr/bin/python3

import sys
if __name__ == "__main__":
    argc = len(sys.argv)
    argv = sys.argv

    if argc < 2:
        print("0 arguments.")
    elif argc == 2:
        print("{} argument:".format(argc - 1))
    else:
        print("{} arguments:".format(argc - 1))

    for i in range(1, argc):
        print("{}: {}".format(i, argv[i]))
