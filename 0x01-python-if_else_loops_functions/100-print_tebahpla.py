#!/usr/bin/python3
for i in range(ord('Z'), ord('A') - 1, -1):
    print("{}".format(chr(i + ((i + 1) % 2) * 32)), end='')
