#!/usr/bin/python3
for i in range(ord('Z'), ord('A') - 1, -1):
    print(chr(i + (i % 2) * 32), end='')
