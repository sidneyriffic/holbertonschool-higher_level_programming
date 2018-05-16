#!/usr/bin/python3
"""Defines the MyInt class"""


class MyInt(int):
    """Integer but with == and != reversed"""

    def __init__(self, myint):
        self.myint = myint

    def __eq__(int1, int2):
        return int1.myint != int2

    def __ne__(int1, int2):
        return int1.myint == int2
