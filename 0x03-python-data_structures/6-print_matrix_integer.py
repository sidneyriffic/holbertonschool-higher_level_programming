#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    for row in matrix:
        if row is not None and len(row) > 0 and row[0] is not None:
            print("{:d}".format(row[0]), end='')
            if len(row) > 1:
                for col in row[1:]:
                    print(" {:d}".format(col), end='')
        print()
