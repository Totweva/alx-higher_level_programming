#!/usr/bin/python3
"""define a lookup function"""


def lookup(obj):
    """a function that lists all attrs and methods"""

    return list(dir(obj))
