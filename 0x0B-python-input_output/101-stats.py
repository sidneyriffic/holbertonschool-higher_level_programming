#!/usr/bin/python3
import sys


stdin = sys.stdin
codes = {}
totalsize = 0
linesread = 0
try:
    while True:
        line = stdin.readline()
        line = line.split(" ")
        if line[-2] in codes:
            codes[line[-2]] += 1
        else:
            codes[line[-2]] = 1
        totalsize += int(line[-1])
        linesread += 1
        if linesread % 10 == 0:
            print("File size:", totalsize)
            for code in codes:
                print("{}: {}\n".format(code, codes[code]))
except KeyboardInterrupt:
    print("File size:", totalsize)
    for code in codes:
        print("{}: {}\n".format(code, codes[code]))
