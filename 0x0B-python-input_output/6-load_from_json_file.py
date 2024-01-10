#!/usr/bin/python3
""" A function that creates an Object from a “JSON file” """


import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file

    Args:
        filename (str): JSON file

    Returns:
        A Python object
    """
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data
