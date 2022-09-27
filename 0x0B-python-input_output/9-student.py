#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """a class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializing first_name(str), last_name(str) and age(int)"""
        self.first_name = first_name
        self.second_name = second_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the Student."""
        return self.__dict__
