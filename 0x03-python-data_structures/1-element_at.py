#!/usr/bin/python3
def element_at(my_list, idx):
    if (my_list is None) or (idx is None)\
       or (idx < 0) or (idx >= len(my_list)):
        return
    return my_list[idx]
