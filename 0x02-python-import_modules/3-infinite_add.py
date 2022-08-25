#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sumArg = 0
    length = sys.argv[1:]
    for arg in length:
        sumArg += int(arg)
    print("{}".format(sumArg))
