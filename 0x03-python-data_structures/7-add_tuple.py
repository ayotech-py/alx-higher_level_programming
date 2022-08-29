#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0 and len(tuple_b) == 0:
        return 0, 0
    elif len(tuple_a) == 0:
        return tuple_b[0], tuple_b[1]
    elif len(tuple_b) == 0:
        return tuple_a[0], tuple_a[1]
    elif len(tuple_a) == 1 and len(tuple_b) == 1:
        add_a = tuple_a[0] + tuple_b[0]
        return add_a, 0
    elif len(tuple_a) == 1:
        add_a = tuple_a[0] + tuple_b[0]
        add_b = 0 + tuple_b[1]
        return add_a, add_b
    elif len(tuple_b) == 1:
        add_a = tuple_a[0] + tuple_b[0]
        add_b = tuple_a[1] + 0
        return add_a, add_b
    else:
        add_a = tuple_a[0] + tuple_b[0]
        add_b = tuple_a[1] + tuple_b[1]
        return add_a, add_b
