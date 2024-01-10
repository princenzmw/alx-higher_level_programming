#!/usr/bin/python3
""" A script that adds all arguments to a Python list,
    and then save them to a file """


import sys
import os.path


if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__(
        "6-load_from_json_file"
    ).load_from_json_file

    file_path = "add_item.json"

    if os.path.isfile(file_path):
        data = load_from_json_file(file_path)
    else:
        data = []

    data.extend(sys.argv[1:])
    save_to_json_file(data, "add_item.json")
