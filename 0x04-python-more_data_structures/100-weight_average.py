#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) <= 0:
        return 0
    weight = 0
    sumtot = 0
    for x, y in my_list:
        weight += y
        sumtot += y * x
    return sumtot/weight
