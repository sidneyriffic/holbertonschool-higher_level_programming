#!/usr/bin/python3
"""Student class"""


class Student:
    """Student class"""

    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.age = age

    def to_json(self):
        """Returns student's serializable dict elements as a dict"""
        retdict = {}
        objdict = self.__dict__
        for ele in objdict:
            if type(objdict[ele]) in [list, dict, str, int, bool]:
                retdict[ele] = objdict[ele]
        return retdict
