#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 1:
        addone = 0
    else:
        addone = tuple_a[0]
    if len(tuple_b) < 1:
        addtwo = 0
    else:
        addtwo = tuple_b[0]
    f = addone + addtwo
    if len(tuple_a) < 2:
        addone = 0
    else:
        addone = tuple_a[1]
    if len(tuple_b) < 2:
        addtwo = 0
    else:
        addtwo = tuple_b[1]
    s = addone + addtwo
    return (f, s)
tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
