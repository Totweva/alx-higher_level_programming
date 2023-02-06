#!/usr/bin/python3
"""define square subclass"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Initalize the subclass rectangle"""

    def __init__(self, size):
        """
        defining the subclass with size
        args:
            size: int
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """defining the area of a Square"""
        return self.__size * self_size

    def __str__(self):
        """print as a string"""
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"
