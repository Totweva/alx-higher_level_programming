#!/usr/bin/python3
""" A function that adds two integer """


def add_integer(a, b=98):
    """ Returns the addition two integer
    Float arguments are typecasted to ints before addition is performed.
    Raises:
    TypeError: if either of a or b is a non-integer and non-float.
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a or b must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
