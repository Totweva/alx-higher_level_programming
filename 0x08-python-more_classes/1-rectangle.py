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
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """implementing the width instance"""
        self.__width = width

    @width.setter
    def width(self, value):
        """
        setting the width property
        Raises:
            TypeError: if not an integer
            ValueError: if less than zero
        """
        if not isinstance(int, value):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """implementing the height instance"""
        self.__height = height

    @height.setter
    def height(self, value):
        """
        setting the height property
        Raises:
            TypeError: if not an integer
            ValueError: if less than zero
        """
        if not isinstance(int, value):
            raise TypeError("height must be integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
