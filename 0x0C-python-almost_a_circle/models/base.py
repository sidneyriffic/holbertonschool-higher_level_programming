#!/usr/bin/python3
"""Base geometry class"""
import json


class Base:
    """Base geometry class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """Returns a json string made out of the dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)

    def from_json_string(json_string):
        """Returns dictionary representations of geometry objects from JSON"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a geometry object from a dictionary"""
        from .rectangle import Rectangle
        from .square import Square
        if cls is Rectangle:
            newrect = Rectangle(1, 1)
            newrect.update(**dictionary)
            return newrect
        elif cls is Square:
            newsquare = Square(1)
            newsquare.update(**dictionary)
            return newsquare

    @classmethod
    def save_to_file(cls, list_objs):
        from .rectangle import Rectangle
        from .square import Square
        for idx in range(len(list_objs)):
            list_objs[idx] = list_objs[idx].to_dictionary()
        print(list_objs)
        if cls is Rectangle:
            with open("Rectangle.json", "w") as f:
                json.dump(list_objs, f)
        elif cls is Square:
            with open("Square.json", "w") as f:
                json.dump(list_objs, f)

    @classmethod
    def load_from_file(cls):
        from .rectangle import Rectangle
        from .square import Square
        if cls is Rectangle:
            with open("Rectangle.json", "r") as f:
                retlist = json.load(f)
                if retlist == "":
                    return []
                return retlist
        elif cls is Square:
            with open("Square.json", "r") as f:
                retlist = json.load(f)
                if retlist == "":
                    return []
                return retlist
