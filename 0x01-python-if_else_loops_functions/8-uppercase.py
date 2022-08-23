#!/usr/bin/python3
def uppercase(str):
    for alpha in range(0, len(str)):
        if ord(str[alpha]) > 96 and ord(str[alpha]) < 123:
            print("{}".format(chr(ord(str[alpha]) - 32)), end="")
        else:
            print("{}".format(str[alpha]), end="")
