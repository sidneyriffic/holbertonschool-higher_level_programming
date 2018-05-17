#!/usr/bin/python3
"""Defines a function that returns a class's serializable dict elements"""


def class_to_json(obj):
    """Returns a class's serializable dict elements as a dict"""
    retdict = {}
    objdict = obj.__dict__
    for ele in objdict:
        if type(objdict[ele]) in [list, dict, str, int, bool]:
            retdict[ele] = objdict[ele]
    return retdict
