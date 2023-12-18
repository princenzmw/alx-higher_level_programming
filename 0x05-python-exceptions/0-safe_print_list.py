#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0

    try:
        for i in range(x):
            print(f"{my_list[i]}", end="")
            count += 1
    except IndexError:
        for element in my_list:
            print(f"{element}", end="")
            count += 1

    print()
    return count
