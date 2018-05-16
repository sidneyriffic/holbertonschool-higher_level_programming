#!/usr/bin/python3
"""Defines the BaseGeometry class"""


class BaseGeometry:
    """Base class for geometry objects"""

    def area(self):
        """Returns area of geometry object if implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates whether values is an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
