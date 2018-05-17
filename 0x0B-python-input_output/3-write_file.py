#!/usr/bin/python3
"""Defines a function that writes a string to a file"""


def write_file(filename="", text=""):
    """Writes a string to a given file"""
    with open(filename, "w") as f:
        return f.write(text)
