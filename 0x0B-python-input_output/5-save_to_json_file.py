#!/usr/bin/python3
""" A function that writes an Object to a text file,
    using a JSON representation """


import json


def save_to_json_file(my_obj, filename):
    """ Writes an Object to a text file,
    using a JSON representation

    Args:
        my_obj (obj): a Python object
        filename (file): a file-like object

    Returns:
        JSON : Write a Python object as a JSON string to a file-like object
    """
    with open(filename, "a", encoding='utf-8') as file:
        json.dump(my_obj, file)
