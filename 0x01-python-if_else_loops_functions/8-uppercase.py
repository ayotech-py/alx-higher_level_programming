#!/usr/bin/python3
def uppercase(str):
    string = ""
    for alpha in range(0, len(str)):
        if ord(str[alpha]) > 96 and ord(str[alpha]) < 123:
            string += chr(ord(str[alpha]) - 32)
        else:
            string += str[alpha]
    print("{}".format(string))
