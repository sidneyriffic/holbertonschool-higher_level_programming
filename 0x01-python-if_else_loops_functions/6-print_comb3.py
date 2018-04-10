#!/usr/bin/python3
for i in range(0, 89):
    if i % 10 > i // 10:
        print("{:02}".format(i), ", ", sep='', end='')
print("89")
