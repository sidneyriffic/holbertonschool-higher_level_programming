#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] in {"+", "-", "/", "*"}:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        if argv[2] == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        if argv[2] == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        if argv[2] == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
