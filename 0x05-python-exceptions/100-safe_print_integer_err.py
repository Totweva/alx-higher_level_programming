#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    flag = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        flag = False
        sys.stderr.write("Exception: {}\n".format(err))
    return flag
