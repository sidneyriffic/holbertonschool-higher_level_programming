#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        for y in range(x):
            print("{:d}".format(my_list[y]), end = "")
    except ValueError:
        return y
    except IndexError:
        return y
    finally:
        print()
    return x
