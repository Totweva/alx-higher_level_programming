#!/usr/bin/python3
"""Define a rectangle class"""


class Rectangle:
    """implementing a rectangle class"""

    def __init__(self, width=0, height=0):
        """
        initialzing the class
        arg:
            width: private instance class
            height: private instance class
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """implementing the width instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        setting the width property
        args: value (int): value
        Raises:
            TypeError: if not an integer
            ValueError: if less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """implementing the height instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        setting the height property
        args: value (int): value
        Raises:
            TypeError: if not an integer
            ValueError: if less than zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """defining the area of a rectangle"""
        self.width = width
        self.height = height
        return (width * height)

    def perimeter(self):
        """defining the perimeter of the rectangle"""
        if width == 0 or height == 0:
            return 0
        elif p = (2 * (width + height))
        return p
