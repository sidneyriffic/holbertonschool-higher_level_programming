#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 | idx > my_list.len():
        return my_list
    listcpy = my_list.copy()
    listcpy[idx] = element
    return listcpy
