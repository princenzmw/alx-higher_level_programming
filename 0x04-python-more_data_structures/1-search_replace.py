#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        my_list = []
    if search not in my_list:
        return my_list

    new_list = my_list.copy()
    
    for i, value in enumerate(new_list):
        if value == search:
            new_list[i] = replace

    return new_list
