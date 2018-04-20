#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    for x in sorted(a_dictionary):
        print("{}: {}".format(x, a_dictionary[x]))
