#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) - 1 == 0:
        print("{} arguments.".format(len(sys.argv) - 1))
    elif len(sys.argv) - 1 == 1:
        print("{} argument:".format(len(sys.argv) - 1))
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        a = 0
        for arg in sys.argv:
            if sys.argv.index(arg) != 0:
                a += 1
                print("{}: {}".format(a, arg))
