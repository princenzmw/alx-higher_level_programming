#!/usr/bin/python3
""" A function that returns an object (Python data structure)
    represented by a JSON string """


import json


def from_json_string(my_str):
    """Return a Python data structure represented by a JSON string.

    Args:
        my_str (JSON): a JSON string

    Returns:
        _type_: A Python data structure
    """
    return json.loads(my_str)
