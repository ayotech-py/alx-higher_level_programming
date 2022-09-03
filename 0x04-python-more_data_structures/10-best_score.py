#!/usr/bin/python3
def best_score(a_dictionary):
    dic_list = []
    for key in a_dictionary:
        dic_list.append(a_dictionary[key])
    largest = dic_list[0]
    for num in dic_list:
        if num > largest:
            largest = num
        else:
            continue
    return largest
