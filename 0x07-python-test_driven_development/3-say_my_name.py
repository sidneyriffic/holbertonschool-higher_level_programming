#!/usr/bin/python3
"""Module containing a function that prints two strings as a name"""


def say_my_name(first_name, last_name=""):
    """Prints two strings as a name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    print("My name is", first_name, end=" ")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(last_name)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
