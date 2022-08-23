#!/usr/bin/python3
for num in range(1, 88):
    if num < 10:
        print("0{}".format(num), end=", ")
    elif int(str(num)[1] + str(num)[0]) > num:
        print("{}".format(num), end=", ")
print("89")
