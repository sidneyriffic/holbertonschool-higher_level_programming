#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10
if number < 10:
    digit = digit - 10
print("Last digit of {:d} is {:d}".format(number, digit),
      end=' and is ')
if digit > 5:
    print("{}".format("greater than 5"))
elif digit == 0:
    print("{}".format("0"))
else:
    print("{}".format("less than 6 and not 0"))
