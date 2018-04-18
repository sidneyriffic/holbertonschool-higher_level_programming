#!/usr/bin/python3
def no_c(my_string):
    newstr = ""
    for c in my_string:
        if (c != 'C') & (c != 'c'):
            newstr += c
    return newstr
