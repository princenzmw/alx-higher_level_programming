#!/usr/bin/python3

import sys

argc = len(sys.argv)
argv = sys.argv

if argc < 2:
    print("0 arguments.")
else:
    print("{} arguments:".format(argc - 1))

for i in range(1, argc):
    print("{}: {}".format(i, argv[i]))
