#!/usr/bin/python3
"""defining a rectangle subclass"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Initalize the subclass rectangle"""

    def __init__(self, width, height):
        """
        defining the subclass with width and height
        args:
            width: int
            height: int
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """defining the area of arectangle"""
        return self.__width * self__height

    def __str__(self):
        """print out as string"""
        return (f"[{self.__class__.__name__}] {self.__width}/{self.__height}")
