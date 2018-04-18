#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (my_list is None) or (idx is None) or (idx < 0) or (idx > len(my_list)):
        return my_list
    listcpy = my_list.copy()
    listcpy[idx] = element
    return listcpy
my_list = None
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
