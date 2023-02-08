#!/usr/bin/python3
"""defines a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """
    write text to a file
    args:
        filename (str): relative path to a file
        texts (str): text to write to file
    returns: number of character written.
    """
    with open(filename="", 'w', encoding="utf-8") as f:
        return f.write(text)
