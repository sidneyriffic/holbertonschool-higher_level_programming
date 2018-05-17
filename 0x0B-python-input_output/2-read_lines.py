#!/usr/bin/python3
"""Defines a function that prints n number of lines from a file"""


def read_lines(filename="", nb_lines=0):
    with open(filename, "r") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            for line in f:
                print(line, end="")
                nb_lines -= 1
                if nb_lines == 0:
                    break
