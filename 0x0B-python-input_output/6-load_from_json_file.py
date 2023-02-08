#!/usr/bin/python3
"""
defines function to loads object to JSON file
"""
import json


def load_from_json_file(filename):
    """
    Loads an object to a text file using JSON representation
    """
    with open(filename) as f:
        return json.load(f)
