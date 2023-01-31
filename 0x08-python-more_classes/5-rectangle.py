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
        return (self.__width * self.__height)

    def perimeter(self):
        """defining the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """print # as the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        _rec = ""
        for i in range(self.__height):
            for j in range(self.__width):
                _rec += "#"
            if i != self.__height - 1:
                _rec += "\n"
        return _rec

    def __repr__(self):
        """return string representation of rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """delete an instance with a messsage " bye rect..."""
        print("Bye rectangle...")
