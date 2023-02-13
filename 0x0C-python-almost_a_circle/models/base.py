#!/usr/bin/python3
"""Definition of a base model"""


class Base:
    """ a base class"""
    __nb_objects = 0

    def __init__(self. id=None):
        """
        Initializing base class
        Args:
            id (int)
        """
        if id is not None:
            self.id = id
        else:
            base.__nb_objects += 1
            self.id = self.__nb_objects
