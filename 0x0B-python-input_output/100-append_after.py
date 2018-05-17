#!/usr/bin/python3
"""Defines a function that adds text to a file after every line where a
given substring is found"""


def append_after(filename="", search_string="", new_string=""):
    """Adds text to a file after every line where a given substring
    is found"""
    with open(filename, "r+") as f:
        text = ""
        for line in f:
            if search_string in line:
                line += new_string
            text += line
        f.seek(0)
        f.write(text)
