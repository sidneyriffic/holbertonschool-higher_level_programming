#!/usr/bin/python3
"""Module contains function that adds two integer values"""


def add_integer(a, b=98):
    """Adds two numbers as integers, second has defaut value of 98"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
