#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {:d} is {:d}".format(number, abs(number) % 10),
      end=' and is ')
if abs(number) % 10 > 5:
    print("{}".format("greater than 5"))
elif abs(number) % 10 == 0:
    print("{}".format("0"))
else:
    print("{}".format("less than 6 and not 0"))
