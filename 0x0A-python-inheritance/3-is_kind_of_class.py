#!/usr/bin/python3
"""define a is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """
    a function that returns TRUE if the obj is an
    instance of or the class inherited or the specified class,
    and FALSE if it isnt.

    args:
        obj: an instance
        a_class: class
    """
    return isinstance(obj, a_class)
