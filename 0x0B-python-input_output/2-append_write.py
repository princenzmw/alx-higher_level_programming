#!/usr/bin/python3
""" A function that appends a string at the end of a text file (`UTF8`)
    and returns the number of characters added """


def append_write(filename="", text=""):
    """ Appends a string to a text file (`UTF8`)
    and returns the number of characters appended.

    Args:
        filename (str, optional): file name. Defaults to "".
        text (str, optional): string to append. Defaults to "".

    Returns:
        int: the number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
