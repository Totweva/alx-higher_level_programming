#!/usr/bin/python3
"""a function that inserts a line of text"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text in each line after a specific string"""

    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w") as w:
        w.write(text)
