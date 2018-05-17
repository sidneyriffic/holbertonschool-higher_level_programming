#!/usr/bin/python3
"""Student class"""


class Student:
    """Student class"""

    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.age = age

    def to_json(self, attrs=None):
        """Returns student's serializable dict elements as a dict"""
        filterattr = 0
        if type(attrs) == list:
            filterattr = 1
            for x in attrs:
                if type(x) is not str:
                    filterattr = 0
                    break
        retdict = {}
        objdict = self.__dict__
        for ele in objdict:
            if type(objdict[ele]) in [list, dict, str, int, bool]:
                if filterattr == 0 or ele in attrs:
                    retdict[ele] = objdict[ele]
        return retdict

    def reload_from_json(self, json):
        """Loads student attributes from json dict"""
        for ele in json:
            self.__dict__[ele] = json[ele]
