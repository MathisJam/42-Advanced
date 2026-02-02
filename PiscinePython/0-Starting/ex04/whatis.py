import sys


def whatis():
    if len(sys.argv) == 1:
        exit()

    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        exit()

    try:
        nb = int(sys.argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        exit()

    if nb % 2 == 0:
        print("I'm even")
    else:
        print("I'm odd")


whatis()
