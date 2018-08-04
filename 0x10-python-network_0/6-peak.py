#!/usr/bin/python3
"""Module to find the peak in a list of integers"""


def find_peak(list_of_integers):
    """Finds the peak in a list of integers"""

    if len(list_of_integers) == 0:
        return None
    peak = list_of_integers[0]
    for num in list_of_integers:
        if num < peak:
            return peak
        peak = num
    return peak
