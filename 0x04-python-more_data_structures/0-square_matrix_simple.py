#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = []
    for elem in matrix:
        new_mat.append(elem[:])

    for lis in new_mat:
        for i in range(len(lis)):
            lis[i] *= lis[i]
    return new_mat
