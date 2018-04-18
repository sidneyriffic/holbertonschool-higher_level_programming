#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if (row):
            print("{:d}".format(row[0]), end = '')
        for col in row[1:]:
            print(" {:d}".format(col), end ='')
        print()
matrix = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
