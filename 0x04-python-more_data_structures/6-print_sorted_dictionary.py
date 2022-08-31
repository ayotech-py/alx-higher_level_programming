#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic_list = sorted(list(a_dictionary))
    for key in dic_list:
        print("{}: {}".format(key, a_dictionary[key]))
