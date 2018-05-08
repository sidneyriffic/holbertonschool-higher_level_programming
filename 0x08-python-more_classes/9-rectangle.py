#!/usr/bin/python3
"""Contains the rectangle class"""


class Rectangle:
    """A rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initilizes a rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Delete a rectangle"""
        print("Bye rectangle...")
        if Rectangle.number_of_instances != 0:
            Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """width property"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """height property"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def __str__(self):
        """Returns rectangle str"""
        if self.width == 0 or self.height == 0:
            return ""
        string = ""
        for y in range(self.height - 1):
            string += str(self.print_symbol) * self.width + '\n'
        string += str(self.print_symbol) * self.width
        return string

    def __repr__(self):
        """Returns repr of the rectangle"""
        string = "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
        return string

    def area(self):
        """Returns area of a rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Returns perimeter of a rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return self.height * 2 + self.width * 2

    def bigger_or_equal(rect_1, rect_2):
        """Returns the greater of rect1 and rect2, rect1 if equal"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """Make a square using the rectangle class"""
        return cls(size, size)
