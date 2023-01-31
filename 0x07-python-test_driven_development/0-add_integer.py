#!/usr/bin/python3
"""defines an integer addition function"""


def add_integer(a, b=98):
    """
    A function that adds 2 interger
    args:
        a: parameter 1
        b: parameter 2
    Raises:
        TypeError: if either of a or b is a non-integer and non-float
    """
    if ((not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be integer")
    return (int(a) + int(b))
