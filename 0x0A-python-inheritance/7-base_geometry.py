#!/usr/bin/python3
"""define a class"""


class BaseGeometry:
    """initializing a class"""


    def area(self):
        """
        defining the propety area
        Raises:
            Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
         """
        defining the propety integer_validator
        args:
            name: str
            value: int
        Raises:
            TypeError: if name is not a string
            ValueError: if if name is not greater than 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than zero")
