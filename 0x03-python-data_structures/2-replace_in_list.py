#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if (idx < 0) | (idx > my_list.len()):
        return my_list
    my_list[idx] = element
