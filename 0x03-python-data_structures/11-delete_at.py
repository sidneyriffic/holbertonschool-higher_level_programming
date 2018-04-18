#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list is None or idx is None or idx >= len(my_list):
        return None
    del my_list[idx]
    return my_list
