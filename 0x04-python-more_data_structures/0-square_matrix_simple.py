#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[col * col for col in row] for row in matrix]
