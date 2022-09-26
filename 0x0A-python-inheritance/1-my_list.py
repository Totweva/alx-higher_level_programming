#!/usr/bin/python3
"""A class MyList that inherits from list"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """prints the list in ascending order"""

        _copy = sorted([i for i in self])
        print(_copy)
