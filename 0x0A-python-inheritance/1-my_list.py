#!/usr/bin/python3
"""A class MyList that inherits from list"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """prints the list in ascending order"""
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
