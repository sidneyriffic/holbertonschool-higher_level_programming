#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    return [replace if x == search else x for x in my_list]
