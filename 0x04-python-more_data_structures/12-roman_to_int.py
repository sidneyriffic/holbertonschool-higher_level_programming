#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    sumtot = 0
    prevval = 1000
    romandict = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}
    numbers = [romandict[x] for x in roman_string]
    for x in numbers:
        if x > prevval:
            sumtot -= prevval * 2
        prevval = x
        sumtot += x
    return sumtot
