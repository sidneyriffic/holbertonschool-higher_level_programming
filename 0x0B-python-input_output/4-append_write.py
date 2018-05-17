#!/usr/bin/python3
"""Defines a function that appends a string to a file"""


def append_write(filename="", text=""):
    """Writes a string to a given file"""
    with open(filename, "a") as f:
        return f.write(text)
