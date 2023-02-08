#!/usr/bin/python3
"""defnes the funton that appends string to end of text file"""


def append_write(filename="", text=""):
    """
    append text to end of text file
    args:
        filename (str): path to file
        text (str): text to be appended
    return: number of characters added.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
