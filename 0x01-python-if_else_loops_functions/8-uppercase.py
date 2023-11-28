#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for ch in str:
        ascii_val = ord(ch)
        if 97 <= ascii_val <= 122:
            ascii_val -= 32
        upper_str += chr(ascii_val)
    print("{}".format(upper_str))
