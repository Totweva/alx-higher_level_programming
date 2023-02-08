#!/usr/bin/pyton3
"""
a script that adds all arguments to a Python list,
and then save them to a file
"""
import json
from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main():
    """reads a list from file and appends the arguments to it"""
    filename = "add_item.json"
    data = list(load_from_json_file(filename)) if path.exists(filename) else []
    for i in range(1, len(argv)):
        data.append(argv[i])
    save_to_json_file(data, filename)


if __name__ == "__main__":
    main()
