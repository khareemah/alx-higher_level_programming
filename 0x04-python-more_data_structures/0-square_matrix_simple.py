#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # return [[col * col for col in row] for row in matrix]
    squared_matrix = []
    for row in matrix:
        squared_row = []
        for col in row:
            squared_row.append(col * col)
        squared_matrix.append(squared_row)
    return squared_matrix
