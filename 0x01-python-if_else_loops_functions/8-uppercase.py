#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        char = letter
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            char = chr(ord(letter) - 32)
        print("{}".format(char), end='')
    print("")
