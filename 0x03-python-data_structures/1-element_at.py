#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 | idx >= my_list.len():
        return
    return my_list[idx]
