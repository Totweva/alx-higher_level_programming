#!/usr/bin/python3
"""a module that prints square"""


def print_square(size):
    """
    a function that prints a square with "#"
    args:
        size: size lenght of the square
    Raises:
        TypeError: If not a integer
        ValueError: if less than zero
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
