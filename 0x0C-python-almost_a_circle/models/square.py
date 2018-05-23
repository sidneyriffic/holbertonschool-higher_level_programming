#!/usr/bin/python3
"""Square class based on Rectangle"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Square class based on Rectangle. No new attributes."""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updates Rectangle attributes. In the following order if positional:
        id, width, height, x, y
        """
        numargs = len(args)
        if numargs > 0:
            self.id = args[0]
        if numargs > 1:
            self.width = args[1]
            self.height = args[1]
        if numargs > 2:
            self.x = args[2]
        if numargs > 3:
            self.y = args[3]
        if numargs == 0:
            for key, value in kwargs.items():
                exec("self.{} = {}".format(key, value))

    def to_dictionary(self):
        """Returns a dictionary of the Rectangle instance's attributes"""
        newdict = {"id": self.id, "size": self.width,
                   "x": self.x, "y": self.y}
        return newdict
