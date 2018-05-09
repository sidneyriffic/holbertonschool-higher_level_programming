#!/usr/bin/python3
"""Module containing a class with locked down attributes"""

class LockedClass:
    """Class with locked down attributes. Can only add first_name"""

    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute 'last_name'")
        else:
            self.__dict__[name] = value
