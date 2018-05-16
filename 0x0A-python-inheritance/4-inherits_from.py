#!/usr/bin/python3
"""Checks if an object is a subclass of another class"""


def inherits_from(obj, a_class):
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
