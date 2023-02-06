#!/usr/bin/python3
"""define a is_same_class function"""


def is_same_class(obj, a_class):
    """
    a function that returns TRUE if the obj is an
    instance of the specified class, and FALSE if it isnt

    args:
        obj:
        a_class:
    """
    x = a_class(dir(obj))
    for i in range(x):
       if i == obj:
           return True
       return False
