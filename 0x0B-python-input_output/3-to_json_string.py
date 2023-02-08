#!/usr/bin/python3
"""a function that returns JSON string"""
import json


def to_json_string(my_obj):
    """
    Returns a JSON rep of an obj(string)
    """
    return json.dumps(my_obj)
