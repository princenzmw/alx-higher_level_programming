#!/usr/bin/python3
""" A Function that adds integers or float numbers """


def add_integer(a, b=98):
    """Add integers

    Args:
        a (int): First value for the addition. must be integer or float
        b (int, optional): Second value for the addition. must be integer
            or float. Defaults to 98.

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer

    Returns:
        int: addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
