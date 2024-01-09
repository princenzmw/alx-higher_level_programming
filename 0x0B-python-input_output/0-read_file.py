#!/usr/bin/python3
""" A  function that reads a text file (UTF8) and prints it to stdout """


def read_file(filename=""):
    """read a file

    Args:
        filename (str, optional): a file's name. Defaults to "".
    """
    with open(filename, encoding="utf-8") as f:
        file_cont = f.read()

    print(file_cont[:-1])
