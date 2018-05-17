#!/usr/bin/python3
"""Defines a function that prints number of lines in a UTF8 text file"""


def number_of_lines(filename=""):
    with open(filename, "r") as f:
        lines = 0
        for line in f:
            lines += 1
        return lines
