#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    add = 0
    for obj in my_list:
        if obj in new_list:
            continue
        else:
            new_list.append(obj)
    for num in new_list:
        add += num
    return add
