#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    if int(str(number)[-1]) > 5:
        print(f"Last digit of {number:d} is {str(number)[-1]} \
and is greater than 5")
    elif int(str(number)[-1]) == 0:
        print(f"Last digit of {number:d} is {str(number)[-1]} and is 0")
    elif int(str(number)[-1]) < 6 and int(str(number)[-1]) != 0:
        sign = ""
        if str(number)[0] == "-":
            sign = "-"
        print(f"Last digit of {number:d} is {sign}{str(number)[-1]} \
and is less than 6 and not 0")
elif number < 0:
    if int(str(number)[-1]) == 0:
        print(f"Last digit of {number:d} is {str(number)[-1]} and is 0")
    elif -1 * int(str(number)[-1]) < 6 and -1 * int(str(number)[-1]) != 0:
        print(f"Last digit of {number:d} is -{str(number)[-1]} \
and is less than 6 and not 0")
elif int(str(number)[-1]) == 0:
    print(f"Last digit of {number:d} is {str(number)[-1]} and is 0")
