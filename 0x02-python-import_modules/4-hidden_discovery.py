#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    for s in dir(sys):
        if s[0] != "_":
            print(s)
