#!/usr/bin/python3
"""Defines a function that saves an object to a file as json string"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w") as f:
        json.dump(my_obj, f)
