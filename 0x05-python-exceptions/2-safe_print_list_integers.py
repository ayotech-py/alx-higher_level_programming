#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    a = 0
    for i in my_list:
        if a == x:
            break
        try:
            print("{:d}".format(i), end="")
        except (TypeError, ValueError, NameError):
            pass
        a += 1
    print()
    return a
