#!/usr/bin/python3
def replace_in_list(my_list, idx, element):

    result = []

    if idx < 0:
        result = my_list
    elif idx >= len(my_list):
        result = my_list
    else:
        my_list[idx] = element
        result = my_list

    return result
