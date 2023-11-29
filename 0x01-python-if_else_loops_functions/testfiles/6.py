#!/usr/bin/python3
for tens in range(10):
    for ones in range(tens + 1, 10):
        if tens == 8 and ones == 9:
            print('89')
        else:
            print("{}{}".format(tens, ones), end=', ')
