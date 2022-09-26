#!/usr/bin/python3
"""A class MyList that inherits from list"""


class MyList(list):
    """
    A class that inherits from list
    """

    def print_sorted(self):
        """Pubilc instance method that prints the list in ascending order"""

        print(sorted(self))
