#!/usr/bin/python3
"""Defines a function that converts an object to a json string"""
import json


def to_json_string(my_obj):
    """Converts an object to a json string"""
    return json.dumps(my_obj)
