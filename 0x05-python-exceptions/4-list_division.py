#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            element = my_list_1[i] / my_list_2[i]
            new_list.append(element)
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except TypeError:
            new_list.append(0)
            print("Wrong type")
        except IndexError:
            new_list.append(0)
            print("out of range")
        finally:
            continue
    return new_list
