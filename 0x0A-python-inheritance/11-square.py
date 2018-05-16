#!/usr/bin/python3
"""Defines the square class which inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class based on Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self._Rectangle__width,
                                           self._Rectangle__height)
