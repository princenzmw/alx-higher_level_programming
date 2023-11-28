#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if 65 <= ord(ch) >= 90:
            ch = ord(ch) - 32
            char = chr(ch)
            print("{}".format(char), end="")
        else:
            print("{}".format(ch), end="")
    print()
