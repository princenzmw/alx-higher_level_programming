#!/usr/bin/python3
""" A function that writes a string to a text file (`UTF8`)
    and returns the number of characters written """


def write_file(filename="", text=""):
    with open(filename, '+a', encoding='utf-8') as f:
        f.write(text)
    return len(text)
