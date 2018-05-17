#!/usr/bin/python3
"""Defines a function that returns a list of lists containing
N sized pascal's triangle"""


def pascal_triangle(n):
    """Returns a pascal's triangle of size n"""
    triangle = []
    n -= 1
    for row in range(n + 1):
        triangle.append([])
        triangle[row].append(1)
        for col in range(int(row / 2)):
            triangle[row].append(triangle[row][col] + row - col - 1)
        if row % 2 == 1:
            triangle[row].extend(triangle[row][::-1])
        else:
            triangle[row].extend(triangle[row][-2::-1])
    return triangle
