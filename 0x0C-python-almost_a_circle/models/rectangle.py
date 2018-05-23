#!/usr/bin/python3
"""Rectangle class"""
from .base import Base


class Rectangle(Base):
    """Rectangle class

    Attributes:
    width - width of Rectangle
    height - height of Rectangle
    x - x coordinate of top left vertex of Rectangle
    y - y coordinate of top left vertex of Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 1:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 1:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns area of Rectangle"""
        return self.width * self.height

    def display(self):
        """Prints rectangle made of #"""
        for y in range(self.y):
            print()
        for h in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """Updates Rectangle attributes. In the following order if positional:
        id, width, height, x, y
        """
        numargs = len(args)
        if numargs > 0:
            self.id = args[0]
        if numargs > 1:
            self.width = args[1]
        if numargs > 2:
            self.height = args[2]
        if numargs > 3:
            self.x = args[3]
        if numargs > 4:
            self.y = args[4]
        if numargs == 0:
            for key, value in kwargs.items():
                exec("self.{} = {}".format(key, value))

    def to_dictionary(self):
        """Returns a dictionary of the Rectangle instance's attributes"""
        newdict = {"id": self.id, "width": self.width, "height": self.height,
                   "x": self.x, "y": self.y}
        return newdict
