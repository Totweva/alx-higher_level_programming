#!/usr/bin/python3
"""define a is_same_class function"""


def inherits_from(obj, a_class):
    """
    a function that returns TRUE if the obj is an
    instance that inherited from the specified class,
    and FALSE if it isnt.
    args:
        obj: instance
        a_class: class
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
