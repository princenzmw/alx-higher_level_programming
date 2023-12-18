#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    elements = 0
    count = 0

    for _ in my_list:
        elements += 1

    try:
        if x <= elements:
            for i in range(x):
                print(f"{my_list[i]}", end="")
                count += 1
        else:
            for q in range(elements):
                print(f"{my_list[q]}", end="")
                count += 1
    except IndexError:
        for t in range(elements):
            print(f"{t}", end="")
            count += 1
    print()
    return count
