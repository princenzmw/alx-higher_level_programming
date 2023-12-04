#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for num_list in matrix:
        for num in num_list:
            print("{}".format(num), end=" " if num is not
                  num_list[len(num_list) - 1] else '')
        else:
            print()
