#!/usr/bin/python3


class MagicClass:
    def __init(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius * self.__radius

    def circumference(self):
        return math.pi * 2 * self.__radius
