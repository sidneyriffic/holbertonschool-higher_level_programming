#!/usr/bin/python3
import sys


codes = {}
totalsize = 0
linesread = 0
try:
    for line in sys.stdin:
        line = line.split(" ")
        if line[-2] in codes:
            codes[line[-2]] += 1
        else:
            codes[line[-2]] = 1
        totalsize += int(line[-1])
        linesread += 1
        if linesread % 10 == 0:
            print("File size:", totalsize)
            for code in sorted(list(codes)):
                print("{}: {}".format(code, codes[code]))
finally:
    print("File size:", totalsize)
    for code in sorted(list(codes)):
        print("{}: {}".format(code, codes[code]))
