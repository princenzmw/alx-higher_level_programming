#!/usr/bin/python3
""" A function that returns the JSON representation of an object (string) """

import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object

    Args:
        my_obj (object): a Python object (data structure)

    Returns:
        str: The JSON representation of a passed object
    """
    return json.dumps(my_obj)
