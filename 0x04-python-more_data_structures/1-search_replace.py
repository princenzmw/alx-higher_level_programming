#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        my_list = []
    
    for i, value in enumerate(my_list):
        if value == search:
            my_list[i] = replace
        else:
            my_list[i] = value

    return my_list
