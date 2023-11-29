#!/usr/bin/python3
def uppercase(str):
    result_str = ""
    for ch in str:
        if 'a' <= ch <= 'z':
            result_str += chr(ord(ch) - ord('a') + ord('A'))
        else:
            result_str += ch
    print("{}".format(result_str))


uppercase("best")
uppercase("Best School 98 Battery street")
