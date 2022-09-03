#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) is 0:
        return None
    dic_list = []
    for key in a_dictionary:
        dic_list.append(a_dictionary[key])
    largest = dic_list[0]
    for num in dic_list:
        if num > largest:
            largest = num
    for large_key in a_dictionary:
        if a_dictionary[large_key] == largest:
            return large_key
