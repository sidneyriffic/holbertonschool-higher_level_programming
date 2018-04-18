#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None or tuple_b is None:
        return None
    if len(tuple_a) < 1 or tuple_a[0] is None:
        addone = 0
    else:
        addone = tuple_a[0]
    if len(tuple_b) < 1 or tuple_b[0] is None:
        addtwo = 0
    else:
        addtwo = tuple_b[0]
    f = addone + addtwo
    if len(tuple_a) < 2 or tuple_a[1] is None:
        addone = 0
    else:
        addone = tuple_a[1]
    if len(tuple_b) < 2 or tuple_b[1] is None:
        addtwo = 0
    else:
        addtwo = tuple_b[1]
    s = addone + addtwo
    return (f, s)
