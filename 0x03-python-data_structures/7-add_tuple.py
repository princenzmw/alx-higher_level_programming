#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res1 = tuple_a + (0, 0)
    res2 = tuple_b + (0, 0)
    final_result = (res1[0] + res2[0], res1[1] + res2[1])

    return final_result
