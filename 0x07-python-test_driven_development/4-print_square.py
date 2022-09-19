#!/usr/bin/python3
"""a function that prints a square with the character #"""


def print_square(size):
    """
    prints a square
    size: length of the square
    Return prints
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    print(('#' * size + '\n') * size, end='')
