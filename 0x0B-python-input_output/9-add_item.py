#!/usr/bin/python3
"""Makes a list from args and saves them to a file in json format"""
savejson = __import__("7-save_to_json_file").save_to_json_file
loadjson = __import__("8-load_from_json_file").load_from_json_file
import sys, json


listy = load_from_json_file("add_item.json")
print listy
for arg in sys.argv:
    listy.append(arg)
