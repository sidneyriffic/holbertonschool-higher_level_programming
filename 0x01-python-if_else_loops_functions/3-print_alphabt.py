#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if ord('q') != i and ord('e') != i:
        print(chr(i), end='')
