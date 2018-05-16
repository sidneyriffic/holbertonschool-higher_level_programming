#!/usr/bin/python3
"""Defined a list class with member function that prints a sorted list"""


class MyList(list):
    def print_sorted(self):
        """Prints MyList, sorted"""
        print(sorted(self))
