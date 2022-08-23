#!/usr/bin/python3
def pow(a, b):
    i = 1
    power = 1
    if b >= 0:
        while i <= b:
            power *= a
            i += 1
    else:
        b = -1 * b
        while i <= b:
            power *= a
            i += 1
        power = 1/power
    return power
