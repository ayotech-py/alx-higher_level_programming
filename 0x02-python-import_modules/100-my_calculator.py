#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    import sys
    arg = sys.argv
    if len(arg) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(arg[1])
    operator = arg[2]
    b = int(arg[3])
    if operator == '+':
        print("{} + {} = {}".format(a, b, cal.add(a, b)))
    elif operator == '-':
        print("{} - {} = {}".format(a, b, cal.sub(a, b)))
    elif operator == '*':
        print("{} * {} = {}".format(a, b, cal.mul(a, b)))
    elif operator == '/':
        print("{} / {} = {}".format(a, b, cal.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
