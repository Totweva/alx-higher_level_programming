#!/usr/bin/python3
"""defines a function that reads a file"""


def read_file(filename=""):
    """
    Reads a file
    args:
        filename (str): relative path to file

    return: none
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
