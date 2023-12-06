#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    result = sorted(a_dictionary.keys())

    for key in result:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
