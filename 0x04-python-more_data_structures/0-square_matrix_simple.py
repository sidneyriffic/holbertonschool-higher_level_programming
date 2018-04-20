#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    return list(list(map(lambda x: x ** 2, y)) for y in matrix)
