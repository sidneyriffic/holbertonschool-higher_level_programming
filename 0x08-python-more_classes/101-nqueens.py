#!/usr/bin/python3
"""Standalone module to solve the nqueens problem"""


import sys


def nqueens(size):
    """Initial setup before recursive call"""
    if type(size) is not int:
        print("N must be a number")
        return
    if size < 4:
        print("N must be at least 4")
        return
    queens = [0] * size

    def printsolution(queens):
        print("[[0, ", queens[0], "]", sep="", end="")
        for y, x in enumerate(queens[1:], 1):
            print(", [", y, ", ", x, "]", sep="", end="")
        print("]")

    def queencalc(queen):
        """Recursive call queen position validator"""
        for x in range(size):
            """horizontal board positions per queen"""
            nextx = 0
            for y in range(queen):
                qx = queens[y]
                if x == qx or x + queen == qx + y or x - queen == qx - y:
                    nextx = 1
                    break
            if nextx == 1:
                nextx == 0
                continue
            if queen != size - 1:
                queens[queen + 1] = 0
                queens[queen] = x
                queencalc(queen + 1)
            else:
                queens[queen] = x
                printsolution(queens)
    queencalc(0)

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit()
try:
    size = int(sys.argv[1])
except (ValueError, TypeError):
    print("N must be a number")
    exit()
nqueens(size)
