#!/usr/bin/python3
for alpha in range(ord('z'), ord('a') - 1, -1):
    case_adj = 0 if alpha % 2 == 0 else 32
    print("{}".format(chr(alpha - case_adj)), end='')
