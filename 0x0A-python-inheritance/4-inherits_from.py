#!/usr/bin/python3
"""Checks if an object is a subclass of another class"""


def inherits_from(obj, a_class):
    return issubclass(type(obj), a_class)
