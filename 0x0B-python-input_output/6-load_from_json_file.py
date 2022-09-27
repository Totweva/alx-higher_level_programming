#!/usr/bin/python3
"""a function that creates an Object"""


def load_from_json_file(filename):
    """creates an Object with a JSON file"""

    with open(filename) as f:
        return json.load(f)
