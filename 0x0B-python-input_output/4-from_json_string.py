#!/usr/bin/python3
"""defines function to convert to object from JSON string"""
import json


def from_json_string(my_str):
    """Convert to object from JSon string"""
    return json.loads(my_str)
