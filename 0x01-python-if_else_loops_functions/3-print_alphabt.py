#!/usr/bin/python3
for p in range(97, 123):
    if chr(p) == 'e' or chr(p) == 'q':
        continue
    print("{}".format(chr(p)), end='')
