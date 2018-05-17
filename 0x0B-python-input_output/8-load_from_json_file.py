#!/usr/bin/python3
"""Defines a function that loads an object from a file's json string"""
import json


def load_from_json_file(filename=""):
    with open(filename, "r") as f:
        return json.load(f)
