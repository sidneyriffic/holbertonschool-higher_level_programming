#!/usr/bin/python3
"""Defines a function that checks if an object
is exactly an instance of a particular class"""


def is_same_class(obj, a_class):
    return type(obj) == a_class
