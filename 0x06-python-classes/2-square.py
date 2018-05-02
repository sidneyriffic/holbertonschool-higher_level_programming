#!/usr/bin/python3
"""Defines the square class"""


class Square:
    """Square class. Has a size"""
    def __init__(self, size=0):
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        except TypeError:
                raise TypeError("size must be an integer")
