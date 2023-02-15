#!/usr/bin/python3
"""Models defines a rectangle class
"""
from models.rectangle import Rectangle

__all__ = ['Square']


class Square(Rectangle):
    """Class to create square objects
    Methods
    -------
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a rectangle object
        Args:
            size (int): hieght and width of square
            x (int): X postion
            y (int): Y postion
            id (int): Unique ID
        Return;
            None
        """
        super().__init__(size, size, x=x, y=y, id=id)

    @property
    def size(self):
        """size property"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """string representation of rectangle
        """
        _str = "[{}] ({}) {}/{} - {}"
        return _str.format(
                self.__class__.__name__,
                self.id,
                self.x,
                self.y,
                self.size,
        )

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
