#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return None
    dictcpy = {}
    for x, y in a_dictionary.items():
        dictcpy[x] = y * 2
    return dictcpy
