#!/usr/bin/python3
"""Definition of Rectangle class"""

from models.base import Base

__all__ = ['Rectangle']


class Rectangle(Base):
    """A rectangle class inherits base module"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializing Rectangle class
        Args:
            width (int)
            height (int)
            x (int): X postion
            y (int): Y postion
            id (int): Unique ID
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for heiight"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x position"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x position"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y position"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y position"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Compute the area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """orint in stdout the Rectangle instance with the character #"""
        if self.__height == 0 and self.__height == 0:
            print("")

        [print("") for i in range(self.__y)]
        for x in range(self.__height):
            [print(" ", end="") for i in range(self.__x)]
            [print("#", end="") for i in range(self.__width)]
            print("")

    def __str__(self):
        """string rep"""
        return ("[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__,
            self.id,
            self.__x.
            self.__y,
            self.__width,
            self.__height)
            )

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
