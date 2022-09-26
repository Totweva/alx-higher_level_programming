#!/usr/bin/python3
"""a function that returns the list of available attributes and methods of an object"""


def lookup(obj):
    """List available attributes and methods in an object
    Args:
        obj (object): object to lookup
    Return:
        List of attributes and methods
    """
    res = []
    if isinstance(obj, object):
        res = dir(obj)
    return res
