#!/usr/bin/python3
""" A function that writes a string to a text file (`UTF8`)
    and returns the number of characters written """


def write_file(filename="", text=""):
    """writes a string to a text file (`UTF8`)
    and returns the number of characters written

    Args:
        filename (str, optional): file name. Defaults to "".
        text (str, optional): string to write. Defaults to "".

    Returns:
        int: the number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
