#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tap_a = tuple_a
    new_tap_b = tuple_b

    if len(tuple_a) < 2:
        new_tap_a = tuple_a + (0,) * (2 - len(tuple_a))
    elif len(tuple_b) < 2:
        new_tap_b = tuple_b + (0,) * (2 - len(tuple_b))

    result1 = new_tap_a[0] + new_tap_b[0]
    result2 = new_tap_a[1] + new_tap_b[1]
    return result1, result2
