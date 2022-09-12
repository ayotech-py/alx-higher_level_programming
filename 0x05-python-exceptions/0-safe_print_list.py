#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        a = 0
        for i in my_list:
            if i == a:
                break
            a += 1
            print('{}'.format(i), end='')
        print()
    except TypeError:
        pass
    return a
